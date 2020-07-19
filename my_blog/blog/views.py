from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Author
from .forms import ArticleForm, CreateUserForm, AuthorForm
from .decorators import role_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'blog/dashboard.html', context)

@login_required(login_url='login')
def AuthorList(request):
    article = Article.objects.all()
    
    context = {'article': article}
    return render(request, 'blog/authorlist.html', context)

# @login_required(login_url='login')
# def createAuthor(request):
#     author = Author.objects.all()
#     form = AuthorForm()
        
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('createblog')
    
#     context = {'author': author, 'form': form}
#     return render(request, 'blog/authorinfo.html', context)

@login_required(login_url='login')
def createArticle(request):
    article = Article.objects.all()
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showblog')            

    context = {'article': article, 'form': form}
    return render(request, 'blog/createblog.html', context)

@login_required(login_url='login')
def readArticle(request, pk):   
    article = Article.objects.get(id=pk)

    context = {'article': article}
    return render(request, 'blog/readblog.html', context)

@login_required(login_url='login')
def showArticle(request):
    article = Article.objects.all()   
    context = {'article': article}
    return render(request, 'blog/blogs.html', context)

@login_required(login_url='login')
@role_required(allowed_roles=['admin'])
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('showblog') 

    context = {'form': form}
    return render(request, 'blog/updateblog.html', context)

@login_required(login_url='login')
@role_required(allowed_roles=['admin'])
def deleteArticle(request, pk):    
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('showblog') 

    context = {'article': article}
    return render(request, 'blog/deleteblog.html', context)


def Login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'blog/Login.html', context)  

def Logout(request):
	logout(request)
	return redirect('login')


def Signup(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'blog/Signup.html', context)  
