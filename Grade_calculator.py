from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QHBoxLayout,QGridLayout
def apply_styles(widget):
    widget.setStyleSheet("""
        QWidget{
            background-color: #1B1B38;
            color: white;
            font-family: 'Segoe UI';
            font-size: 16px;
        }
        QLabel {
            font-size: 22px;
            font-weight: bold;
            color: #46B7E3;
        }
        QLineEdit {
            background-color: #2d2d2d;
            border: 2px solid #46B7E3;
            border-radius: 8px;
            padding: 10px;
            color: white;
        }
        QPushButton {
            background-color: #00bfff;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #009acd;
        }
    """)
app=QApplication([])
window=QWidget()
window.resize(700,400)
window.setWindowTitle("Grade Calculator")
mainlayout=QVBoxLayout()
mainlayout.setContentsMargins(20, 20, 20, 20)
mainlayout.setSpacing(14)
title = QLabel("Grade Calculator")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
mainlayout.addWidget(title)

subject_name=[]
grades=[]
credits=[]
def add_textbox():
    subject=QLineEdit()  
    subject.setPlaceholderText("Subject Name")
    grade=QLineEdit()
    grade.setPlaceholderText("Grade (0-10)")
    credit=QLineEdit()
    credit.setPlaceholderText("Credits (1-4)")
    subject_name.append(subject)
    grades.append(grade)
    credits.append(credit)
    Layout=QHBoxLayout()
    Layout1=QHBoxLayout()
    Layout.addWidget(subject)
    Layout.addWidget(grade)     
    Layout.addWidget(credit)
    Layout1.addWidget(button1)
    Layout1.addWidget(button2)
    mainlayout.addLayout(Layout)
    mainlayout.addLayout(Layout1)


  

def clicked():
    total_points=0
    for i in range(len(subject_name)):   
        try:
            if(type(float(grades[i].text()))==float and type(int(credits[i].text()))==int):
                if(float(grades[i].text())>=0 and float(grades[i].text())<=10 and int(credits[i].text())>0 and int(credits[i].text())<=4):
                    total_points+=float(grades[i].text())*int(credits[i].text())
                    gpa=total_points/sum(int(credits[j].text()) for j in range(len(credits)))
                    text=QLabel(f"Your GPA is: {gpa:.2f}")
                    text.setAlignment(Qt.AlignCenter)
                    mainlayout.addWidget(text) 
            else:
                raise ValueError
        except ValueError:
            error=QLabel("Please enter valid inputs for grades (0-10) and credits (1-4).")
            error.setAlignment(Qt.AlignCenter)
            mainlayout.addWidget(error)

# buttons
button1=QPushButton("+ Add Subject")
button2=QPushButton("Calculate GPA")
button2.clicked.connect(lambda: clicked())
button1.clicked.connect(add_textbox) 
if len(subject_name)==0:
    add_textbox()
apply_styles(window)    
window.setLayout(mainlayout)
window.show()
app.exec_()