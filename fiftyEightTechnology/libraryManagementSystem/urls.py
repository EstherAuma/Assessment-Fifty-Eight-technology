from django.urls import path
from libraryManagementSystem import views

urlpatterns = [
    # path('',views.borrow_book, name='borrow_book'),
    path('', views.all_books, name='all_books'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('all_borrowed_books', views.all_borrowed_books, name='all_borrowed_books'),
    path('overdue_books',views.overdue_books, name='overdue_books'),
    path('overdue_books/', views.overdue_books, name='overdue_books'), 
]