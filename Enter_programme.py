# подключаем блок работы с файлами
import json
import Main
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

Faculties = ["Биолого-почвенный", "Географический", "Геологический", "Исторический",
"Подготовительный для иностранных граждан", "Сибирско-американский", "Бизнеса и менеджмента",
"Бизнес-коммуникаций и информатики", "Психологии", "Физический", "Химический"]

Specs = {'Биолого-почвенный': ["Экология и природопользование", "Биология", "Почвоведение", "Биоинженерия и биоинформатика", "Экология и природопользование", "Биология", "Почвоведение"],
'Географический': ["География", "Гидрометеорология", "Экология и природопользование", "Гидрометеорология", "Экология и природопользование"],
"Геологический": ["Геология"],
"Исторический":["История", "Международные отношения", "Политология", "Культурология","Музеология и охрана объектов культурного и природного наследия", "Теология", "Философия"],
"Подготовительный для иностранных граждан":["-"],
"Сибирско-американский":["Менеджмент"],
"Бизнеса и менеджмента":["Стратегический менеджмент", "Oбщий и операционный менеджмент", "Финансовое управление компанией", "Маркетинг для малого и среднего бизнеса", "Управление качеством", "Управление персоналом", "Управление проектами", "Логистика", "Профессиональное командообразование"],
"Бизнес-коммуникаций и информатики":["Прикладная информатика", "Управление персоналом", "Реклама и связи с общественностью", "Сервис", "Туризм"],
"Психологии": ["Психология", "Психолого-педагогическое образование"],
"Физический":["Физика", "Радиофизика", "Информационная безопасность", " Электроника и наноэлектроника", " Педагогическое образование"],
"Химический":["Химия"]}

#Данные для ввода
comission = [] #массив членов ГЭК (ФИО)
P = [] #Председатель ГЭК
S = [] #Секретарь ГЭК
Order = [] #Номер приказа, учреждающего комиссию
Order_Date = [] #Число, месяц и год Приказа


Number = 0 #Номер протокола, увеличивается на 1 при создании нового
Date = [] #Число, месяц и год
Theme = [] #Тема
Student_RP = [] #ФИО студента в Родительном падеже
Student_DP = [] #ФИО студента в Дательном падеже
Faculty = [] #Факультет
Spec = []#Специальность
Form = [] #Форма обучения (очная, очно-заочная, заочная)
Head = [] #Руководитель
Cons = [] #Консультант - не обязательно
Video = [] #Наличие или отсутствие демовидео

Implant = [] #Акт о внедрении, одна из трех позиций

Questions = [] #Вопросы выступающему, могут быть заполнены не все
Answer = [] #Хар-ка ответов - номер выбранной позиции по каждому критерию приложения 1
Creative = [] # проявление творчества
Demonstration = []   # проф язык

ComOp1 = [0 for j in range(4)] #Мнение комиссии - номер выбранной позиции по каждому критерию приложения 2
ComOp2 = [0 for j in range(2)]
ComOp3 = [0 for j in range(3)]
ComOp4 = [0 for j in range(2)]
ComOp5 = []
ComOp6 = [0 for j in range(2)]
ComOp7 = [0 for j in range(2)]
ComOp8 = [0 for j in range(2)]
ComOp9 = [0 for j in range(2)]
ComOp9_1 = [0 for j in range(3)]
ComOp10 = []
ComOp11 = []
ComOp12 = [0 for j in range(12)]
ComOp12_1 = [] #Строка для вписывания графы "Другое"
ComOp13 = [0 for j in range(3)]
Lack = [0 for j in range(7)] #Недочеты - приложение 3
Lack_1 = [] #Строка для вписывания графы "Другое"

Mark = [] #Оценка
Qualif = [] #Присвоенная квалификация (номер)


Yes = [] #За
No = [] #Против
Abstained = [] #Воздержались

def btn_click_comission(): #Получаем в память членов комиссии
    P.append(Predsed.get())
    S.append(Sec.get())
    Order.append(OrderField.get())
    Order_Date.append(Order_DateField.get())
    messagebox.showinfo(title='Успешно', message='Состав комиссии сохранен')

def next_frame(): #Листает на фрейм 2
    Date.append(DateField.get())
    Theme.append(ThemeField.get())
    Student_RP.append(Student_RPField.get())
    Student_DP.append(Student_DPField.get())
    Faculty.append(FacultyField.get())
    Spec.append(SpecField.get())
    Form.append(FormField.get())
    Head.append(HeadField.get())
    Cons.append(ConsField.get())
    Video.append(Video_Var.get())
    Implant.append(Imp_var.get())
    frame1.place_forget()
    frame0.place_forget()
    frame3.place_forget()
    frame2.place(relwidth=1, relheight=1)

def next_frame2():
    Answer.append(Answer_var.get())
    Demonstration.append(Demonstration_var.get())
    Creative.append(Creative_var.get())
    for i in range(4):
        ComOp1[i] = ComOp1Var[i].get()
    for i in range(2):
        ComOp2[i] = ComOp2Var[i].get()
    frame2.place_forget()
    frame4.place_forget()
    frame3.place(relwidth=1, relheight=1)


def next_frame3():
    for i in range(3):
        ComOp3[i] = ComOp3Var[i].get()
    for i in range(2):
        ComOp4[i] = ComOp4Var[i].get()
    ComOp5.append(ComOp5Var.get())
    for i in range(2):
        ComOp6[i] = ComOp6Var[i].get()
    for i in range(2):
        ComOp7[i] = ComOp7Var[i].get()
    ComOp8[0] = ComOp8Var[0].get()
    frame3.place_forget()
    frame5.place_forget()
    frame4.place(relwidth=1, relheight=1)

