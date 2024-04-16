from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    YES = 'Yes'
    NO = 'No'
    AVAILABILITY_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    name = models.CharField(max_length=25, blank=False, null=False)
    genre = models.CharField(max_length=50, blank=False, null=False)
    availability = models.CharField(max_length=3, choices=AVAILABILITY_CHOICES, default=YES)
    number_of_copies = models.IntegerField(blank=False, null=False)
    book_number = models.CharField(max_length=25, blank=False, null=False)
    author = models.CharField(max_length=25, blank=False, null=False)
    publisher = models.CharField(max_length=25, blank=False, null=False)
    language = models.CharField(max_length=25, default='English')

    def __str__(self):
        return self.name


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    fine_amount = models.CharField(max_length=50, null=False, blank=False, default='$10.00 dollars')  # Fine amount field

    def __str__(self):
        return f"{self.book.name} - {self.username}"
    
    def is_overdue(self):
        return self.due_date < timezone.now().date()
    
class ReturnedBook(models.Model):
    returned_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    returned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.returned_book.book.name} - Returned"

    def increase_copies(self):
        # Get the returned book
        returned_book = self.returned_book.book

        # Increase the number of copies by 1
        returned_book.number_of_copies += 1
        returned_book.save()

    
# class OverdueBook(models.Model):
#     borrowed_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE)
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     fine_amount = models.CharField(max_length=20, default='10 dollars')

#     def __str__(self):
#         return f"Overdue Book: {self.borrowed_book.book.name} - {self.username}"

    

