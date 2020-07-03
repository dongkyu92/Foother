from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .forms import ReviewForm, CommentForm
from .models import Review
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    # user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('accounts:profile', review.user.username)

    else:
        form = ReviewForm()
        # key = config('API_KEY')

    context = {
        'form' : form,
        # 'key' : key,
    }
    return render(request, 'maps/review_create.html', context)

@login_required
def comment_create(request,pk):
    
    if request.method == 'POST':
        print("comment post 들어옴")
        review = Review.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            print("comment post_valid 들어옴")
            comment = form.save(commit=False)
            print(comment)
            comment.review = review
            comment.save()
            return redirect('maps:comment_create_complete')
    else:
        print("comment get 들어옴")
        form = CommentForm()
        context = {
            'form' : form,
            'pk' : pk,
        }
        print(form)
    
    return render(request, 'maps/review_comment_create.html',context)

def comment_create_complete(request):
    return render(request, 'maps/complete.html')