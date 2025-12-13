import tkinter as tk
from tkinter import ttk

class IconCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg='white', **kwargs)
        self.bind("<Button-1>", self.on_click)
        self.icons = []
        # Sürükleme işlemi için:
        self.drag_data = {"item": None, "x": 0, "y": 0}

    def on_click(self, event):
        if hasattr(self.master.master, "selected_icon"):
            icon = self.master.master.selected_icon
            self.create_text(event.x, event.y, text=icon, font=('Arial', 16), tags="icon")
            self.icons.append((icon, event.x, event.y))

            # Tree'ye ekle
            self.master.master.add_tree_item(icon)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Icon Panel Interface")
        self.geometry("900x600")
        self.selected_icon = None

        self.create_menu()
        self.create_toolbar()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=lambda: print("New File"))
        file_menu.add_command(label="Open", command=lambda: print("Open File"))
        file_menu.add_command(label="Save", command=lambda: print("Save File"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=lambda: print("Undo"))
        edit_menu.add_command(label="Redo", command=lambda: print("Redo"))
        menubar.add_cascade(label="Edit", menu=edit_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Settings", command=lambda: print("Settings"))
        tools_menu.add_command(label="Preferences", command=lambda: print("Preferences"))
        menubar.add_cascade(label="Tools", menu=tools_menu)

        self.config(menu=menubar)


    def create_toolbar(self):
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED, bg="lightgray")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        new_btn = tk.Button(toolbar, text="New", command=lambda: print("Toolbar: New"))
        open_btn = tk.Button(toolbar, text="Open", command=lambda: print("Toolbar: Open"))
        save_btn = tk.Button(toolbar, text="Save", command=lambda: print("Toolbar: Save"))
        settings_btn = tk.Button(toolbar, text="Settings", command=lambda: print("Toolbar: Settings"))

        for btn in [new_btn, open_btn, save_btn, settings_btn]:
            btn.pack(side=tk.LEFT, padx=2, pady=2)

    def create_widgets(self):
        # Sol Panel: İkon listesi
        icon_frame = tk.Frame(self, width=120, bg='lightgray')
        icon_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(icon_frame, text="Icons", bg='lightgray', font=('Arial', 10, 'bold')).pack(pady=5)

        self.icon_listbox = tk.Listbox(icon_frame, font=('Arial', 12), height=10, exportselection=False)
        self.icon_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.icons = ['★', '☀', '⚙', '⚠', '✉', '.', 'F', 'A', 'T', 'İ', 'H']
        for icon in self.icons:
            self.icon_listbox.insert(tk.END, icon)

        self.icon_listbox.bind("<<ListboxSelect>>", self.on_icon_select)

        # Orta Panel: Canvas
        canvas_frame = tk.Frame(self, bg='white')
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = IconCanvas(canvas_frame)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Sağ Panel: Ağaç yapısı
        tree_frame = tk.Frame(self, width=200, bg='lightblue')
        tree_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(tree_frame)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.root_node = self.tree.insert('', 'end', text='Root')
        self.icons_node = self.tree.insert(self.root_node, 'end', text='Placed Icons')

        # Diğer örnek dallar
        child1 = self.tree.insert(self.root_node, 'end', text='Other Node')
        self.tree.insert(child1, 'end', text='Subnode')

    def on_icon_select(self, event):
        selection = self.icon_listbox.curselection()
        if selection:
            index = selection[0]
            self.selected_icon = self.icons[index]
            print(f"Selected icon: {self.selected_icon}")

    def add_tree_item(self, icon):
        self.tree.insert(self.icons_node, 'end', text=icon)
        self.tree.item(self.icons_node, open=True)  # Otomatik aç

    def on_click(self, event):
        if hasattr(self.master.master, "selected_icon"):
            icon = self.master.master.selected_icon
            item = self.create_text(event.x, event.y, text=icon, font=('Arial', 16), tags=("icon", "draggable"))
            self.icons.append((icon, event.x, event.y))

            # Tree'ye ekle
            self.master.master.add_tree_item(icon)

            # Sürükleme olaylarını bağla
            self.tag_bind(item, "<ButtonPress-1>", self.on_start_drag)
            self.tag_bind(item, "<B1-Motion>", self.on_drag)
            self.tag_bind(item, "<ButtonRelease-1>", self.on_drop)

    def on_start_drag(self, event):
        # En alttaki elemanı al (birden fazla olabilir)
        item = self.find_closest(event.x, event.y)[0]
        self.drag_data["item"] = item
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        if self.drag_data["item"]:
            self.move(self.drag_data["item"], dx, dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_drop(self, event):
        self.drag_data["item"] = None

if __name__ == "__main__":
    app = App()
    app.mainloop()
