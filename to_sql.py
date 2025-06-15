import sqlite3
import os

def sqlite_to_sql(input_db, output_sql):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(input_db)
        with open(output_sql, 'w', encoding='utf-8') as f:
            # Итерируем по всем SQL-командам из дампа
            for line in conn.iterdump():
                f.write(f"{line}\n")
        print(f"Дамп успешно сохранен в {output_sql}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if conn:
            conn.close()

# === Пример использования ===
if __name__ == "__main__":
    input_file = "django_project/db.sqlite3"   # Укажите ваш .sqlite3 файл
    output_file = "dump.sql"         # Имя выходного SQL-файла

    if not os.path.exists(input_file):
        print(f"Файл {input_file} не найден!")
    else:
        sqlite_to_sql(input_file, output_file)