from task1_purchases import get_purchases
import csv

def find_visits(visits_filename: str) -> str:
    """
    Поиск всех покупок с определением категории из входящего файла лога визитов
    и формирование выходного файла в формате .csv со структурой (user_id,source,category)
    :param visits_filename: наименование файла лога визитов
    :return: наименование файла отчета о покупках
    """
    report_filename = "funnel.csv"
    purchases = get_purchases("purchase_log.txt")
    with (open(visits_filename, encoding='utf-8') as visits_file,
          open(report_filename, 'w', newline='') as report_file):
        visits_reader = csv.reader(visits_file)
        report_writer = csv.writer(report_file)

        report_writer.writerow(["user_id", "source", "category"])
        for visit in visits_reader:
            if len(visit) < 2: continue
            user_id, source = visit[:2]

            if user_id in purchases:
                category = purchases[user_id]
                report_writer.writerow([user_id, source, category])
    return report_filename


def show_result():
    for index, line in enumerate(open(find_visits("visit_log.csv"))):
        print(line, end="")
        if index == 2: break
show_result()
