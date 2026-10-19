from app.db.db import get_session
from app.db import crud

def main():
    session = get_session()
    try:
        print("=== ВЫВОД ДАННЫХ ИЗ БАЗЫ ===")
        categories = crud.get_all_categories(session)
        for c in categories:
            print(f"\nКатегория: {c.title}")
            books = crud.get_books_by_category(session, c.id)
            for b in books:
                print(f"  - {b.title} | Цена: {b.price} | Описание: {b.description}")
    finally:
        session.close()

if __name__ == "__main__":
    main()