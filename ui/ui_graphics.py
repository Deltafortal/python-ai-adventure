import tkinter as tk
from tkinter import scrolledtext

class GraphicalUIManager:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("AI Adventure")
        self.root.geometry("700x650")
        self.root.configure(bg="#212121")
        



        title = tk.Label(self.root, text="🐉 Python AI RPG", font=("Helvetica", 16, "bold"), bg="#212121", fg="#ffffff")
        title.pack(pady=10)



        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=70, height=18, 
                                                   font=("Georgia", 12), bg="#1e1e1e", fg="#d4d4d4", 
                                                   padx=15, pady=15, borderwidth=0)
        
        self.text_area.pack(pady=10, fill="both", expand=True, padx=20)
        self.text_area.config(state=tk.DISABLED)
        


        self.choice_frame = tk.Frame(self.root, bg="#212121")
        self.choice_frame.pack(pady=15, fill="x")
        
        self.selected_target = None



    def display_text(self, text):

        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"\n{text}\n")
        self.text_area.see(tk.END)
        self.text_area.config(state=tk.DISABLED)
        self.root.update()




    def get_choice(self, options):
        for widget in self.choice_frame.winfo_children():
            widget.destroy()
            
        self.selected_target = None
        
        for opt in options:
            btn = tk.Button(self.choice_frame, text=opt['label'], font=("Helvetica", 11),
                            bg="#333333", fg="white", activebackground="#555555", activeforeground="white",
                            cursor="hand2", relief="flat",
                            command=lambda t=opt['target']: self._on_select(t))
            btn.pack(side="top", fill="x", padx=50, pady=5)
            


        #Wait until the user selects an option
        while self.selected_target is None:
            self.root.update()
            


        for widget in self.choice_frame.winfo_children():
            widget.destroy()
            


        return self.selected_target





    def _on_select(self, target):
        self.selected_target = target





    def get_text_input(self, prompt_text):

        for widget in self.choice_frame.winfo_children():
            widget.destroy()
            


        self.input_result = None

        
        lbl = tk.Label(self.choice_frame, text=prompt_text, font=("Helvetica", 11), bg="#212121", fg="white")
        lbl.pack(pady=5)
        


        entry = tk.Text(self.choice_frame, width=60, height=4, font=("Helvetica", 11), 
                        bg="#1e1e1e", fg="white", insertbackground="white", borderwidth=1)
        entry.pack(pady=5)
        


        def on_submit():

            self.input_result = entry.get("1.0", "end-1c").strip()
            

        submit_btn = tk.Button(self.choice_frame, text="Submit", font=("Helvetica", 11, "bold"),
                               bg="#2e7d32", fg="white", activebackground="#388e3c",
                               cursor="hand2", relief="flat", command=on_submit)
        submit_btn.pack(pady=10)
        

        #Wait until the user submits their input
        while self.input_result is None:
            self.root.update()
            


        for widget in self.choice_frame.winfo_children():
            widget.destroy()
            

        return self.input_result