# подключаем дополнительные блоки
import work_with_file.add_report
import work_with_file.replace_tags
import work_with_file.change_table

# блок формирующий файлы
def Create_reports(Report_number, tags, table_tags):
    # Report_number - номер отчёта, пока не задаеётся
    # tags - тэги для замены

    # название файла с отчётами
    Report_name = "Report-" + str(Report_number) + ".docx"

    # Добаваляем новый отчёт в список отчётов
    work_with_file.add_report.add_report(Report_name)

    # заменяем тэги в новом отчёте соответствующими значениями
    work_with_file.replace_tags.replace_tags(Report_name, tags)

    # заменяем тэшги в таблицах соответствующими значениями
    work_with_file.change_table.replace_tags_in_table(Report_name, table_tags)