import tkinter as tk

class CodeBuilder:
    # Changed _init_ to __init__
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Code Builder")
        self.root.geometry("800x500")

        # ----- LEFT PANEL (BLOCKS) -----
        self.block_panel = tk.Frame(root, bg="#2b2b2b", width=200)
        self.block_panel.pack(side="left", fill="y")

        tk.Label(
            self.block_panel,
            text="Blocks",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 14)
        ).pack(pady=10)

        self.print_block_button = tk.Button(
            self.block_panel,
            text="print",
            command=self.add_print_block,
            bg="#4CAF50",
            fg="white",
            width=10
        )
        self.print_block_button.pack(pady=5)

        # ----- WORKSPACE -----
        self.workspace = tk.Frame(root, bg="#1e1e1e")
        self.workspace.pack(fill="both", expand=True)

        tk.Label(
            self.workspace,
            text="Workspace",
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 14)
        ).pack(anchor="nw", padx=10, pady=10)

        # ----- RUN BUTTON -----
        self.run_button = tk.Button(
            root,
            text="Run",
            command=self.run_code,
            bg="#2196F3",
            fg="white"
        )
        self.run_button.pack(side="bottom", pady=10)

        self.blocks = []

    def add_print_block(self):
        frame = tk.Frame(self.workspace, bg="#4CAF50", pady=5)
        
        label = tk.Label(frame, text="print", bg="#4CAF50", fg="white")
        label.pack(side="left", padx=5)

        entry = tk.Entry(frame)
        entry.pack(side="left", padx=5)

        frame.pack(pady=5, anchor="w", padx=20)
        self.blocks.append(entry)

    def run_code(self):
        # Using a line separator for clarity in the console
        print("\n" + "="*20)
        print("Program Output:")
        for entry in self.blocks:
            text = entry.get()
            print(text)
        print("="*20)

root = tk.Tk()
app = CodeBuilder(root)
root.mainloop()
