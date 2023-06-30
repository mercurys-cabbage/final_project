# работа с docx файлами
import docx
from docx.shared import Pt
# объединение файлов
from docxcompose.composer import Composer
from docx import Document as Document_compose
# для удаления временного файла
import os
# для проверки наличия файла
import os.path

# функция добавления незаполненного отчёта
def add_report(Report_name):
    # проверяем существование файла с отчётом
    # если его нет, то сначала создадим его
    if not(os.path.exists(Report_name)):
        # создаём новый пустой документ
        Report = docx.Document("Head_example.docx")
        style = Report.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)
        Report.save(Report_name)


    # master файл в который будем добавлять отчёты
    master = Document_compose(Report_name)

    compose = Composer(master)
    # загружаем заполненный шаблон
    New_Report = Document_compose("Report_example.docx")

    # добавляем заполненный шаблон к остальным отчётам
    compose.append(New_Report)

    # сохраняем отчёт с добавленным шаблоном
    compose.save(Report_name)



