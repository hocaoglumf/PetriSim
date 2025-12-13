import math
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parametreler ve Sabitler
# -----------------------------
V = 0.10                 # m^3
Ps = 800e3               # Pa
Ts = 300.0               # K
d = 8e-3                 # m
A = math.pi * (d**2) / 4 # m^2
Cd = 0.82                # -
T_inf = 300.0            # K (ambient)
UA = 20.0                # W/K
P0 = 100e3               # Pa
T0 = 300.0               # K

R = 287.0                # J/(kg K) for air
gamma = 1.4              # -
cv = R / (gamma - 1.0)   # J/(kg K)
cp = gamma * R / (gamma - 1.0)

# Simülasyon ayarları
t_end = 60.0             # s
dt = 0.005               # s  (RK4 ile 12k adım)
show_plots = True        # Grafik çizilsin mi?

# -----------------------------
# Yardımcı Fonksiyonlar
# -----------------------------
def tank_pressure(m, T):
    """Ideal gaz: P = m R T / V"""
    return (m * R * T) / V

def mdot_orifice(P_tank):
    """Kaynak -> tank orifis akışı (isentropik orifis modeli).
       P_tank >= Ps ise geri akış yok varsayımı ile mdot = 0."""
    if P_tank >= Ps:
        return 0.0
    Pi = P_tank / Ps
    Pi_star = (2.0 / (gamma + 1.0)) ** (gamma / (gamma - 1.0))
    if Pi <= Pi_star:  # choked
        term = (2.0 / (gamma + 1.0)) ** ((gamma + 1.0) / (2.0 * (gamma - 1.0)))
        mdot = Cd * A * Ps * math.sqrt(gamma / (R * Ts)) * term
    else:  # non-choked
        inside = (Pi ** (2.0 / gamma) - Pi ** ((gamma + 1.0) / gamma))
        inside = max(inside, 0.0)  # sayısal güvenlik
        mdot = Cd * A * Ps * math.sqrt( (2.0 * gamma) / (R * Ts * (gamma - 1.0)) * inside )
    return mdot

def rhs(t, y):
    """Durum: y = [m, T]. Çıkış: dy/dt = [dm/dt, dT/dt], ayrıca Qdot (diagnostic)."""
    m, T = y
    P_tank = tank_pressure(m, T)
    mdot_in = mdot_orifice(P_tank)
    Qdot = -UA * (T - T_inf)  # tanka giren ısı pozitif; T>T_inf ise negatif

    dmdt = mdot_in
    # dT/dt = [ mdot_in*(gamma*Ts - T) + Qdot/cv ] / m
    # m çok küçük olmasın diye küçük alt sınır:
    m_eff = max(m, 1e-8)
    dTdt = ( mdot_in * (gamma * Ts - T) + Qdot / cv ) / m_eff

    return np.array([dmdt, dTdt]), Qdot

def rk4_step(t, y, h):
    """Tek adım RK4. Diagnostik olarak Qdot özeti de dönelim (trapz için)."""
    k1, Q1 = rhs(t, y)
    k2, Q2 = rhs(t + 0.5*h, y + 0.5*h*k1)
    k3, Q3 = rhs(t + 0.5*h, y + 0.5*h*k2)
    k4, Q4 = rhs(t + h,     y + h*k3)

    y_next = y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    # Qdot için RK4 ortalaması (entegral doğruluğu için iyi bir yaklaşım)
    Qdot_avg = (Q1 + 2*Q2 + 2*Q3 + Q4) / 6.0
    return y_next, Qdot_avg

# -----------------------------
# Başlangıç Koşulları
# -----------------------------
m0 = P0 * V / (R * T0)   # m = P V / (R T)
y = np.array([m0, T0])

# Kayıt dizileri
N = int(t_end / dt) + 1
t_arr = np.zeros(N)
m_arr = np.zeros(N)
T_arr = np.zeros(N)
P_arr = np.zeros(N)

# Isı integrali (tanka giren ısı +)
Q_total = 0.0

# 600 kPa anı
t_reach_600kpa = None
P_target = 600e3

# -----------------------------
# Zaman İlerlemesi
# -----------------------------
t = 0.0
for i in range(N):
    m, T = y
    P = tank_pressure(m, T)

    t_arr[i] = t
    m_arr[i] = m
    T_arr[i] = T
    P_arr[i] = P

    if t_reach_600kpa is None and P >= P_target:
        t_reach_600kpa = t

    # Son adımda çık
    if i == N-1:
        break

    # RK4
    y_next, Qdot_avg = rk4_step(t, y, dt)
    Q_total += Qdot_avg * dt

    # İleri
    y = y_next
    t += dt

# -----------------------------
# Sonuçların Yazdırılması
# -----------------------------
print("=== Sonuçlar ===")
print(f"600 kPa'a ulaşma zamanı: {t_reach_600kpa:.3f} s" if t_reach_600kpa is not None
      else "600 kPa'a 60 s içinde ulaşılamadı.")
print(f"t=60 s son durum:")
print(f"  P = {P_arr[-1]/1e3:.2f} kPa")
print(f"  T = {T_arr[-1]:.2f} K")
print(f"  m = {m_arr[-1]:.5f} kg")
print(f"Toplam ısı (tanka giren +): Q_total = {Q_total/1e3:.3f} kJ")

# -----------------------------
# (İsteğe Bağlı) Grafikler
# -----------------------------
if show_plots:
    plt.figure()
    plt.plot(t_arr, P_arr/1e3)
    plt.xlabel("t (s)")
    plt.ylabel("P (kPa)")
    plt.title("Tank Basıncı")

    plt.figure()
    plt.plot(t_arr, T_arr)
    plt.xlabel("t (s)")
    plt.ylabel("T (K)")
    plt.title("Tank Sıcaklığı")

    plt.figure()
    plt.plot(t_arr, m_arr)
    plt.xlabel("t (s)")
    plt.ylabel("m (kg)")
    plt.title("Tank Kütlesi")

    plt.show()
