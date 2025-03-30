import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("計算機")
        master.configure(bg="white")
        master.resizable(False, False)
        
        # 創建主框架
        self.main_frame = tk.Frame(master, bg="white")
        self.main_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # 顯示結果的文字框
        self.display = tk.Entry(self.main_frame, width=20, font=('Arial', 16), 
                               justify='right', bd=5, bg="white", fg="black")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # 儲存計算結果
        self.result = ""
        
        # 按鈕佈局
        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]
        
        # 創建按鈕
        for (text, row, col) in button_layout:
            # 使用深灰色作為按鈕背景色
            self.create_button(text, row, col)
        
        # 添加圖片框架
        self.image_frame = tk.Frame(master, bg="white")
        self.image_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # 圖片標籤
        self.image_label = tk.Label(self.image_frame, bg="white")
        self.image_label.pack()
        
        # 直接載入指定圖片
        self.load_image("C:\\Users\\zgmfx\\Downloads\\7123813.jpg")
    
    def select_image(self):
        """打開檔案選擇對話框讓使用者選擇圖片"""
        file_path = filedialog.askopenfilename(
            title="選擇圖片",
            filetypes=[
                ("圖片檔案", "*.png *.jpg *.jpeg *.gif *.bmp *.webp"),
                ("所有檔案", "*.*")
            ]
        )
        
        if file_path:
            self.load_image(file_path)
    
    def load_image(self, image_path):
        """載入並顯示圖片"""
        try:
            # 載入圖片
            original_image = Image.open(image_path)
            
            # 調整圖片大小，保持比例
            width, height = original_image.size
            new_height = 400  # 設定新高度
            new_width = int(width * (new_height / height))
            resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
            
            # 轉換為 Tkinter 可用的格式
            self.tk_image = ImageTk.PhotoImage(resized_image)
            
            # 更新標籤來顯示圖片
            self.image_label.config(image=self.tk_image)
            
        except Exception as e:
            messagebox.showerror("錯誤", f"無法載入圖片: {e}")
    
    def create_button(self, text, row, col):
        # 設定按鈕顏色
        # bg="#0668E1" 設定按鈕背景顏色為藍色
        # fg="white" 設定按鈕文字顏色為白色
        button = tk.Button(self.main_frame, text=text, width=5, height=2, 
                          font=('Arial', 40), bg="#0668E1", fg="white",
                          command=lambda t=text: self.button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    def button_click(self, text):
        if text == '=':
            try:
                # 計算結果
                self.result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.result)
            except Exception as e:
                messagebox.showerror("錯誤", "計算錯誤！")
                self.display.delete(0, tk.END)
        elif text == 'C':
            # 清除所有
            self.display.delete(0, tk.END)
        elif text == 'CE':
            # 清除最後一個字符
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current[:-1])
        else:
            # 添加按鈕文字到顯示框
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current + text)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
