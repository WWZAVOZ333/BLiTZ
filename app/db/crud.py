from app.db.models import Category, Book

def create_category(session, title):
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_all_categories(session):
    return session.query(Category).order_by(Category.id).all()

def create_book(session, title, description, price, url, category_id):
    book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def get_all_books(session):
    return session.query(Book).order_by(Book.id).all()

def get_books_by_category(session, category_id):
    return session.query(Book).filter_by(category_id=category_id).all()