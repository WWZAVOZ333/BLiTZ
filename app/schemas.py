from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal

# --- Схемы для Категорий ---
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True) # Замена orm_mode в Pydantic v2

# --- Схемы для Книг ---
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Decimal
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)