# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

        for row in data:
            for key in row:
                try:
                    row[key] = f"{float(row[key]):.6f}"
                except ValueError:
                    pass
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':

    task()

    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