def next_frame4():
    ComOp8[1] = ComOp8Var[1].get()
    for i in range(2):
        ComOp9[i] = ComOp9Var[i].get()
    ComOp10.append(ComOp10Var.get())
    ComOp11.append(ComOp11Var.get())
    for i in range(12):
        ComOp12[i] = ComOp12Var[i].get()
    for i in range(3):
        ComOp13[i] = ComOp13Var[i].get()
    for i in range(7):
        Lack[i] = LackField[i].get()
    Lack_1.append(Lack_1Field.get())
    frame4.place_forget()
    frame5.place(relwidth=1, relheight=1)
    
def new_member():
    member = comName.get()
    comission.append(member)
    ActualMembers['text'] = ActualMembers['text'] + '\n' + comission[-1]
    comName.delete(0, END)

def delete_member():
    comission = []
    ActualMembers['text'] = ''

def new_question():
    question = QuestionsField.get()
    Questions.append(question)
    ActualQuestions['text'] = ActualQuestions['text'] + '\n' + Questions[-1]
    QuestionsField.delete(0, END)

def delete_question():
    Questions = []
    ActualQuestions['text'] = ''

def new_add():
    add = AddField.get()
    ComOp12_1.append(add)
    ActualAdd['text'] = ActualAdd['text'] + '\n' + ComOp12_1[-1]
    AddField.delete(0, END)

def delete_add():
    ComOp12_1 = []
    ActualAdd['text'] = ''
    
def on_change_selection(event):
    SpecField['values'] = Specs[Faculty_var.get()]

def save_all():
    Mark.append(MarkField.get())
    Qualif.append(QualifField.get())
    Yes.append(YesField.get())
    No.append(NoField.get())
    Abstained.append(AbstainedField.get())
    global Number
    Number += 1
    print(Number)

                # Работы с файлами
    # достаём JSON
    with open('JSON_text.json', 'r', encoding='utf-8') as f:
        date = json.load(f)

    # проверка формата введения года
    if len(Date[-1].split()[0]) <= 2:     year = "20" + Date[-1].split()[2]
    else:   year = Date[-1].split()[2]


    # проверка наличия демонстрационного видео
    video = ""
    if Video: video = date["video"]


    # формирование вопросов
    questions = ""
    for x, text in enumerate(Questions):
        questions += str(x+1) + ". " + text + '\n'

    # проверка дополнительного пункта при ответах на вопросы
    creative = ""
    if Creative:
        creative = date["creative"]

    # print(ComOp1, ComOp2, ComOp3, ComOp4)

    # формируем мнение комиссии
    opinion = ""
    opinion += date["opinion"]["0"][ComOp1[0]]
    opinion += date["opinion"]["1"][ComOp1[1]]
    opinion += date["opinion"]["2"][ComOp1[2]]
    opinion += date["opinion"]["3"][ComOp1[3]]
    opinion += date["opinion"]["4"][ComOp2[0]]
    opinion += date["opinion"]["5"][ComOp2[1]]
    opinion += date["opinion"]["6"][ComOp3[0]]
    opinion += date["opinion"]["7"][ComOp3[1]]
    opinion += date["opinion"]["8"][ComOp3[2]]
    opinion += date["opinion"]["9"][ComOp4[0]]
    opinion += date["opinion"]["10"][ComOp4[1]]
    opinion += date["opinion"]["11"][ComOp5[0]]
    opinion += date["opinion"]["12"][ComOp6[0]]
    if ComOp6[1]: opinion += date["opinion"]["13"]

    opinion += date["opinion"]["14"][ComOp7[0]]
    opinion += date["opinion"]["15"][ComOp7[1]]
    opinion += date["opinion"]["16"][ComOp8[0]]
    opinion += date["opinion"]["17"][ComOp8[1]]
    opinion += date["opinion"]["18"][ComOp9[0]]
    opinion += date["opinion"]["19"][ComOp9[1]]
    if ComOp9_1[0]: opinion += date["opinion"]["20"]
    if ComOp9_1[1]: opinion += date["opinion"]["21"]
    if ComOp9_1[2]: opinion += date["opinion"]["22"]
    opinion += date["opinion"]["23"][ComOp10[0]]
    opinion += date["opinion"]["24"][ComOp11[0]]

    if ComOp12[0]: opinion += date["opinion"]["25"]
    if ComOp12[1]: opinion += date["opinion"]["26"]
    if ComOp12[2]: opinion += date["opinion"]["27"]
    if ComOp12[3]: opinion += date["opinion"]["28"]
    if ComOp12[4]: opinion += date["opinion"]["29"]
    if ComOp12[5]: opinion += date["opinion"]["30"]
    if ComOp12[6]: opinion += date["opinion"]["31"]
    if ComOp12[7]: opinion += date["opinion"]["32"]
    if ComOp12[8]: opinion += date["opinion"]["33"]
    if ComOp12[9]: opinion += date["opinion"]["34"]
    if ComOp12[10]: opinion += date["opinion"]["35"]
    if ComOp12[11]: opinion += date["opinion"]["36"]

    for text in ComOp12_1: opinion += text

    if ComOp13[0]: opinion += date["opinion"]["37"]
    if ComOp13[1]: opinion += date["opinion"]["38"]
    if ComOp13[2]: opinion += date["opinion"]["39"]


    # формируем мнение о недостатках работы
    disadvantages = ""
    if Lack[0]: disadvantages += date["opinion"]["40"]
    if Lack[1]: disadvantages += date["opinion"]["41"]
    if Lack[2]: disadvantages += date["opinion"]["42"]
    if Lack[3]: disadvantages += date["opinion"]["43"]
    if Lack[4]: disadvantages += date["opinion"]["44"]
    if Lack[5]: disadvantages += date["opinion"]["45"]
    if Lack[6]: disadvantages += date["opinion"]["46"]

    for text in Lack_1: disadvantages += text



    # тэги и соответствующие им данные
    tags = [
        ["${Study_format}", Form[-1]],
        ["${Specialization}", Spec[-1]],
        ["${Faculty}", Faculty[-1]],
        ["${Number}", str(Number)],
        ["${Day}", Date[-1].split()[0]],
        ["${Month}", Date[-1].split()[1]],
        ["${Year}", year],
        ["${Student_RP}", Student_RP[-1]],
        ["${Theam}", Theme[-1]],

        ["${Order_Date}", Order_Date[-1]],
        ["${Order}", Order[-1]],
        ["${Video}", video],
        ["${Implant}", date["Implant"][Implant[-1]]],
        ["${Questions}", questions],
        ["${Answer}", date["Answer"][Answer[-1]]],
        ["${Demonstration}", date["Demonstration"][Demonstration[-1]]],
        ["${Creative}", creative],

        ["${Сommission_opinion}", opinion],

        ["${disadvantages}", disadvantages],

        ["${Mark}", Mark[-1]],
        ["${Student_DP}", Student_DP[-1]],
        ["${Qualification}", Qualif[-1]],
        ["${Yes}", Yes[-1]],
        ["${No}", No[-1]],
        ["${Abstained}", Abstained[-1]],
        ["${Chairman}", P[-1]],
        ["${Secretary}", S[-1]]
    ]

    if Cons:
        # таблица, с консультантом
        table_tags = [
            P[-1],  # председатель
            comission,  # комиссия
            Head[-1],  # руководитель
            Cons[-1]]  # консультант
    else:
        # таблица, без консультанта
        table_tags = [
            P[-1],  # председатель
            comission,  # комиссия
            Head[-1]]  # руководитель


    # запуск блока формирующего протоколы
    Main.Create_reports(0, tags, table_tags)
    messagebox.showinfo(title='Успешно', message='Протокол сохранен')
    
