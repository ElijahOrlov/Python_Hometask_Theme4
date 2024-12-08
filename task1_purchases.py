
import json


def get_purchases(purchase_filename: str) -> dict:
    """
    Перевод содержимого входящего файла лога покупок в словарь вида {"user_id": "", "category": ""}
    :param purchase_filename: наименование файла лога
    :return: словарь из данных файла
    """
    purchases = {}
    with open(purchase_filename, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line: continue
            purchase = json.loads(line)
            user_id = purchase.get("user_id")
            category = purchase.get("category")
            if user_id not in ("", "user_id") and category not in ("", "category"):
                purchases[user_id] = category
    return purchases


def show_result():
    for index, (user_id, category) in enumerate(get_purchases("purchase_log.txt").items()):
        print(f"{user_id} '{category}'")
        if index == 1: break
# show_result()

