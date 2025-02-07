import pytholog as pl

# Yeni bir mantık bilgi tabanı oluştur
factorial_model = pl.KnowledgeBase("factorial")

# Faktöriyel için kuralları ekle
factorial_model(["factorial(0, 1)",
    "factorial(N, F) :- N1 is N - 1, factorial(N1, F1), F is N * F1"])

# Faktöriyel hesaplayan fonksiyon
def calculate_factorial(n):
    # Sorguyu tanımlıyoruz
    query = f"factorial({n}, Result)"
    # Sorguyu çalıştırıyoruz
    result = factorial_model.query(query)
    if result:  # Eğer sonuç dönerse
        return result[0][0]
    else:
        return "Hesaplanamadı"

# Kullanıcıdan bir sayı alıp faktöriyel hesaplayalım
number = 2
print(f"{number}! = {calculate_factorial(number)}")
