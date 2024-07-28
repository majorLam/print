from PySide6.QtWidgets import QPushButton,QApplication, QWidget,QHBoxLayout,QVBoxLayout,QStackedWidget
from PySide6.QtCore import QSize
from Home.Home import HomePage

class MyWidow(QWidget):
    def __init__(self):
        super().__init__()
        #主窗口固定大小
        self.setMinimumSize(QSize(800, 500))  
        # self.setMaximumSize(QSize(300, 300))

        self.leftMain()
        self.righttMain()

        # #主窗口布局
        self.MainLayout = QHBoxLayout(self) #水平布局
        self.MainLayout.addWidget(self.leftMainPage,1) 
        self.MainLayout.addWidget(self.righttMainPage,5)


    def leftMain(self):
        #左布局
        self.leftMainPage = QWidget() #创建页面
        leftMainPageLayout = QVBoxLayout(self.leftMainPage) # 左布局为垂直布局
        #左上布局
        self.LeftUpper = QWidget()
        LeftUpperLayout = QVBoxLayout( self.LeftUpper)
        LeftUpperBUtton = [
            QPushButton('首页'),
            QPushButton('第二页')
        ]
        # 遍历列表，将每个按钮添加到左侧布局中
        for button in LeftUpperBUtton:
            LeftUpperLayout.addWidget(button)
        #左下布局
        self.LeftLower = QWidget()
        LeftLowerLayout = QVBoxLayout( self.LeftLower)
        button = QPushButton('设置')
        LeftLowerLayout.addWidget(button)
        # 添加进左布局
        leftMainPageLayout.addWidget(self.LeftUpper)
        leftMainPageLayout.addStretch(1)
        leftMainPageLayout.addWidget(self.LeftLower)


    def righttMain(self):
        #右布局
        self.righttMainPage = QStackedWidget() #创建页面
        #使用单独的函数创建点击页面
        self.HomePage = HomePage()
        #将页面添加到QStackedWidget
        self.righttMainPage.addWidget(self.HomePage)


if __name__=='__main__':
    app = QApplication([])
    window = MyWidow()
    window.show()
    app.exec()