import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, 'data', 'example_input.csv')
output_file = os.path.join(script_dir, 'result', 'vedomost_result.xlsx')


def load_and_clean(file_path):
  
    df = pd.read_csv(file_path, encoding='utf-8', sep=None, engine='python')
    print(f"1. Считано строк из файла: {len(df)}")

    
    df.columns = [str(col).strip().lower() for col in df.columns]
    print("Колонки:", df.columns.tolist())


    required = ['обозначение', 'наименование']
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"В файле нет колонок: {missing}. Найдены только: {df.columns.tolist()}")

    for col in required:
        df[col] = df[col].astype(str).str.strip().replace({'': pd.NA, 'nan': pd.NA, 'None': pd.NA})

 
    before = len(df)
    df = df.dropna(subset=required)
    print(f"2. Удалено строк с пустыми полями: {before - len(df)}")


    df = df.reset_index(drop=True)
    print(f"3. Итог после очистки: {len(df)} строк")
    return df


def get_category(name):
    name_low = str(name).lower()
    if any(x in name_low for x in ['болт', 'гайка', 'шайба']):
        return 'Крепёж'
    elif 'подшипник' in name_low:
        return 'Подшипники'
    elif any(x in name_low for x in ['уплотнение', 'кольцо']):
        return 'Уплотнения'
    elif any(x in name_low for x in ['кабель', 'провод', 'автомат']):
        return 'Электрооборудование'
    else:
        return 'Прочие'


def group_by_category(df):
    df['категория'] = df['наименование'].apply(get_category)
    return df


def save_to_excel(df, output_path):
    folder = os.path.dirname(output_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
  
        df.to_excel(writer, sheet_name='Ведомость', index=False)
       
        for cat, group in df.groupby('категория'):
            
            sheet_name = cat[:31]
            group.to_excel(writer, sheet_name=sheet_name, index=False)


if __name__ == '__main__':
    try:
        df_raw = load_and_clean(input_file)
        df_grouped = group_by_category(df_raw)

        print("Распределение по категориям:")
        print(df_grouped['категория'].value_counts().to_string())

        save_to_excel(df_grouped, output_file)
        print(f'Готово: {output_file}')
    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути: {input_file}")
        print("Проверь, что папка data существует и в ней лежит example_input.csv")
    except Exception:
        import traceback
        traceback.print_exc()
    finally:
        input('Press Enter to exit...')
