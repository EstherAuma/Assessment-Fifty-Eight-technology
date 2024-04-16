from django.forms import ModelForm
from .models import *

from django import forms

class BorrowBookForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select a due date'
    )
    username = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select your name")
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label="Select a book")

    class Meta:
        model = BorrowedBook
        fields = ['username', 'book', 'due_date']
class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = ReturnedBook
        fields = [ 'username','returned_book']

# class OverdueBooksForm(forms.ModelForm):
#     due_date = forms.DateField(
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date',
#                 'class': 'datepicker' 
#             }
#         )
#     )

#     class Meta:
#         model = OverdueBook
#         fields = ['borrowed_book','username', 'fine_amount']