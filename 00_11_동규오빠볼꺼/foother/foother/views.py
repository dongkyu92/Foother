from django.shortcuts import render
from maps.models import Review
from maps.forms import ReviewForm
# from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()

def foother_index(request):
    reviews = Review.objects.all()
    # paginator = Paginator(reviews, 12)
    users = User.objects.all()
    if len(users) > 10:
        while len(users) == 10:
            del users[-1]
    # page_number = request.GET.get('page')
    # reviews = paginator.get_page(page_number)
    # for star in len(reviews.food_star):
    

    context = {
        'reviews' : reviews,
        'users' : users,
    }
    return render(request, 'review_all.html', context)