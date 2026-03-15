import tkinter as tk
from tkinter import messagebox

class CodeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic-First Python Builder")
        self.root.geometry("900x600")

    # --- INTERNAL DATA (Your 'Hardcoded' Database) ---
    # You can add more logic rules here easily without a real database.
        self.function_db = {
            "Print Text": {"syntax": "print('{value}')", "color": "#4CAF50"},
            "Calculate": {"syntax": "print(f'Result: {{{value}}}')", "color": "#FF9800"},
            "Variable": {"syntax": "{value}", "color": "#2196F3"}
        }

        # ----- SIDEBAR -----
        self.block_panel = tk.Frame(root, bg="#2b2b2b", width=200)
        self.block_panel.pack(side="left", fill="y")

        tk.Label(self.block_panel, text="Logic Blocks", bg="#2b2b2b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

        for name in self.function_db:
            btn = tk.Button(self.block_panel, text=name, 
                            command=lambda n=name: self.add_block(n),
                            bg=self.function_db[name]["color"], fg="white", width=15)
            btn.pack(pady=5, padx=10)

        # ----- WORKSPACE -----
        self.workspace = tk.Frame(root, bg="#1e1e1e")
        self.workspace.pack(fill="both", expand=True)

        # ----- RUN BAR -----
        self.action_panel = tk.Frame(root, bg="#333", height=50)
        self.action_panel.pack(side="bottom", fill="x")

        tk.Button(self.action_panel, text="▶ RUN LOGIC", command=self.run_code, 
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=10)
        
        self.active_blocks = []

    def add_block(self, name):
        config = self.function_db[name]
        frame = tk.Frame(self.workspace, bg=config["color"], pady=5)
        frame.pack(pady=5, anchor="w", padx=20)

        tk.Label(frame, text=f"{name}:", bg=config["color"], fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        entry = tk.Entry(frame, width=40)
        entry.pack(side="left", padx=5)

        block_data = [name, entry, frame]
        self.active_blocks.append(block_data)
        
        # Delete Button
        tk.Button(frame, text="✕", command=lambda: self.remove_block(block_data), 
                  bg="#f44336", fg="white", bd=0).pack(side="right", padx=5)

    def remove_block(self, block_data):
        block_data[2].destroy()
        self.active_blocks.remove(block_data)

    def run_code(self):
        full_script = []
        for name, entry, frame in self.active_blocks:
            val = entry.get()
            template = self.function_db[name]["syntax"]
            # This replaces the placeholder with your math or text
            line = template.replace("{value}", val)
            full_script.append(line)
        
        final_code = "\n".join(full_script)
        
        print("\n--- Running Your Logic ---")
        try:
            # exec() is the 'magic' that runs the string as real Python
            exec(final_code)
        except Exception as e:
            messagebox.showerror("Logic Error", f"Something went wrong:\n{e}")
        print("--------------------------")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeBuilder(root)
    root.mainloop()