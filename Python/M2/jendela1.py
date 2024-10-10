import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[(sg.Text("SELAMAT DATANG DI KELAS", font=("Arial", 25, "italic","bold","underline")))],
                            [sg.Text("NPM:      2210010200")],
                            [sg.Text("Nama:     Gadsa Khalimatus Sadiah")],
                            [sg.Text("Kelas:    5P Regular Banjarmasin")], 
                            [sg.Text("Matkul:   Pemrograman Visual 2")]],
                            size=(500,200),
                            font=("Times", 18))
window()
window.close()