import pandas as pd

# Загрузка данных из листов Excel
movement_df = pd.read_excel('C:\\Users\\Profil1\\Documents\\решение задач\\03.xlsx', sheet_name='Движение товаров')

# Фильтрация данных для продаж кофе в магазинах Октябрьского района за указанный период
coffee_skus = [46, 47, 48]  # Пример артикулов кофе
october_shops = ['M1', 'M5', 'M6', 'M10', 'M15']
filtered_df = movement_df[(movement_df['Тип операции'] == 'Продажа') &
                          (movement_df['ID магазина'].isin(october_shops)) &
                          (movement_df['Артикул'].isin(coffee_skus)) &
                          (movement_df['Дата'].dt.month == 6) &
                          (movement_df['Дата'].dt.day.between(1, 10))]

# Расчет общей выручки, учитывая количество упаковок и цену за упаковку
total_revenue = (filtered_df['Количество упаковок, шт.'] * filtered_df['Цена руб./шт.']).sum()

print(total_revenue)

# Изменяем некоторые данные исходя из условия задания!