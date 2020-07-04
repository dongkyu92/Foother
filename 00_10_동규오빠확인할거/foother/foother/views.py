from django.shortcuts import render
from maps.models import Review
from maps.forms import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()


def foother_index(request):
    reviews = Review.objects.all()
    users = User.objects.all()
    if len(users) > 10:
        while len(users) == 10:
            del users[-1]

    # usernames = [ x.username for x in users ]
    # userscores = [ x.user_score for x in users ]
    # rank = [ x for x in range(1,len(user)+1) ]
    # print(rank)
    # rank = str(rank)
    # print(usernames)
    # print(userscores)
    # userranks = [rank, usernames, userscores]
    # users = {
    #     'userranks': usernames, userscores
    #     "usernames": usernames,
    #     "userscores": userscores,
    # }
    paginator = Paginator(reviews, 12)
    
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    context = {
         'reviews' : reviews,
        # 'userranks' : userranks,
        'users' : users,
    }
    return render(request, 'review_all.html', context)