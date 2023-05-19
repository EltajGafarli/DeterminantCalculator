import tkinter
import tkinter as tk
from tkinter import INSERT
from tkinter import messagebox

from determinant import Matrix
from determinant import MatrixException
from generate_matrix import convert_matrix_to_string
from generate_matrix import generate_matrix


def convert_to_integer_list(text: str):
    try:
        row = list(map(int, text.split()))
        return row
    except ValueError as error:
        raise MatrixException("Matris ədədlərdən ibarət olmalıdır!")


error_text: str = None


def get_text() -> str:
    global error_text
    text = inputBox.get("1.0", tkinter.END).strip("\n")
    text = text.splitlines()

    matrix = []
    for txt in text:
        try:
            matrix.append(convert_to_integer_list(txt))
        except MatrixException as error:
            error_text = error.message
            break

    if error_text is not None:
        messagebox.showerror(title="Xəta", message=error_text)
        error_text = None
    else:
        matrix = Matrix(matrix=matrix)

        try:
            determinant_of_matrix = matrix.calculate()

            answer_label.config(
                text=f"Girilən matrisin determinantı {determinant_of_matrix}")

        except MatrixException as error:
            error_text = error.message
            messagebox.showerror(title="Xəta", message=error_text)
            error_text = None


def set_text_to_input_text(text: str):
    inputBox.delete("1.0", "end")
    inputBox.insert(INSERT, text)


root = tk.Tk()

root.title("Determinant Kalkulayator")
root.geometry("1360x800")
root.config(background="#FFA07A")

label = tk.Label(root, text="Matrisi daxil edin!", font=('Arial', 20))
label.pack(pady=10)
label.config(background="#FFA07A")

inputBox = tk.Text(root, width=88, height=10, font=(' Arial', 20))
inputBox.pack(pady=10)

calculate_button = tk.Button(root, text="Hesabla", borderwidth=.6, background="#3498db", width=10, height=1,
                             font=('Arial', 20),
                             command=lambda: get_text(), relief="groove")
calculate_button.pack(pady=20)

generate_button = tk.Button(
    root, text="Rastgələ matris generasiya elə", borderwidth=.6, background="#3498db", width=30, height=1,
    font=('Arial', 20),
    command=lambda: set_text_to_input_text(convert_matrix_to_string(generate_matrix())), relief="groove"
)

generate_button.pack(padx=50)

answer_label = tk.Label(root, text="Cavab burada göstəriləcək", font=('Arial', 30))
answer_label.pack(pady=0)
answer_label.config(background="#FFA07A")

tk.mainloop()
