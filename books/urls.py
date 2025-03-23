from django.urls import path
from .views import admin_signup, admin_login, create_book, get_books, update_book, delete_book

urlpatterns = [
    
    path('admin/signup/', admin_signup, name='admin_signup'),
    path('admin/login/', admin_login, name='admin_login'),
    path('books/', get_books, name='get_books'),
    path('books/create/', create_book, name='create_book'),
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
