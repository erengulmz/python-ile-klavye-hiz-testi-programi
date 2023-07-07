import tkinter as tk
import random
from datetime import *
random_metin = ["ben klavye hız testi yapıyorum", "klavye parmak hızımı öğrenmeye çalışıyorum","kalvyede hızlı olup olmadığımı öğrenmeye çalışıyorum", "on parmak hızımı bulmaya çalışıyorum","hızlı bir şekilde yazıp yazamadığımı öğreniyorum", "klavyede ne kadar hızlıyım bilmek istiyorum","bu test bana ne kadar hızlı yazdığımı gösterecek","verilen paragrafı ne kadar hızlı yazabilirim"]
metin =(random.choice(random_metin))
before = datetime.now()

# Create the main window
window = tk.Tk()
window.title("Klavye Hız Testi")

# Create a label to display the instructions
instructions_label = tk.Label(text="Aşağıdaki metni olabildiğince hızlı yazın:")
instructions_label.pack()

# Display the random text
random_text_label = tk.Label(text=metin)
random_text_label.pack()

# Create an input field for the user to type in
input_field = tk.Entry()
input_field.pack()

# Create a function to check the user's input
def check_input():
  user_input = input_field.get()
  if user_input == metin:
    # Calculate the speed
    after = datetime.now()
    speed = after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(metin) / seconds, 1)

    # Display the results
    result_label = tk.Label(text="Tebrikler! {} karakterlik metni {} saniyede yazdınız ({} saniyedeki harf sayısı)".format(len(metin), seconds, letter_per_second))
    result_label.pack()
  else:
    result_label = tk.Label(text="Yanlış! Lütfen tekrar deneyin.")
    result_label.pack()

# Create a button to check the user's input
check_button = tk.Button(text="Kontrol Et", command=check_input)
check_button.pack()

# Run the main loop
window.mainloop()