import os
from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory


def input_path():
    target_path = askdirectory()
    lbl_input_path["text"] = target_path

    global pdf_lst
    pdf_lst = sorted(
        [f for f in os.listdir(target_path) if f.endswith('.pdf')])
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    if len(pdf_lst) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"


def output_path():
    global output_path

    output_path = askdirectory()
    lbl_output_path["text"] = output_path


def merge_pdf():
    output_filename = "Untitled.pdf" if not ent_output_name.get() else (
        ent_output_name.get() + ".pdf")

    file_merger = PdfFileMerger(strict=False)

    for pdf in pdf_lst:
        file_merger.append(pdf)  # combine pdf files

    file_merger.write(os.path.join(output_path, output_filename))
    tk.messagebox.showinfo("通知", "已完成")


# Create desktop GUI
window = tk.Tk()
window.title("Merge PDF")
window.geometry("400x400")
# Not able to resize the GUI window
window.resizable(0, 0)

# --- Ask target path ---
fr_bg1 = tk.Frame(window, bd=3)
lbl_input_target = tk.Label(fr_bg1, text="選擇文件夾 (需要有2個或以上的PDF檔案)")
lbl_input_target.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_input_target = tk.Button(fr_bg1, text="瀏覽", command=input_path)

btn_input_target.grid(row=1, column=0, sticky="ew", padx=5)
lbl_input_path = tk.Label(fr_bg1, text="")
lbl_input_path.grid(row=2, column=0, pady=5)
fr_bg1.pack()

# --- Ask output path ---
fr_bg2 = tk.Frame(window, bd=3)
lbl_output_target = tk.Label(fr_bg2, text="選擇合拼檔案輸出位置")
lbl_output_target.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_output_target = tk.Button(fr_bg2, text="瀏覽", command=output_path)

btn_output_target.grid(row=1, column=0, sticky="ew", padx=5)
lbl_output_path = tk.Label(fr_bg2, text="")
lbl_output_path.grid(row=2, column=0, pady=5)
fr_bg2.pack()

# --- Button to merge PDFs ---
fr_bg3 = tk.Frame(window, bd=3)
lbl_to_merge = tk.Label(fr_bg3, text="合拼PDF的文件名稱")
lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

ent_output_name = tk.Entry(master=fr_bg3, width=7)
ent_output_name.grid(row=1, column=0, sticky="ew")

btn_merge = tk.Button(fr_bg3, text="合拼", state="disabled", command=merge_pdf)

btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_bg3.pack()

fr_bg4 = tk.Frame(window, bd=3)
lbl_reminder = tk.Label(
    fr_bg4,
    text="請等待至有pop-up window提示才為成功",
)
lbl_reminder.grid(row=0, column=0, sticky="ew", padx="5", pady="20")
fr_bg4.pack()

# --- Button to exit ---
btn_exit = tk.Button(window, text="離開", command=window.destroy, bd=2)
btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    window.mainloop()
