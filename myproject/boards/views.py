from django.shortcuts import render,get_object_or_404,redirect
from .models import Board
from django.http import Http404
from django.contrib.auth.models import User
from .models import Board,Topic,Post
from .forms import NewTopicForm
# Create your views here.

def home(request):
    boards=Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def board_topics(request,pk):
    board=get_object_or_404(Board,pk=pk)
    return render(request,'topics.html',{'board':board})

def new_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
    user=User.objects.first() #get currently logged in users
    if request.method=='POST':
        form=NewTopicForm(request.POST)  #instantiate a form instance passing the POST data to the form
        if form.is_valid():
            topic=form.save(commit=False)
            """    
                This save() method accepts an optional commit keyword argument, which accepts either True or False.
                If you call save() with commit=False, then it will return an object that hasn’t yet been saved to the
                database. In this case, it’s up to you to call save() on the resulting model instance. This is useful 
                if you want to do custom processing on the object before saving it, or if you want to use one of the 
                specialized model saving options. commit is True by default.
            """
            #HERE if we haven't commited false we couldn't have beeen able to update topics field
            topic.board=board
            topic.starter=user
            topic.save()
            post=Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=user,
                topic=topic
            )
            return redirect('board_topics',pk=board.pk) #edirect to the created topic page
    else:
        form=NewTopicForm()
    return render(request,'new_topic.html',{'board':board,'form':form})
