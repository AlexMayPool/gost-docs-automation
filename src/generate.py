import pandas as pd
import os

def load_and_clean(path):
    df = pd.read_csv(path, sep=',', encoding='utf-8')  # тут разделитель запятая, как в нашем примере
    df.columns = df.columns.str.strip()
    if 'наименование' in df.columns:
        df['наименование'] = df['наименование'].astype(str).str.strip()
    if 'обозначение' in df.columns:
        df['обозначение'] = df['обозначение'].astype(str).str.strip()
    df = df.dropna(subset=['обозначение', 'наименование'], how='any')
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
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for cat, group in df.groupby('категория'):
            group.to_excel(writer, sheet_name=cat, index=False)
        df.to_excel(writer, sheet_name='Ведомость', index=False)

if __name__ == '__main__':
    input_file = 'data/example_input.csv'
    output_file = 'result/vedomost_result.xlsx'
    try:
        df_raw = load_and_clean(input_file)
        df_grouped = group_by_category(df_raw)
        save_to_excel(df_grouped, output_file)
        print(f'Готово: {output_file}')
    except Exception as e:
        print(f'Ошибка: {e}')
