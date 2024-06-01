from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import Alumni  # or the model that contains registration_no and password
from django.contrib.auth import login, authenticate

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            registration_no = cd['registration_no']  # Change 'username' to 'registration_no'
            password = cd['password']
            user = authenticate(request, registration_no=registration_no, password=password)  # Change 'username' to 'registration_no'
            if user is not None:
                if user.is_active:
                    login(request, user, backend='USER.backends.CustomAuthenticationBackend')  # Specify the authentication backend
                    return redirect('Alumni_clubs:user_dashboard')
                else:
                    return HttpResponse('Disabled user')
            else:
                return HttpResponse('Invalid login')
    return render(request, 'login.html', {'form': form})







# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import OtherInfo, History, Achieve
from .forms import OtherInfoForm, HistoryForm, AchieveForm
from .models import EducationalBackground

# List View
def list_details_view(request):
    if request.user.is_authenticated:
        user = request.user
        other_info = OtherInfo.objects.all()
        histories = History.objects.all()
        achievements = Achieve.objects.all()
        background = EducationalBackground.objects.all()
        return render(request, 'user/list_details.html', {
            'other_info': other_info,
            'histories': histories,
            'achievements': achievements,
            'background': background
        })
    else:
        return redirect('login')  # Redirect to login if user is not authenticated
    

# Create Views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OtherInfoForm

@login_required
def add_other_info(request):
    if request.method == 'POST':
        form = OtherInfoForm(request.POST, request.FILES)
        if form.is_valid():
            other_info = form.save(commit=False)
            other_info.alumni = request.user
            other_info.save()
            return redirect('list_details')
    else:
        form = OtherInfoForm()
    return render(request, 'user/form.html', {'form': form, 'title': 'Add Other Info'})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import OtherInfo, History
from .forms import HistoryForm

@login_required
def add_history(request):
    # Get the OtherInfo for the current user
    other_info = get_object_or_404(OtherInfo, alumni=request.user)
    
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.other_info = other_info
            history.save()
            return redirect('list_details')  # Update with the correct view name
    else:
        form = HistoryForm()

    return render(request, 'user/form.html', {'form': form, 'title': 'Add Work History'})


@login_required
def add_achieve(request):
    # Get the OtherInfo for the current user
    other_info = get_object_or_404(OtherInfo, alumni=request.user)
    
    if request.method == 'POST':
        form = AchieveForm(request.POST, request.FILES)
        if form.is_valid():
            achieve = form.save(commit=False)
            achieve.other_info = other_info
            achieve.save()
            return redirect('list_details')
    else:
        form = AchieveForm()
    return render(request, 'user/form.html', {'form': form, 'title': 'Add Achievement'})

# Edit Views
def edit_other_info(request, pk):
    other_info = get_object_or_404(OtherInfo, pk=pk)
    if request.method == 'POST':
        form = OtherInfoForm(request.POST, request.FILES, instance=other_info)
        if form.is_valid():
            form.save()
            return redirect('list_details')
    else:
        form = OtherInfoForm(instance=other_info)
    return render(request, 'user/form.html', {'form': form, 'title': 'Edit Other Info'})

def edit_history(request, pk):
    history = get_object_or_404(History, pk=pk)
    if request.method == 'POST':
        form = HistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('list_details')
    else:
        form = HistoryForm(instance=history)
    return render(request, 'user/form.html', {'form': form, 'title': 'Edit Work History'})

def edit_achieve(request, pk):
    achieve = get_object_or_404(Achieve, pk=pk)
    if request.method == 'POST':
        form = AchieveForm(request.POST, request.FILES, instance=achieve)
        if form.is_valid():
            form.save()
            return redirect('list_details')
    else:
        form = AchieveForm(instance=achieve)
    return render(request, 'user/form.html', {'form': form, 'title': 'Edit Achievement'})

# Delete Views
def delete_other_info(request, pk):
    other_info = get_object_or_404(OtherInfo, pk=pk)
    if request.method == 'POST':
        other_info.delete()
        return redirect('list_details')
    return render(request, 'user/confirm_delete.html', {'object': other_info, 'title': 'Delete Other Info'})

def delete_history(request, pk):
    history = get_object_or_404(History, pk=pk)
    if request.method == 'POST':
        history.delete()
        return redirect('list_details')
    return render(request, 'user/confirm_delete.html', {'object': history, 'title': 'Delete Work History'})

def delete_achieve(request, pk):
    achieve = get_object_or_404(Achieve, pk=pk)
    if request.method == 'POST':
        achieve.delete()
        return redirect('list_details')
    return render(request, 'user/confirm_delete.html', {'object': achieve, 'title': 'Delete Achievement'})



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AlumniForm

def register(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = AlumniForm()
    return render(request, 'register.html', {'form': form})


from django.http import JsonResponse
from .models import Course

def load_courses(request):
    branch_id = request.GET.get('branch_id')
    courses = Course.objects.filter(branch_id=branch_id).order_by('name')
    return JsonResponse(list(courses.values('id', 'name')), safe=False)


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import EducationalBackground
from .forms import EducationalBackgroundForm

@login_required
def create_educational_background(request):
    if request.method == 'POST':
        form = EducationalBackgroundForm(request.POST)
        if form.is_valid():
            educational_background = form.save(commit=False)
            educational_background.alumni = request.user
            educational_background.save()
            return redirect('list_details')  # Update with the correct view name
    else:
        form = EducationalBackgroundForm()
    return render(request, 'user/create_edu_background.html', {'form': form, 'title': 'Add Educational Background'})


@login_required
def edit_educational_background(request):
    educational_background = get_object_or_404(EducationalBackground, alumni=request.user)
    
    if request.method == 'POST':
        form = EducationalBackgroundForm(request.POST, instance=educational_background)
        if form.is_valid():
            form.save()
            return redirect('list_details')  # Update with the correct view name
    else:
        form = EducationalBackgroundForm(instance=educational_background)
    return render(request, 'user/edit_edu_background.html', {'form': form, 'title': 'Edit Educational Background'})


# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AlumniEditForm
from .models import Alumni

@login_required
def edit_alumni_profile(request):
    alumni = request.user
    if request.method == 'POST':
        form = AlumniEditForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page or any other page
    else:
        form = AlumniEditForm(instance=alumni)
    return render(request, 'user/edit_alumni.html', {'form': form, 'title': 'Edit Profile'})
