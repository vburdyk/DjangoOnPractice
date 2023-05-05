from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile, Post, LikePost, Comment


@login_required(login_url='/auth')
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})
    else:
        return redirect('/auth/')


def auth_page(request):
    return render(request, 'auth.html')


def auth_page_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Неправильні дані для входу!")
        return redirect('/auth')


# def signup_page(request):
#     return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Цей логін вже зайнятий!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                new_profile = Profile.objects.create(user=user)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Passwords not correct')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


@login_required(login_url='/auth')
def upload(request):
    return render(request, 'upload.html')


@login_required(login_url='/auth')
def upload_submit(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        title = request.POST['title']
        content = request.POST['content']

        new_post = Post.objects.create(user=user, image=image, title=title, content=content)
        new_post.save()

        return redirect('/')


@login_required(login_url='/auth')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()
        return redirect('/')


@login_required(login_url='/auth')
def make_comment_page(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, "add_comment.html", {"post_id": post_id})
    except:
        return HttpResponseNotFound("hello")


@login_required(login_url='/auth')
def make_comment_send(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        # comments = post.comments.all()

        username = request.POST['username']
        body = request.POST['body']

        new_comment = Comment.objects.create(username=username, body=body, post=post)
        new_comment.save()

        return redirect('/')
    else:
        return redirect('make-comment', post_id=post_id)


@login_required(login_url='/auth')
def delete_post(request, post_id=None):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('/')


@login_required(login_url='/auth')
def logout(request):
    auth.logout(request)
    return redirect('auth_page')
