from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views import generic

# Create your views here.
class BookListView(generic.ListView):
    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     db_data = Book.objects.all()
#     context = {"data":db_data}
#     return render(request, "books/index.html", context)

def show(request,id):
    singleBook = get_object_or_404(Book,id=id)
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    context = {"book":singleBook,"reviews":reviews}
    return render(request, "books/show.html", context)

def review(request,id):
    body = request.POST['review']
    newReview = Review(body=body,book_id=id)
    newReview.save()
    return redirect("/books")