def open_first():
    frame2.place_forget()
    frame5.place_forget()
    Number = 0 
    Date = [] 
    Theme = [] 
    Student_RP = [] 
    Student_DP = [] 
    Faculty = [] 
    Spec = []
    Form = [] 
    Head = [] 
    Cons = [] 
    Video =[]
    Implant = []
    Questions = [] 
    Answer = [] 
    Demonstration = []  
    Creative = []
    ComOp1 = [0 for j in range(4)]
    ComOp2 = [0 for j in range(2)]
    ComOp3 = [0 for j in range(3)]
    ComOp4 = [0 for j in range(2)]
    ComOp5 = 0
    ComOp6 = [0 for j in range(2)]
    ComOp7 = [0 for j in range(2)]
    ComOp8 = [0 for j in range(2)]
    ComOp9 = [0 for j in range(2)]
    ComOp9_1 = [0 for j in range(3)]
    ComOp10 = []
    ComOp11 = []
    ComOp12 = [0 for j in range(13)]
    ComOp12_1 = [] 
    ComOp13 = [0 for j in range(3)]
    Lack = [0 for j in range(7)] 
    Lack_1 = [] 
    Mark = []
    Qualif = [] 
    Yes = []
    No = [] 
    Abstained = [] 
    frame0.place(relwidth=0.3, relheight=1)
    frame1.place(relwidth=0.7, relheight=1, relx = 0.3)

with open('JSON_text.json', 'r', encoding='utf-8') as f:
    date = json.load(f)

root.title('Ввод протоколов')
root.state('zoomed')

frame0 = Frame(root, bg="#F7D6BB")
frame0.place(relwidth=0.3, relheight=1)

title = Label(frame0, text='Данные комиссии', font='Courier 20 bold', bg="#F7D6BB")
title.place(x=20, y = 20)

Text1 = Label(frame0, text = "Члены ГЭК:", font='Courier 16', bg='#F7D6BB')
Text1.place(x=20, y=60)
comName = Entry(frame0, bg = 'white', width=35, font='Courier 12')
comName.place(x=20, y = 105)

NewMember = Button(frame0, text='Добавить', bg = 'grey',font='Courier 12 bold', command=new_member)
NewMember.place(x=100, y = 140)

DeleteMember = Button(frame0, text='Очистить', bg = 'grey',font='Courier 12 bold', command=delete_member)
DeleteMember.place(x=200, y = 140)

ActualMembers = Label(frame0, text = "", font='Courier 12', bg="#F7D6BB", justify=tkinter.LEFT)
ActualMembers.place(x=20, y=172)
    
R_label = Label(frame0, text = "Председатель:", font='Courier 15', bg="#F7D6BB")
R_label.place(x=20, y = 380)
Predsed = Entry(frame0, bg = 'white', width=35, font='Courier 12')
Predsed.place(x=20, y = 410)

S_label = Label(frame0, text = "Секретарь:", font='Courier 15', bg="#F7D6BB")
S_label.place(x=20, y = 440)
Sec = Entry(frame0, bg = 'white', width=35, font='Courier 12')
Sec.place(x=20, y = 470)

OrderLabel = Label(frame0, text = "Приказ No", font='Courier 15', bg="#F7D6BB")
OrderLabel.place(x=20, y = 500)
OrderField = Entry(frame0, bg = 'white', width=10, font='Courier 12')
OrderField.place(x=140, y = 505)

Order_DateLabel = Label(frame0, text = "от", font='Courier 15', bg="#F7D6BB")
Order_DateLabel.place(x=260, y = 500)
Order_DateField = Entry(frame0, bg = 'white', width=10, font='Courier 12')
Order_DateField.place(x=300, y = 505)

Save_comission = Button(frame0, text='Сохранить', bg = 'grey',font='Courier 12 bold', command=btn_click_comission)
Save_comission.place(relx=0.5, y = 565)

#Данные студента
frame1 = Frame(root, bg="#FDE6D5")
frame1.place(relwidth=0.7, relheight=1, relx = 0.3)

title = Label(frame1, text='Данные работы', font='Courier 20 bold', bg="#FDE6D5")
title.place(x=20, y = 20)

DateLabel = Label(frame1, text = "Дата (чч мм гг)", font='Courier 15', bg="#FDE6D5")
DateLabel.place(x=20, y = 60)
DateField = Entry(frame1, bg = 'white', width=10, font='Courier 12')
DateField.place(x=210, y = 65)

