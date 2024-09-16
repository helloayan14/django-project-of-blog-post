from django.shortcuts import render
from .models import Post
from .forms import Postform,UserRegistrationform
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')

def postlist(request):
    posts=Post.objects.all().order_by('post_date')
    return render(request,'postlist.html',{'posts':posts})

@login_required
def postcreate(request):
    if request.method=='POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('postlist')
    else:
        form=Postform()
   
    return render(request,'postform.html',{'form':form})
@login_required
def postedit(request,post_id):
    post=get_object_or_404(Post,pk=post_id,user=request.user)
    if request.method=='POST':
        form=Postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
           post=form.save(commit=False)
           post.user=request.user
           post.save()
           return redirect('postlist')
    else:
        form=Postform(instance=post)
   
    return render(request,'postform.html',{'form':form})
@login_required
def postdelete(request,post_id):
    post=get_object_or_404(Post,pk=post_id,user=request.user)
    if request.method=='POST':
        post.delete()
        return redirect("postlist")
    return render(request,'post_conf_del.html',{'post':post})


def Register(request):
    if request.method=="POST":
        form=UserRegistrationform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('postlist')

    else:
        form=UserRegistrationform()

    return render(request,'registration/register.html',{'form':form})