from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QHBoxLayout,QGridLayout
app=QApplication([])
window=QWidget()
window.resize(700,400)
window.setWindowTitle("Grade Calculator")
mainlayout=QVBoxLayout()
title=QLabel("Grade Calculator")
title.setAlignment(Qt.AlignCenter)
mainlayout.addWidget(title)
button1=QPushButton("+ Add Subject")
button2=QPushButton("Calculate GPA")
Layout1=QHBoxLayout()
Layout1.addWidget(button1)
Layout1.addWidget(button2)
subject_name=[]
grades=[]
credits=[]
def add_textbox():
    Layout=QHBoxLayout()
    subject=QLineEdit()  
    subject.setPlaceholderText("Subject Name")
    grade=QLineEdit()
    grade.setPlaceholderText("Grade (0-10)")
    credit=QLineEdit()
    credit.setPlaceholderText("Credits (1-4)")
    subject_name.append(subject)
    grades.append(grade)
    credits.append(credit)
    Layout.addWidget(subject)
    Layout.addWidget(grade)     
    Layout.addWidget(credit)
    mainlayout.addLayout(Layout)
mainlayout.addLayout(Layout1)

  

def clicked():
    total_points=0
    for i in range(len(subject_name)):
            try:
                if(float(grades[i].text())>=0 and float(grades[i].text())<=10 and int(credits[i].text())>0 and int(credits[i].text())<=4):
                    total_points+=float(grades[i].text())*int(credits[i].text())
                    gpa=total_points/sum(int(credits[j].text()) for j in range(len(credits)))
                    
                else:
                    break
            except ValueError:
                print("Invalid input")  

    text=QLabel(f"Your GPA is: {gpa:.2f}")
    text.setAlignment(Qt.AlignCenter)
    mainlayout.addWidget(text)                   
button1.clicked.connect(add_textbox) 
button2.clicked.connect(lambda: clicked())
window.setLayout(mainlayout)
window.show()
app.exec_()