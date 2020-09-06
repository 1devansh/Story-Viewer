from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count, F, Value
from django.utils import timezone
# Create your views here.


def home(request):
  count = User.objects.count()
  all_users = User.objects.all()

  user_list=[]
  check = timezone.now() + timezone.timedelta(minutes=-5)
  
  for user in all_users:
    if user.last_login is None:
      user.last_login = timezone.now()
      
    if (user.last_login >= check) and (user.is_authenticated):
      user_list.append(user)
  
  stories = models.Stories.objects.all()
  D=[]
  for i in stories:
    title = i.title
    D.append(title)
  return render(request, 'home.html', {'count': count,'stories': D,'users':user_list})


def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form':form
  })



def story(request, title):

  stories = get_object_or_404(models.Stories, title=title)
  
  title = stories.title
  content = stories.content
  count = stories.view
  stories.view=count+1
  stories.save()
  
  return render(request, 'story.html', {'views':count+1, 'title': title, 'content': content})
