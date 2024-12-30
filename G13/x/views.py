from django.shortcuts import render
from .models import X
from .forms import XForm, UserRegisterForm 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.
def homeX(request):
  return render(request, 'index.html')


def tweet_list(request):
  tweets = X.objects.all().order_by('-created_at')
  return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
  if request.method == 'POST':
    form = XForm(request.POST, request.FILES)
    if form.is_valid():
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('tweet_list')
  else:
    form = XForm()
    
  return render(request, 'X_form.html', {'form': form})
    
@login_required   
def tweet_edit(request, tweet_id):
  tweet = get_object_or_404(X, pk=tweet_id, user=request.user)
  if request.method == 'POST':
    form = XForm(request.POST, request.FILES, instance=tweet)
    if(form.is_valid()):
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('tweet_list')
  else:
    form = XForm(instance=tweet)
  return render(request, 'x_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
  tweet = get_object_or_404(X, pk=tweet_id, user=request.user)
  if request.method == 'POST':
    tweet.delete()
    return redirect('tweet_list')
  return render(request, 'tweet_delete.html', {'tweet': tweet})


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit = False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('tweet_list')    
  else:
    form = UserRegisterForm()
  return render(request, 'registration/register.html', {'form': form})