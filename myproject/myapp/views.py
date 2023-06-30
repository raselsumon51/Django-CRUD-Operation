from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_create(request):
    form = BookForm(request.POST or None)
    print(form)
    if form.is_valid():
        print("valid")
        form.save()
        return redirect('book_list')
    print('render')
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    print(pk)
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
