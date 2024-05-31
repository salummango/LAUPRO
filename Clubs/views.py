from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Club, Post, Comment, Notification,ClubMembership


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})

def club_detail_view(request, pk):
    club = get_object_or_404(Club, pk=pk)
    members = ClubMembership.objects.filter(club=club)
    posts = Post.objects.filter(club=club)
    return render(request, 'club_details.html', {
        'club': club,
        'members': members,
        'posts': posts
    })

def view_club(request, club_id):
    # Retrieve the club object
    club = get_object_or_404(Club, id=club_id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the user is a member of the club
        is_member = ClubMembership.objects.filter(user=request.user, club=club).exists()
        if is_member:
            # Retrieve posts and other details related to the club
            posts = Post.objects.filter(club=club)
            return render(request, 'club/post_list.html', {'club': club, 'posts': posts})
        else:
            # User is not a member of the club, display a message
            messages.warning(request, "You need to join the club to view its details.")
    else:
        # User is not authenticated, prompt them to log in
        messages.warning(request, "Please log in or register to view club details.")
    
    # Redirect the user to the previous page or a specific URL
    # You can customize the redirect behavior based on your requirements
    return redirect('Alumni_clubs:user_dashboard')  # Redirect to the home page or any other URL

def join_club(request, club_id):
    if request.method == 'POST':
        club = Club.objects.get(id=club_id)
        user = request.user
        # Check if the user is already a member of the club
        if ClubMembership.objects.filter(user=user, club=club).exists():
            messages.warning(request, 'You are already a member of this club.')
        else:
            membership = ClubMembership.objects.create(user=user, club=club)
            membership.save()
            messages.success(request, 'You have joined the club successfully.')
    return redirect('Alumni_clubs:dashboard')

# def post_list(request, club_id):
#     club = Club.objects.get(id=club_id)
#     posts = Post.objects.filter(club=club)
#     return render(request, 'post_list.html', {'club': club, 'posts': posts})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Club, Post
from .forms import PostForm

@login_required
def create_post(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.club = club
            post.save()
            return redirect('Alumni_clubs:view_club', club_id=club.id)
    else:
        form = PostForm()
    return render(request, 'club/create_post.html', {'form': form, 'club': club})


def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        author = request.user
        content = request.POST.get('content')

        try:
            if content and content.strip():  # Check if content is not empty or only whitespace
                comment = Comment.objects.create(post=post, author=author, content=content)
                # Optionally, send notifications to other members of the club
                return redirect('Clubs:view_club', club_id=post.club.id)  # Redirect to the post detail page
            else:
                # Handle empty comment
                # Optionally, display an error message to the user
                return redirect('Clubs:view_club', club_id=post.club.id)  # Still redirect to the post detail page
        except Exception as e:
            # Log the exception or handle it appropriately
            print(f"An error occurred: {e}")
            # Optionally, display an error message to the user
            return redirect('Clubs:view_club', club_id=post.club.id)  # Redirect to the post detail page
    else:
        return redirect('Clubs:user_dashboard')


def view_post(request, club_id, post_id):
    post = get_object_or_404(Post, pk=post_id, club__id=club_id)
    comments = Comment.objects.filter(post=post)  # Filter comments related to the post
    return render(request, 'club/post_comments.html', {'post': post, 'comments': comments})


def mark_notification_as_read(request, notification_id):
    if request.method == 'POST' and request.is_ajax():
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()
        return JsonResponse({'message': 'Notification marked as read'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    
from django.shortcuts import render, get_object_or_404
from .models import Club, Notification, ClubMembership

def user_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        clubs_not_member = Club.objects.exclude(clubmembership__user=user)
        notifications = Notification.objects.filter(user=user)
        memberships = ClubMembership.objects.filter(user=user)
        return render(request, 'user_dashboard.html', {
            'notifications': notifications,
            'memberships': memberships,
            'clubs_not_member': clubs_not_member
        })
    else:
        return redirect('login')  # Redirect to login if user is not authenticated


