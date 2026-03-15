import tkinter as tk
from tkinter import messagebox

class CodeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Code Builder Prototype")
        self.root.geometry("900x600")

        # --- REFINED DATABASE ---
        self.function_db = {
            "print": {"syntax": "print('{value}')", "color": "#4CAF50"},
            # Notice the change here: we wrap {value} in eval() or just let it run
            "calculate": {"syntax": "print(f'Result: {{{value}}}')", "color": "#FF9800"},
            "raw_code": {"syntax": "{value}", "color": "#2196F3"}
        }

        # ----- UI SETUP (Condensed for brevity) -----
        self.block_panel = tk.Frame(root, bg="#2b2b2b", width=200)
        self.block_panel.pack(side="left", fill="y")

        for func_name in self.function_db:
            btn = tk.Button(self.block_panel, text=f"Add {func_name}", 
                            command=lambda f=func_name: self.add_block(f),
                            bg=self.function_db[func_name]["color"], fg="white", width=15)
            btn.pack(pady=5, padx=10)

        self.workspace = tk.Frame(root, bg="#1e1e1e")
        self.workspace.pack(fill="both", expand=True)

        self.action_panel = tk.Frame(root, bg="#333", height=50)
        self.action_panel.pack(side="bottom", fill="x")

        tk.Button(self.action_panel, text="▶ Run Code", command=self.run_code, bg="#4CAF50", fg="white").pack(side="left", padx=10, pady=10)
        
        self.active_blocks = []

    def add_block(self, func_name):
        config = self.function_db[func_name]
        frame = tk.Frame(self.workspace, bg=config["color"], pady=5)
        frame.pack(pady=5, anchor="w", padx=20)

        tk.Label(frame, text=f"{func_name}:", bg=config["color"], fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        entry = tk.Entry(frame, width=30)
        entry.pack(side="left", padx=5)

        block_data = [func_name, entry, frame]
        self.active_blocks.append(block_data)
        
        # Delete Button
        tk.Button(frame, text="✕", command=lambda: self.remove_block(block_data), bg="#f44336", fg="white").pack(side="right", padx=5)

    def remove_block(self, block_data):
        block_data[2].destroy()
        self.active_blocks.remove(block_data)

    def generate_full_script(self):
        full_script = []
        for func_name, entry, frame in self.active_blocks:
            val = entry.get()
            template = self.function_db[func_name]["syntax"]
            # Formatting the template with the user input
            line = template.replace("{value}", val)
            full_script.append(line)
        return "\n".join(full_script)

    def run_code(self):
        """This method now executes the code instead of just printing the string."""
        script = self.generate_full_script()
        print("\n--- Executing Program ---")
        try:
            # exec() takes a string and runs it as actual Python code
            exec(script) 
        except Exception as e:
            print(f"Error in your blocks: {e}")
            messagebox.showerror("Runtime Error", str(e))
        print("-------------------------")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeBuilder(root)
    root.mainloop()