ThemeLabel = Label(frame1, text = "Тема", font='Courier 15', bg="#FDE6D5")
ThemeLabel.place(x=20, y = 90)
ThemeField = Entry(frame1, bg = 'white', width=40, font='Courier 12')
ThemeField.place(x=100, y = 95)

Student_RPLabel = Label(frame1, text = "ФИО студента(в род.п.)", font='Courier 15', bg="#FDE6D5")
Student_RPLabel.place(x=20, y = 125)
Student_RPField = Entry(frame1, bg = 'white', width=56, font='Courier 12')
Student_RPField.place(x=20, y = 150)

Student_DPLabel = Label(frame1, text = "ФИО студента(в дат.п.)", font='Courier 15', bg="#FDE6D5")
Student_DPLabel.place(x=20, y = 180)
Student_DPField = Entry(frame1, bg = 'white', width=56, font='Courier 12')
Student_DPField.place(x=20, y = 205)

FacultyLabel = Label(frame1, text = "Факультет", font='Courier 15', bg="#FDE6D5")
FacultyLabel.place(x=650, y = 125)
Faculty_var = StringVar()
FacultyField = ttk.Combobox(frame1, textvariable = Faculty_var, font='Courier 12', width = 35)
FacultyField['values'] = Faculties
FacultyField.set("Биолого-почвенный")
FacultyField.bind("<<ComboboxSelected>>", on_change_selection)
FacultyField.place(x = 650, y = 150)

SpecLabel = Label(frame1, text = "Направление", font='Courier 15', bg="#FDE6D5")
SpecLabel.place(x=650, y = 180)
Spec_var = StringVar()
SpecField = ttk.Combobox(frame1, textvariable = Spec_var, font='Courier 12', width = 35)
SpecField['values'] = Specs[Faculty_var.get()]
SpecField.place(x = 650, y = 205)

FormLabel = Label(frame1, text = "Форма обучения", font='Courier 15', bg="#FDE6D5")
FormLabel.place(x=650, y = 235)
Form_var = StringVar()
FormField = ttk.Combobox(frame1, textvariable = Form_var, font='Courier 12', width = 35)
FormField['values'] = ['Очная', 'Очно-Заочная', 'Заочная']
FormField.place(x = 650, y = 260)

HeadLabel = Label(frame1, text = "Руководитель", font='Courier 15', bg="#FDE6D5")
HeadLabel.place(x=20, y = 235)
HeadField = Entry(frame1, bg = 'white', width=56, font='Courier 12')
HeadField.place(x=20, y = 260)

ConsLabel = Label(frame1, text = "Консультант", font='Courier 15', bg="#FDE6D5")
ConsLabel.place(x=20, y = 290)
ConsField = Entry(frame1, bg = 'white', width=56, font='Courier 12')
ConsField.place(x=20, y = 315)

Text3 = Label(frame1, text = "В работе присутствуют: ", font='Courier 15', bg="#FDE6D5")
Text3.place(x=20, y = 385)

Video_Var = BooleanVar()
VideoField = Checkbutton(frame1, text='Видео', variable=Video_Var, onvalue=1, offvalue=0, font='Courier 15', bg = '#FDE6D5')
VideoField.place(x=20, y = 425)

Imp_var = IntVar()
Imp_var.set(0)
r1 = Radiobutton(frame1, text='Акт о внедрении результатов', variable=Imp_var, value=0, font='Courier 15', bg = '#FDE6D5',)
r2 = Radiobutton(frame1, text='Акт о намерении внедрения результатов', variable=Imp_var, value=1, font='Courier 15', bg = '#FDE6D5',)
r3 = Radiobutton(frame1, text='-', variable=Imp_var, value=2, font='Courier 15', bg = '#FDE6D5',)
r1.place(x=20, y = 470)
r2.place(x=20, y = 500)
r3.place(x=20, y = 530)

