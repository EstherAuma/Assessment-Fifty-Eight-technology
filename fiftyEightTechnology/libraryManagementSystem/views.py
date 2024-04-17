from django.shortcuts import render, redirect, get_object_or_404
from .forms import BorrowBookForm,ReturnBookForm
from .models import Book,BorrowedBook,ReturnedBook
from django.contrib import messages
from django.utils import timezone


# borrow books
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book'].id
            book = Book.objects.get(pk=book_id)
            if book.number_of_copies > 0:
                borrowed_book = form.save()
                book.number_of_copies -= 1
                book.save()
                return redirect('all_books')
            else:
                form.add_error(None, 'No copies of this book available for borrowing.')
    else:
        form = BorrowBookForm()
    return render(request, 'borrow_book.html', {'form': form})

def all_books(request):
    books = Book.objects.all().order_by('id')  
    return render(request, 'all_books.html', {'books': books})


#return books
def return_book(request):
    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            returned_book_instance = form.save()  # Save the returned book instance

            # Call increase_copies method to increase the number of copies
            returned_book_instance.increase_copies()

            return redirect('all_books')
    else:
        form = ReturnBookForm()
    return render(request, 'return_book.html', {'form': form})


#all borrowed books
def all_borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    
    context = {
        'borrowed_books': borrowed_books
    }
    return render(request, 'all_borrowed_books.html', context)


#overdue books
def overdue_books(request):
    overdue_books = BorrowedBook.objects.filter(due_date__lt=timezone.now().date())
    return render(request, 'overdue_books.html', {'overdue_books': overdue_books})