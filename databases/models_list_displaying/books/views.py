from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request, pub_date=None):
    context = {}
    all_books = Book.objects.all()
    all_books_sorted = Book.objects.all().order_by('pub_date')

    if pub_date is None:
        context['books'] = all_books
        template = 'books/books_list.html'
        return render(request, template, context)
    else:
        template = 'books/book.html'
        paginator = Paginator(all_books_sorted, 1)
        for page, book in enumerate(all_books_sorted, start=1):
            if pub_date == book.pub_date:
                current_page = paginator.page(page)
                if current_page.has_previous():
                    prev_book_date = paginator.page(current_page.previous_page_number()).object_list[0].pub_date
                    context['prev_pub_date'] = prev_book_date
                if current_page.has_next():
                    next_book_date = paginator.page(current_page.next_page_number()).object_list[0].pub_date
                    context['next_pub_date'] = next_book_date
                context['book'] = book
        return render(request, template, context)