Next = Button(frame1, text='  Далее  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame)
Next.place(x=845, y = 740)

#Вопросы и ответы
frame2 = Frame(root, bg="#FDE6D5")

Text2 = Label(frame2, text = "Вопросы комиссии", font='Courier 20 bold', bg='#FDE6D5')
Text2.place(x=20, y = 20)

QuestionsField = Entry(frame2, bg = 'white', width=35, font='Courier 12')
QuestionsField.place(x=20, y = 80)

NewQuestion = Button(frame2, text='Добавить', bg = 'grey',font='Courier 12 bold', command=new_question)
NewQuestion.place(x=100, y = 110)

DeleteQuestion = Button(frame2, text='Очистить', bg = 'grey',font='Courier 12 bold', command=delete_question)
DeleteQuestion.place(x=200, y = 110)

ActualQuestions = Label(frame2, text = "", font='Courier 12 bold', bg='#FDE6D5', wraplength=480, justify=tkinter.LEFT)
ActualQuestions.place(x=20, y = 150)

Text4 = Label(frame2, text = "Характеристика ответов", font='Courier 20 bold', bg='#FDE6D5')
Text4.place(x=20, y = 420)

Answer_var = BooleanVar()
A1 = Radiobutton(frame2, text=date["Answer"][0], variable=Answer_var, value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
A2 = Radiobutton(frame2, text=date["Answer"][1], variable=Answer_var, value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
A3 = Radiobutton(frame2, text=date["Answer"][2], variable=Answer_var, value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
A4 = Radiobutton(frame2, text=date["Answer"][3], variable=Answer_var, value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
A5 = Radiobutton(frame2, text=date["Answer"][4], variable=Answer_var, value=4, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
A1.place(x=20, y = 480)
A2.place(x=20, y = 520)
A3.place(x=20, y = 560)
A4.place(x=20, y = 600)
A5.place(x=20, y = 640)

Creative_var = BooleanVar()
CreativeField = Checkbutton(frame2, text='Проявляет творческие способности в понимании\n и изложении ответов на вопросы.',variable = Creative_var, onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CreativeField.place(x=20, y = 720)

Demonstration_var = BooleanVar()
Demonstration_var.set(0)
B1 = Radiobutton(frame2, text=date["Demonstration"][0], variable=Demonstration_var, value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
B2 = Radiobutton(frame2, text=date["Demonstration"][1], variable=Demonstration_var, value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
B3 = Radiobutton(frame2, text=date["Demonstration"][2], variable=Demonstration_var, value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
B4 = Radiobutton(frame2, text=date["Demonstration"][3], variable=Demonstration_var, value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
B1.place(x=530, y = 20)
B2.place(x=530, y = 60)
B3.place(x=530, y = 100)
B4.place(x=530, y = 160)

Text5 = Label(frame2, text = "Мнение комиссии", font='Courier 20 bold', bg='#FDE6D5')
Text5.place(x=530, y = 220)

ComOp1Label = Label(frame2, text = "Актуальность", font='Courier 15 bold', bg='#FDE6D5')
ComOp1Label.place(x=530, y = 260)

ComOp1Var = [IntVar() for j in range(4)]

CO111 = Radiobutton(frame2, text=date["opinion"]["0"][0], variable=ComOp1Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO112 = Radiobutton(frame2, text=date["opinion"]["0"][1], variable=ComOp1Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO113 = Radiobutton(frame2, text=date["opinion"]["0"][2], variable=ComOp1Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO114 = Radiobutton(frame2, text=date["opinion"]["0"][3], variable=ComOp1Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO111.place(x=530, y = 290)
CO112.place(x=530, y = 330)
CO113.place(x=530, y = 360)
CO114.place(x=530, y = 380)

CO12 = Checkbutton(frame2, text=date["opinion"]["1"][1],variable = ComOp1Var[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CO12.place(x=530, y = 450)

CO131 = Radiobutton(frame2, text=date["opinion"]["2"][0], variable=ComOp1Var[2], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO132 = Radiobutton(frame2, text=date["opinion"]["2"][1], variable=ComOp1Var[2], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO133 = Radiobutton(frame2, text=date["opinion"]["2"][2], variable=ComOp1Var[2], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO131.place(x=530, y = 480)
CO132.place(x=530, y = 515)
CO133.place(x=530, y = 570)

CO141 = Radiobutton(frame2, text=date["opinion"]["3"][0], variable=ComOp1Var[3], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO142 = Radiobutton(frame2, text=date["opinion"]["3"][1], variable=ComOp1Var[3], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO143 = Radiobutton(frame2, text=date["opinion"]["3"][2], variable=ComOp1Var[3], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO144 = Radiobutton(frame2, text=date["opinion"]["3"][3], variable=ComOp1Var[3], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO141.place(x=530, y = 630)
CO142.place(x=530, y = 670)
CO143.place(x=530, y = 710)
CO144.place(x=530, y = 750)

ComOp2Label = Label(frame2, text = "Раскрытие темы ВКР", font='Courier 15 bold', bg='#FDE6D5')
ComOp2Label.place(x=1100, y = 20)

ComOp2Var = [IntVar() for j in range(2)]

CO211 = Radiobutton(frame2, text=date["opinion"]["4"][0], variable=ComOp2Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO212 = Radiobutton(frame2, text=date["opinion"]["4"][1], variable=ComOp2Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO213 = Radiobutton(frame2, text=date["opinion"]["4"][2], variable=ComOp2Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO214 = Radiobutton(frame2, text=date["opinion"]["4"][3], variable=ComOp2Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO211.place(x=1100, y = 50)
CO212.place(x=1100, y = 120)
CO213.place(x=1100, y = 190)
CO214.place(x=1100, y = 270)

CO221 = Radiobutton(frame2, text=date["opinion"]["5"][0], variable=ComOp2Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO222 = Radiobutton(frame2, text=date["opinion"]["5"][1], variable=ComOp2Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO223 = Radiobutton(frame2, text=date["opinion"]["5"][2], variable=ComOp2Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO224 = Radiobutton(frame2, text=date["opinion"]["5"][3], variable=ComOp2Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO221.place(x=1100, y = 360)
CO222.place(x=1100, y = 385)
CO223.place(x=1100, y = 410)
CO224.place(x=1100, y = 435)

Next2 = Button(frame2, text='  Далее  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame2)
Next2.place(x=1300, y = 740)

Back = Button(frame2, text='  Назад  ', bg = 'lightgrey',font='Courier 12 bold', command=open_first)
Back.place(x=1180, y =740)

#Вторая страница информации

frame3 = Frame(root, bg="#FDE6D5")

ComOp3Var = [IntVar() for j in range(3)]

Text6 = Label(frame3, text = "Уровень теоретической\n проработки проблемы", font='Courier 15 bold', bg='#FDE6D5')
Text6.place(x=20, y = 20)

CO311 = Radiobutton(frame3, text=date["opinion"]["6"][0], variable=ComOp3Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO312 = Radiobutton(frame3, text=date["opinion"]["6"][1], variable=ComOp3Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO313 = Radiobutton(frame3, text=date["opinion"]["6"][2], variable=ComOp3Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO314 = Radiobutton(frame3, text=date["opinion"]["6"][3], variable=ComOp3Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO311.place(x=20, y = 80)
CO312.place(x=20, y = 140)
CO313.place(x=20, y = 180)
CO314.place(x=20, y = 235)

CO321 = Radiobutton(frame3, text=date["opinion"]["7"][0], variable=ComOp3Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO322 = Radiobutton(frame3, text=date["opinion"]["7"][1], variable=ComOp3Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO323 = Radiobutton(frame3, text=date["opinion"]["7"][2], variable=ComOp3Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO324 = Radiobutton(frame3, text=date["opinion"]["7"][3], variable=ComOp3Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO321.place(x=20, y = 310)
CO322.place(x=20, y = 335)
CO323.place(x=20, y = 360)
CO324.place(x=20, y = 385)

CO331 = Radiobutton(frame3, text=date["opinion"]["8"][0], variable=ComOp3Var[2], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO332 = Radiobutton(frame3, text=date["opinion"]["8"][1], variable=ComOp3Var[2], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO333 = Radiobutton(frame3, text=date["opinion"]["8"][2], variable=ComOp3Var[2], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO334 = Radiobutton(frame3, text=date["opinion"]["8"][3], variable=ComOp3Var[2], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO331.place(x=20, y = 420)
CO332.place(x=20, y = 460)
CO333.place(x=20, y = 480)
CO334.place(x=20, y = 520)

ComOp4Var = [IntVar() for j in range(2)]

Text7 = Label(frame3, text = "Качество анализа проблемы, достоверность\n выводов и обоснованность выдвигаемых\n проектных решений", font='Courier 15 bold', bg='#FDE6D5')
Text7.place(x=20, y = 560)

CO411 = Radiobutton(frame3, text=date["opinion"]["9"][0], variable=ComOp4Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO412 = Radiobutton(frame3, text=date["opinion"]["9"][1], variable=ComOp4Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO413 = Radiobutton(frame3, text=date["opinion"]["9"][2], variable=ComOp4Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO414 = Radiobutton(frame3, text=date["opinion"]["9"][3], variable=ComOp4Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO411.place(x=20, y = 630)
CO412.place(x=20, y = 670)
CO413.place(x=20, y = 690)
CO414.place(x=20, y = 760)

CO421 = Radiobutton(frame3, text=date["opinion"]["10"][0], variable=ComOp4Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO422 = Radiobutton(frame3, text=date["opinion"]["10"][1], variable=ComOp4Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO423 = Radiobutton(frame3, text=date["opinion"]["10"][2], variable=ComOp4Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO424 = Radiobutton(frame3, text=date["opinion"]["10"][3], variable=ComOp4Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO421.place(x=530, y = 30)
CO422.place(x=530, y = 80)
CO423.place(x=530, y = 135)
CO424.place(x=530, y = 160)

ComOp5Var = IntVar()

Text8 = Label(frame3, text = "Апробация и внедрение результатов\n в практическую деятельность", font='Courier 15 bold', bg='#FDE6D5')
Text8.place(x=530, y = 230)

CO511 = Radiobutton(frame3, text=date["opinion"]["11"][0], variable=ComOp5Var, value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO512 = Radiobutton(frame3, text=date["opinion"]["11"][1], variable=ComOp5Var, value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO513 = Radiobutton(frame3, text=date["opinion"]["11"][2], variable=ComOp5Var, value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO514 = Radiobutton(frame3, text=date["opinion"]["11"][3], variable=ComOp5Var, value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO511.place(x=530, y = 290)
CO512.place(x=530, y = 335)
CO513.place(x=530, y = 390)
CO514.place(x=530, y = 430)

ComOp6Var = [IntVar() for j in range(2)]

Text9 = Label(frame3, text = "Самостоятельность и творческий подход\n к разработке темы", font='Courier 15 bold', bg='#FDE6D5')
Text9.place(x=530, y = 490)

CO611 = Radiobutton(frame3, text=date["opinion"]["12"][0], variable=ComOp6Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO612 = Radiobutton(frame3, text=date["opinion"]["12"][1], variable=ComOp6Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO613 = Radiobutton(frame3, text=date["opinion"]["12"][2], variable=ComOp6Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO614 = Radiobutton(frame3, text=date["opinion"]["12"][3], variable=ComOp6Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO611.place(x=530, y = 520)
CO612.place(x=530, y = 560)
CO613.place(x=530, y = 600)
CO614.place(x=530, y = 640)

CO621 = Checkbutton(frame3, text=date["opinion"]["13"],variable = ComOp6Var[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CO621.place(x=530, y = 690)

ComOp7Var = [IntVar() for j in range(2)]

Text10 = Label(frame3, text = "Грамотность написания и оформления\n работы, его соответствие\n установленным стандартам", font='Courier 15 bold', bg='#FDE6D5')
Text10.place(x=1100, y = 40)

CO711 = Radiobutton(frame3, text=date["opinion"]["14"][0], variable=ComOp7Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO712 = Radiobutton(frame3, text=date["opinion"]["14"][1], variable=ComOp7Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO713 = Radiobutton(frame3, text=date["opinion"]["14"][2], variable=ComOp7Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO714 = Radiobutton(frame3, text=date["opinion"]["14"][3], variable=ComOp7Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO711.place(x=1100, y = 140)
CO712.place(x=1100, y = 180)
CO713.place(x=1100, y = 230)
CO714.place(x=1100, y = 270)

CO721 = Radiobutton(frame3, text=date["opinion"]["15"][0], variable=ComOp7Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO722 = Radiobutton(frame3, text=date["opinion"]["15"][1], variable=ComOp7Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO723 = Radiobutton(frame3, text=date["opinion"]["15"][2], variable=ComOp7Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO724 = Radiobutton(frame3, text=date["opinion"]["15"][3], variable=ComOp7Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO721.place(x=1100, y = 310)
CO722.place(x=1100, y = 350)
CO723.place(x=1100, y = 400)
CO724.place(x=1100, y = 440)

ComOp8Var = [IntVar() for j in range(2)]

Text11 = Label(frame3, text = "Качество доклада.\n Навыки публичной дискуссии", font='Courier 15 bold', bg='#FDE6D5')
Text11.place(x=1100, y = 510)

CO811 = Radiobutton(frame3, text=date["opinion"]["16"][0], variable=ComOp8Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO812 = Radiobutton(frame3, text=date["opinion"]["16"][1], variable=ComOp8Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO813 = Radiobutton(frame3, text=date["opinion"]["16"][2], variable=ComOp8Var[0], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO814 = Radiobutton(frame3, text=date["opinion"]["16"][3], variable=ComOp8Var[0], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
CO811.place(x=1100, y =570)
CO812.place(x=1100, y = 610)
CO813.place(x=1100, y = 650)
CO814.place(x=1100, y = 690)

Next3 = Button(frame3, text='  Далее  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame3)
Next3.place(x=1300, y = 740)

Back3 = Button(frame3, text='  Назад  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame)
Back3.place(x=1180, y =740)

#Третья страница информации

frame4 = Frame(root, bg="#FDE6D5")

CO811 = Radiobutton(frame4, text=date["opinion"]["17"][0], variable=ComOp8Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO812 = Radiobutton(frame4, text=date["opinion"]["17"][1], variable=ComOp8Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO813 = Radiobutton(frame4, text=date["opinion"]["17"][2], variable=ComOp8Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO814 = Radiobutton(frame4, text=date["opinion"]["17"][3], variable=ComOp8Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO811.place(x=20, y =20)
CO812.place(x=20, y = 60)
CO813.place(x=20, y = 100)
CO814.place(x=20, y = 140)

ComOp9Var = [IntVar() for j in range(2)]

Text12 = Label(frame4, text = "Качество презентации результатов\n работы (слайды)", font='Courier 15 bold', bg='#FDE6D5')
Text12.place(x=20, y = 190)

CO911 = Radiobutton(frame4, text=date["opinion"]["18"][0], variable=ComOp9Var[0], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO912 = Radiobutton(frame4, text=date["opinion"]["18"][1], variable=ComOp9Var[0], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO911.place(x=20, y=260)
CO912.place(x=20, y=300)

CO921 = Radiobutton(frame4, text=date["opinion"]["19"][0], variable=ComOp9Var[1], value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO922 = Radiobutton(frame4, text=date["opinion"]["19"][1], variable=ComOp9Var[1], value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO923 = Radiobutton(frame4, text=date["opinion"]["19"][2], variable=ComOp9Var[1], value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO924 = Radiobutton(frame4, text=date["opinion"]["19"][3], variable=ComOp9Var[1], value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO921.place(x=20, y =340)
CO922.place(x=20, y = 380)
CO923.place(x=20, y = 420)
CO924.place(x=20, y = 460)

ComOp9_1Var = [BooleanVar() for j in range(3)]

CO931 = Checkbutton(frame4, text=date["opinion"]["20"],variable = ComOp9_1Var[0], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CO931.place(x=20, y = 520)
CO932 = Checkbutton(frame4, text=date["opinion"]["21"],variable = ComOp9_1Var[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CO932.place(x=20, y = 545)
CO933 = Checkbutton(frame4, text=date["opinion"]["22"],variable = ComOp9_1Var[2], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5')
CO933.place(x=20, y = 570)

ComOp10Var = IntVar()

Text13 = Label(frame4, text = "Степень выполнения задач и\n реализация цели ВКР", font='Courier 15 bold', bg='#FDE6D5')
Text13.place(x=20, y = 610)

CO1011 = Radiobutton(frame4, text=date["opinion"]["23"][0], variable=ComOp10Var, value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1012 = Radiobutton(frame4, text=date["opinion"]["23"][1], variable=ComOp10Var, value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1013 = Radiobutton(frame4, text=date["opinion"]["23"][2], variable=ComOp10Var, value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1014 = Radiobutton(frame4, text=date["opinion"]["23"][3], variable=ComOp10Var, value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1011.place(x=20, y =670)
CO1012.place(x=20, y = 695)
CO1013.place(x=20, y = 720)
CO1014.place(x=20, y = 745)

Text14 = Label(frame4, text = "Оценка техникоэкономического\n обоснования (ТЭО), выполненного\n в рамках ВКР исследования или проекта", font='Courier 15 bold', bg='#FDE6D5')
Text14.place(x=520, y = 20)

ComOp11Var = IntVar()

CO1111 = Radiobutton(frame4, text=date["opinion"]["24"][0], variable=ComOp11Var, value=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1112 = Radiobutton(frame4, text=date["opinion"]["24"][1], variable=ComOp11Var, value=1, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1113 = Radiobutton(frame4, text=date["opinion"]["24"][2],variable=ComOp11Var, value=2, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1114 = Radiobutton(frame4, text=date["opinion"]["24"][3], variable=ComOp11Var, value=3, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1111.place(x=530, y =110)
CO1112.place(x=530, y = 140)
CO1113.place(x=530, y = 180)
CO1114.place(x=530, y = 210)

Text14 = Label(frame4, text = "Отмечается", font='Courier 15 bold', bg='#FDE6D5')
Text14.place(x=530, y = 260)

ComOp12Var = [BooleanVar() for j in range(12)]

CO1211 = Checkbutton(frame4, text=date["opinion"]["25"],variable = ComOp12Var[0], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1211.place(x=530, y = 290)

CO1212 = Checkbutton(frame4, text=date["opinion"]["26"],variable = ComOp12Var[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1212.place(x=530, y = 310)

CO1213 = Checkbutton(frame4, text=date["opinion"]["27"],variable = ComOp12Var[2], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1213.place(x=530, y = 350)

CO1214 = Checkbutton(frame4, text=date["opinion"]["28"],variable = ComOp12Var[3], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1214.place(x=530, y = 420)

CO1215 = Checkbutton(frame4, text=date["opinion"]["29"],variable = ComOp12Var[4], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1215.place(x=530, y = 470)

CO1216 = Checkbutton(frame4, text=date["opinion"]["30"],variable = ComOp12Var[5], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1216.place(x=530, y = 490)

CO1217 = Checkbutton(frame4, text=date["opinion"]["31"],variable = ComOp12Var[6], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1217.place(x=530, y = 540)

CO1218 = Checkbutton(frame4, text=date["opinion"]["32"],variable = ComOp12Var[7], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1218.place(x=530, y = 580)

CO1219 = Checkbutton(frame4, text=date["opinion"]["33"],variable = ComOp12Var[8], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1219.place(x=530, y = 620)

CO12110 = Checkbutton(frame4, text=date["opinion"]["34"],variable = ComOp12Var[9], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO12110.place(x=530, y = 680)

CO12111 = Checkbutton(frame4, text=date["opinion"]["35"],variable = ComOp12Var[10], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO12111.place(x=530, y = 720)

CO12112 = Checkbutton(frame4, text=date["opinion"]["36"],variable = ComOp12Var[11], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO12112.place(x=530, y = 760)

Text15 = Label(frame4, text = "Также отмечается", font='Courier 20 bold', bg='#FDE6D5')
Text15.place(x=1100, y = 20)

AddField = Entry(frame4, bg = 'white', width=35, font='Courier 12')
AddField.place(x=1100, y = 60)

NewAdd = Button(frame4, text='Добавить', bg = 'grey',font='Courier 12 bold', command=new_add)
NewAdd.place(x=1100, y = 90)

DeleteAdd = Button(frame4, text='Очистить', bg = 'grey',font='Courier 12 bold', command=delete_add)
DeleteAdd.place(x=1200, y = 90)

ActualAdd = Label(frame4, text = "", font='Courier 12 bold', bg='#FDE6D5', wraplength=480, justify=tkinter.LEFT)
ActualAdd.place(x=1100, y = 125)

ComOp13Var = [BooleanVar() for j in range(3)]

LackField = [BooleanVar() for j in range(7)]

Text17 = Label(frame4, text = "Недостатки работы", font='Courier 20 bold', bg='#FDE6D5')
Text17.place(x=1100, y = 280)

Lack1 = Checkbutton(frame4, text=date["opinion"]["40"],variable = LackField[0], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack1.place(x=1100, y = 310)

Lack2 = Checkbutton(frame4, text=date["opinion"]["41"],variable = LackField[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack2.place(x=1100, y = 330)

Lack3 = Checkbutton(frame4, text=date["opinion"]["42"],variable = LackField[2], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack3.place(x=1100, y = 350)

Lack4 = Checkbutton(frame4, text=date["opinion"]["43"],variable = LackField[3], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack4.place(x=1100, y = 420)

Lack5 = Checkbutton(frame4, text=date["opinion"]["44"],variable = LackField[4], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack5.place(x=1100, y = 460)

Lack6 = Checkbutton(frame4, text=date["opinion"]["45"],variable = LackField[5], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack6.place(x=1100, y = 510)

Lack7 = Checkbutton(frame4, text=date["opinion"]["46"],variable = LackField[6], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=400, justify=tkinter.LEFT)
Lack7.place(x=1100, y = 550)

Lack_1Label = Label(frame4, text = "Другое:", font='Courier 12', bg='#FDE6D5')
Lack_1Label.place(x = 1100, y = 640)
Lack_1Field = Entry(frame4, bg = 'white', width=40, font='Courier 12')
Lack_1Field.place(x=1100, y = 670)

Next4 = Button(frame4, text='  Далее  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame4)
Next4.place(x=1300, y = 740)

Back4 = Button(frame4, text='  Назад  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame2)
Back4.place(x=1180, y =740)

#Последний фрейм
frame5 = Frame(root, bg="#FDE6D5")

Text16 = Label(frame5, text = "Рекомендации", font='Courier 20 bold', bg='#FDE6D5')
Text16.place(x=20, y = 20)

CO1311 = Checkbutton(frame5, text='Рекомендация к магистратуре.',variable = ComOp13Var[0], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1311.place(x=20, y = 50)

CO1312 = Checkbutton(frame5, text='Рекомендация к публикации.',variable = ComOp13Var[1], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1312.place(x=20, y = 80)

CO1313 = Checkbutton(frame5, text='Рекомендация к внедрению.',variable = ComOp13Var[2], onvalue=1, offvalue=0, font='Courier 10', bg = '#FDE6D5', wraplength=480, justify=tkinter.LEFT)
CO1313.place(x=20, y = 110)

Mark_label = Label(frame5, text = "Оценка", font='Courier 15 bold', bg="#FDE6D5")
Mark_label.place(x=20, y = 160)
MarkVar = StringVar()
MarkField = ttk.Combobox(frame5, textvariable = MarkVar, font='Courier 12', width = 35)
MarkField['values'] = ['Отлично', 'Хорошо', 'Удовлетворительно', 'Неудовлетворительно']
MarkField.place(x = 130, y = 160)

Qualif_label = Label(frame5, text = "Полученная квалификация", font='Courier 15 bold', bg="#FDE6D5")
Qualif_label.place(x=20, y = 200)
QualifVar = StringVar()
QualifField = ttk.Combobox(frame5, textvariable = QualifVar, font='Courier 12', width = 35)
QualifField['values'] = ['Бакалавр', 'Специалист', 'Магистр']
QualifField.place(x = 320, y = 200)

YesLabel = Label(frame5, text = "За: ", font='Courier 15', bg="#FDE6D5")
YesLabel.place(x=20, y = 240)
YesField = Entry(frame5, bg = 'white', width=10, font='Courier 12')
YesField.place(x=20, y = 270)

NoLabel = Label(frame5, text = "Против: ", font='Courier 15', bg="#FDE6D5")
NoLabel.place(x=170, y = 240)
NoField = Entry(frame5, bg = 'white', width=10, font='Courier 12')
NoField.place(x=170, y = 270)

AbstainedLabel = Label(frame5, text = "Воздержались: ", font='Courier 15', bg="#FDE6D5")
AbstainedLabel.place(x=310, y = 240)
AbstainedField = Entry(frame5, bg = 'white', width=10, font='Courier 12')
AbstainedField.place(x=310, y = 270)

SaveAll = Button(frame5, text='Сохранить протокол', bg = 'lightgrey',font='Courier 12 bold', command=save_all)
SaveAll.place(x=100, y = 340)

ToBegin = Button(frame5, text='Вернуться в начало', bg = 'lightgrey',font='Courier 12 bold', command=open_first)
ToBegin.place(x=300, y = 340)

Back = Button(frame5, text='  Назад  ', bg = 'lightgrey',font='Courier 12 bold', command=next_frame3)
Back.place(x=1180, y =740)

root.mainloop()
