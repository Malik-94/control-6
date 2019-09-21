from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from webapp.models import Book


def index_view(request):
    # здесь нужно поставить правильный филтьр
    # и сортировку вместо all()
    #book = Book.objects.order_by('category', 'name')
    book = Book.objects.all()
    return render(request, 'index.html', context={
        'books': book
    })


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')