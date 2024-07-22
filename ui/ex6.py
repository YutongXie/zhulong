import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Window, Style
from ttkbootstrap.style import Bootstyle
from ttkbootstrap.widgets import Button
from ttkbootstrap.constants import *
import ttkcreator as ttc

def on_search():
    # 这里模拟查询操作，实际中应根据用户输入进行查询
    result_area.delete('1.0', tk.END)
    result_area.insert(tk.END, "查询结果将显示在这里...\n")

def on_select_question(event):
    # 模拟选中常用问题列表中的一项
    print(f"选中了问题: {event.widget.cget('text')}")


# app = ttk.Window('Desktop 应用', theme='superhero')
# app = ttk.Window('Desktop 应用')
app = ttk.Window(themename='superhero')
app.geometry('800x600')

# 样式设置（如果需要的话，这里可以配置其他控件的样式）
# style = Style(app)

# 布局
main_frame = tk.Frame(app)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# 上部分：问题输入和查询按钮
input_frame = tk.Frame(main_frame)
input_frame.pack(fill=X, expand=True, pady=5)

question_entry = tk.Text(input_frame, height=5, wrap=tk.WORD)
question_entry.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

search_button = Button(input_frame, text=">>", command=on_search, bootstyle="info")
search_button.pack(side=RIGHT, padx=5, pady=5)

# 下部分：分为左右两部分
lower_frame = tk.Frame(main_frame)
lower_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# 左侧：滚动文本区域显示答案
left_frame = tk.LabelFrame(lower_frame, text="答案区域")
left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

scroll_y = tk.Scrollbar(left_frame, orient=VERTICAL)
result_area = tk.Text(left_frame, wrap=tk.WORD, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
result_area.pack(side=LEFT, fill=BOTH, expand=True)
scroll_y.config(command=result_area.yview)

# 右侧：常用问题列表（这里使用Listbox作为示例）
right_frame = tk.LabelFrame(lower_frame, text="常用问题")
# right_frame.pack(side=RIGHT, fill=Y, expand=False, padx=5, pady=5, width=200)
right_frame.pack(side=RIGHT, fill=Y, expand=False, padx=5, pady=5)

# 示例：添加一些常用问题到Listbox
question_list = tk.Listbox(right_frame, selectmode=SINGLE, exportselection=False)
for question in ["问题1", "问题2", "问题3"]:
    question_list.insert(tk.END, question)
question_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

# 为Listbox添加点击事件监听器
question_list.bind("<<ListboxSelect>>", on_select_question)

app.mainloop()
