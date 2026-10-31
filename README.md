# gost-docs-automation

Автоматизирую подготовку ведомостей покупных изделий по ГОСТ из «грязных» Excel/CSV.

## Что делает
Скрипт автоматически очищает и структурирует «грязные» данные: убирает пустые строки, нормализует регистр, группирует по категориям и формирует итоговую ведомость.

## Результат (до/после)

| До: сырой CSV с мусором | После: готовая ведомость |
| --- | --- |
| ![До](screens/placeholder.png) | ![После](screens/placeholder.png) |

> Примечание: скриншоты будут добавлены после локального запуска скрипта.

## Как запустить
```bash
git clone https://github.com/AlexMayPool/gost-docs-automation.git
cd gost-docs-automation
pip install -r requirements.txt
python src/generate.py
```
## Технологии
- Python 3
- pandas
- openpyxl

## Входные данные
Файл `data/example_input.csv` — реалистичные «грязные» данные, как на реальных заводах.

## Выход
Файл `result/vedomost_result.xlsx` — готовая ведомость с группировкой по разделам и итоговым листом.
