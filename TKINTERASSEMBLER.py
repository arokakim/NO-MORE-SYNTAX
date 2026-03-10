import tkinter as tk

class CodeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Code Builder Prototype")
        self.root.geometry("900x600")

        # --- SIMULATED DATABASE ---
        # This is where you'll eventually pull from your SQL database
        self.function_db = {
            "print": {"syntax": "print('{value}')", "color": "#4CAF50"},
            "calculate": {"syntax": "result = {value} * 2\nprint(result)", "color": "#FF9800"},
            "sleep": {"syntax": "import time\ntime.sleep({value})", "color": "#9C27B0"}
        }

        # ----- LEFT PANEL (BLOCKS) -----
        self.block_panel = tk.Frame(root, bg="#2b2b2b", width=200)
        self.block_panel.pack(side="left", fill="y")

        tk.Label(self.block_panel, text="Block Library", bg="#2b2b2b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

        # Create buttons dynamically based on our "database"
        for func_name in self.function_db:
            btn = tk.Button(
                self.block_panel, 
                text=f"Add {func_name}", 
                command=lambda f=func_name: self.add_block(f),
                bg=self.function_db[func_name]["color"],
                fg="white", width=15
            )
            btn.pack(pady=5, padx=10)

        # ----- WORKSPACE -----
        self.workspace = tk.Frame(root, bg="#1e1e1e")
        self.workspace.pack(fill="both", expand=True)

        # ----- ACTION PANEL -----
        self.action_panel = tk.Frame(root, bg="#333", height=50)
        self.action_panel.pack(side="bottom", fill="x")

        tk.Button(self.action_panel, text="Run Code", command=self.run_code, bg="#2196F3", fg="white", width=12).pack(side="left", padx=10, pady=10)
        tk.Button(self.action_panel, text="Export Script", command=self.export_code, bg="#757575", fg="white", width=12).pack(side="left", padx=10)

        self.active_blocks = [] # Stores tuples: (function_name, entry_widget)

    def add_block(self, func_name):
        config = self.function_db[func_name]
        frame = tk.Frame(self.workspace, bg=config["color"], pady=5)
        frame.pack(pady=5, anchor="w", padx=20)

        tk.Label(frame, text=f"{func_name}:", bg=config["color"], fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)

        entry = tk.Entry(frame, width=30)
        entry.pack(side="left", padx=5)

        # Track both the function type and the widget to extract data later
        self.active_blocks.append((func_name, entry))

    def generate_full_script(self):
        full_script = []
        for func_name, entry in self.active_blocks:
            val = entry.get()
            # Pull syntax from DB and swap the placeholder
            template = self.function_db[func_name]["syntax"]
            line = template.replace("{value}", val)
            full_script.append(line)
        return "\n".join(full_script)

    def run_code(self):
        print("\n--- Executing Visual Program ---")
        script = self.generate_full_script()
        print(script) # In the real version, you might use exec(script)
        print("--------------------------------")

    def export_code(self):
        script = self.generate_full_script()
        with open("generated_script.py", "w") as f:
            f.write(script)
        print("Successfully saved to generated_script.py!")

root = tk.Tk()
app = CodeBuilder(root)
root.mainloop()
