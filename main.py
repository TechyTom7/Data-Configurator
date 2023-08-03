import tkinter as tk
import pandas as pd
import os

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Data Configurator')

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        self.error_pos = 100

        self.border_gap = 10

        self.add_objects()
        self.window.mainloop()

    def destroy_warning(self, label):
        label.destroy()
        self.error_pos -= 50

    def update_output(self, text: str, error=False):
        warning_lable = tk.Label(self.window, text=text, foreground='red' if error else 'white',
                                 font=('Brass Mono', 30), background='grey')
        warning_lable.place(x=400, y=self.error_pos)
        self.error_pos += 50
        self.canvas.after(5000, lambda: self.destroy_warning(warning_lable))


    def submit_file_path(self, file_path: str):
        if file_path.endswith('.xlsx') or file_path.endswith('.csv'):
            self.current_file_text.config(text=f"Current: {file_path}", foreground='black')
            self.update_output('Updated file path')
        else:
            self.current_file_text.config(text=f"Current: {file_path}", foreground='red')
            self.update_output('Invalid file path', True)

    def add_objects(self):

        title_text = tk.Label(self.window, text='Data Configurator', font=('Arial Rounded MT bold', 45))
        title_text.place(x=10, y=10)

        instructions_file_field = tk.Label(self.window,
                                           text='Please input the file path. \nMust end in .xlsx or .csv to work.',
                                           font=('Brass Mono', 20), justify='left')
        instructions_file_field.place(x=10, y=100)

        file_field = tk.Entry(self.window, font=('Brass Mono', 20))
        file_field.place(x=10, y=160)

        enter_file_btn = tk.Button(self.window, text='Submit', font=('Avenir', 20),
                                   command=lambda: self.submit_file_path(file_field.get()))
        enter_file_btn.place(x=260, y=160)

        output_box = self.canvas.create_rectangle(400, 100, 750, 300, fill='grey')
        output_title = tk.Label(self.window, text='Output', font=('Avenir', 30))
        output_title.place(x=670, y=60,  anchor='center')

        self.current_file_text = tk.Label(self.window, text='No current file', font=('Brass Mono', 30))
        self.current_file_text.place(x=180, y=220, anchor='center')


if __name__ == '__main__':
    App()

