from .models import Category
from .forms import BookSearchForm

def category_links(request):
    categories =Category.objects.all()
    return ({'categories':categories})

def book_search(request):
    search_form = BookSearchForm
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return {'search_form':search_form}











