from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length= 25, blank=False, null=False)
    genre = models.CharField(max_length= 50, blank=False, null=False)
    availability = models.BooleanField(default=True)
    number_of_copies = models.IntegerField(blank=False, null=False)
    book_number = models.CharField(max_length= 25, blank=False, null=False)
    author = models.CharField(max_length= 25, blank=False, null=False)
    publisher = models.CharField(max_length= 25, blank=False, null=False)
    Language = models.CharField(max_length= 25,default= 'English' )

    def __str__(self):
        return self.name


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    

    def __str__(self):
        return f"{self.book.name} - {self.username}"
    
    def is_overdue(self):
        return self.due_date < timezone.now().date()
    
class ReturnedBook(models.Model):
    returned_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE)
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    returned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.returned_book.book.name} - Returned"

    
class OverdueBook(models.Model):
    borrowed_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    fine_amount = models.CharField(max_length=20, default='10 dollars')

    def __str__(self):
        return f"Overdue Book: {self.borrowed_book.book.name} - {self.username}"

    

