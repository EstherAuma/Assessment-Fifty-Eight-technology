from django.shortcuts import render, redirect, get_object_or_404
from .forms import BorrowBookForm,ReturnBookForm,OverdueBooksForm
from .models import Book,BorrowedBook,OverdueBook
from django.contrib import messages
from django.utils import timezone

# Create your views here.
# views.py
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book'].id
            book = Book.objects.get(pk=book_id)
            if book.availability == Book.YES and book.number_of_copies > 0:
                borrowed_book = form.save()
                book.number_of_copies -= 1
                book.save()
                return redirect('all_books')
            else:
                if book.availability == Book.NO:
                    form.add_error(None, 'This book is not available for borrowing.')
                else:
                    form.add_error(None, 'No copies of this book available for borrowing.')
    else:
        form = BorrowBookForm()
    return render(request, 'borrow_book.html', {'form': form})

def all_books(request):
    books = Book.objects.all().order_by('id')  
    return render(request, 'all_books.html', {'books': books})

def return_book(request):
    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('all_borrowed_books') 
    else:
        form = ReturnBookForm()
    return render(request, 'return_book.html', {'form': form})

def all_borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    
    context = {
        'borrowed_books': borrowed_books
    }
    return render(request, 'all_borrowed_books.html', context)


def overdue_books(request):
    if request.method == 'POST':
        form = OverdueBooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_overdue_books')
    else:
        form = OverdueBooksForm()
        
    context = {'form': form}
    return render(request, 'overdue_books.html', context)

def all_overdue_books(request):
    overdue_books = OverdueBook.objects.all()  # Query all OverdueBook instances
    return render(request, 'all_overdue_books.html', {'overdue_books': overdue_books})