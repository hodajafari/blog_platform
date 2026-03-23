from django.shortcuts import render

# Create your views here.
from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from .forms import CommentForm
from .models import Comment
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q', '')

    posts_list = Post.objects.exclude(id__isnull=True).order_by('-created_at')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(posts_list, 5) 

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {
        'posts': posts,
        'query': query
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            if request.user.is_authenticated:
                comment.author = request.user
            
            parent_id = request.POST.get('parent_id')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id, post=post)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass 

            comment.save()

            messages.success(request, "Comment submitted successfully ✅")
            return redirect('post_detail', id=post.id)

    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    liked_posts = request.session.get('liked_posts', [])

    if id in liked_posts:
        liked_posts.remove(id)
        liked = False
        post.likes_count = post.likes_count - 1 if post.likes_count > 0 else 0
    else:
        liked_posts.append(id)
        liked = True
        post.likes_count = post.likes_count + 1

    request.session['liked_posts'] = liked_posts
    post.save()

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes_count
    })
def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('home')

    else:

        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


def edit_post(request, id):

    post = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():

        form.save()

        return redirect('post_detail', id=id)

    return render(request, 'blog/edit_post.html', {'form': form})


def delete_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})
@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.author:
        return redirect('post_detail', id=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated ✅")
            return redirect('post_detail', id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.author:
        return redirect('post_detail', id=comment.post.id)

    if request.method == "POST":
        post_id = comment.post.id
        comment.delete()
        messages.success(request, "Comment deleted ❌")
        return redirect('post_detail', id=post_id)

    return render(request, 'blog/delete_comment.html', {'comment': comment})