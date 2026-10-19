from app.db.db import init_engine, get_session
from app.db import crud

def main():
    print("1. Создаем таблицы в базе данных...")
    init_engine()
    
    session = get_session()
    try:
        print("2. Добавляем категории и книги...")
        fiction = crud.create_category(session, "Художественная литература")
        tech = crud.create_category(session, "Техническая литература")

        crud.create_book(session, "Мастер и Маргарита", "Роман", 890.00, "", fiction.id)
        crud.create_book(session, "Чистый Python", "Книга по Python", 1990.00, "", tech.id)

        print("3. База данных успешно инициализирована!")
    finally:
        session.close()

if __name__ == "__main__":
    main()
