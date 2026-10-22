from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from decimal import Decimal

# --- Схемы для Категорий ---
class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Название категории")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- Схемы для Книг ---
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    # Ограничиваем цену: она должна быть больше 0
    price: Decimal = Field(..., gt=0, description="Цена должна быть больше нуля")
    url: Optional[str] = Field(None, max_length=500)
    category_id: int = Field(..., gt=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[Decimal] = Field(None, gt=0)
    url: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = Field(None, gt=0)

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)