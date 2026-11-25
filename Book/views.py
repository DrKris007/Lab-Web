from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'books/index.html', {"posts": posts})

def detail(request, post_id):
    return render(request, 'books/detail.html')

def create(request):
    if request.method == 'POST':
        # Handle form submission
        title = request.POST['title']
        author = request.POST['author']
        summary = request.POST['summary']
        description = request.POST['description']
        cover = request.FILES['cover']
        pdf = request.FILES['pdf']

        Post.objects.create(
            title=title,
            author=author,
            summary=summary,
            description=description,
            cover=cover,
            pdf=pdf
        )
    redirect('book:list')  # Redirect to the home page after creating the book

    #     print(f"Title: {title}, Author: {author}, Summary: {summary}, Description: {description}")
    return render(request, 'books/create-book.html')

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('book:list')  # Redirect to the home page after deleting the book

def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle form submission
        title = request.POST['title']
        author = request.POST['author']
        summary = request.POST['summary']
        description = request.POST['description']
        cover = request.FILES.get('cover')
        pdf = request.FILES.get('pdf')

        # Update the post fields
        post.title = title
        post.author = author
        post.summary = summary
        post.description = description
        if cover:
            post.cover = cover
        if pdf:
            post.pdf = pdf

        post.save()
        return redirect('book:list')  # Redirect to the home page after updating the book

    return render(request, 'books/update.html', {"post": post})