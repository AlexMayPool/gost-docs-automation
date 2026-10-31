# gost-docs-automation

Автоматизирую формирование ведомостей покупных изделий по ГОСТ из «грязных» Excel/CSV.

## Что делает
Скрипт читает CSV с кривыми данными (пустые ячейки, примечания, разный регистр), нормализует их, группирует по категориям и формирует Excel-ведомость с отдельными листами по разделам.

## Результат (до/после)

| До: сырой CSV с мусором | После: готовая ведомость |
| --- | --- |
| ![До](screens/placeholder.png) | ![После](screens/placeholder.png) |

> Примечание: скриншоты будут добавлены после локального запуска скрипта.

## Как запустить
```bash
git clone https://github.com/<AlexMayPool>/gost-docs-automation.git
cd gost-docs-automation
pip install -r requirements.txt
python src/generate.py

## Технологии
- Python 3
- pandas
- openpyxl

## Входные данные
Файл `data/example_input.csv` — реалистичные «грязные» данные, как на реальных заводах.

## Выход
Файл `result/vedomost_result.xlsx` — готовая ведомость с группировкой по разделам и итоговым листом.
