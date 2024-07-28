# first_page.py  
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel  
  
def HomePage():  
    page = QWidget()  
    layout = QVBoxLayout()  
    label = QLabel("首页")  
    layout.addWidget(label)  
    page.setLayout(layout)  
    page.setStyleSheet("background-color: lightgray;")  # 仅为了区分  

    return page