from sqlalchemy.orm import Session
from app.db.models import Category, Book

# =========== CATEGORIES ===========
def create_category(session: Session, title: str) -> Category:
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_category(session: Session, category_id: int) -> Category | None:
    return session.get(Category, category_id)

def get_all_categories(session: Session) -> list[Category]:
    return session.query(Category).order_by(Category.id).all()

def update_category(session: Session, category_id: int, title: str) -> Category | None:
    category = session.get(Category, category_id)
    if category:
        category.title = title
        session.commit()
        session.refresh(category)
    return category

def delete_category(session: Session, category_id: int) -> bool:
    category = session.get(Category, category_id)
    if category:
        session.delete(category)
        session.commit()
        return True
    return False

# =========== BOOKS ===========
def create_book(session: Session, title: str, description: str | None, price: float, url: str | None, category_id: int) -> Book:
    book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def get_book(session: Session, book_id: int) -> Book | None:
    return session.get(Book, book_id)

def get_all_books(session: Session) -> list[Book]:
    return session.query(Book).order_by(Book.id).all()

def get_books_by_category(session: Session, category_id: int) -> list[Book]:
    return session.query(Book).filter_by(category_id=category_id).all()

def update_book(session: Session, book_id: int, **fields) -> Book | None:
    book = session.get(Book, book_id)
    if book:
        for key, value in fields.items():
            if hasattr(book, key):
                setattr(book, key, value)
        session.commit()
        session.refresh(book)
    return book

def delete_book(session: Session, book_id: int) -> bool:
    book = session.get(Book, book_id)
    if book:
        session.delete(book)
        session.commit()
        return True
    return False