from django.shortcuts import render
from django.http import HttpResponse, request
from django.http.response import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from .models import Post, EnewsPaper, Nuser, EnewsPaper02, EnewsPaper03, EnewsPaper04, ENewsUpload, Developer, tinytest, Education, Business, Sports, Entertainment, Science, LifeStyle, Comics, Cartoons, Jobs, Opinions, International, Circulation, Advertisement
from .forms import ProductForm, RegisterUserForm, UserForm, Userform, UserLoginForm, tinyFormTest, ImageFileUploadForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
	all_post = Post.objects.all()

	for post in all_post:
		print(post.title)
		print(post.description)
	return render(request, 'index.html', {'all_post_list': all_post})

def post_list(request):
	post_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		post_list = post_list.filter(title=query)

	return render(request, 'post_list.html', {'post_list': post_list})

def single_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	print(post)

	return render(request, 'single_post.html', {'post': post})

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
		rform = UserForm()

	context = {
		'form':form,
		'regiform':rform
	}
	return render(request, 'product_create.html', context)

def userRegistration(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UserForm()

	context = {
		'form':form,
		'regiform': form,
	}
	return render(request, 'registration.html', context)


def userReg(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UserForm()

		context = {
			'form':form,

		}
		return render(request, 'registration.html', context)

# TheENews shows easily runs program
def eNewsView(request):
	allNewsInPage = EnewsPaper.objects.all()

	for eNewsView in allNewsInPage:
		print(eNewsView.date)
		print(eNewsView.pageNumber)
		print(eNewsView.position0)
		print(eNewsView.position1)
		print(eNewsView.position2)
		print(eNewsView.position3)
		print(eNewsView.position4)
		print(eNewsView.position5)
		print(eNewsView.position6)
		print(eNewsView.position7)
		print(eNewsView.position8)
		print(eNewsView.position9)
	return render(request, 'eachNewsDiffer.html', {'eachNews': allNewsInPage})

def eachNews(request):
	eachNews = EnewsPaper.objects.all()
	return render(request, 'eNewsPaperHome.html', {'eachNews': eachNews})

def eachNews02(request):
	eachNews = EnewsPaper02.objects.all()
	return render(request, 'eNewsPaperHome.html', {'eachNews': eachNews})

def eachNews03(request):
	eachNews = EnewsPaper03.objects.all()
	return render(request, 'eNewsPaperHome.html', {'eachNews': eachNews})

def eachNews04(request):
	eachNews = EnewsPaper04.objects.all()
	return render(request, 'eNewsPaperHome.html', {'eachNews': eachNews})

#New querry for uploading posts/images & showing by category
def ENewsUploadView(request):
	allENewsInPage = ENewsUpload.objects.all()

	for ENewsUploadView in allENewsInPage:
		print(ENewsUploadView.date)
		print(ENewsUploadView.pageNumber)
		print(ENewsUploadView.position)
		print(ENewsUploadView.category)
		print(ENewsUploadView.news)
	return render(request, 'eNewsDiffer.html', {'singleNews': allENewsInPage})

def eNews(request):
	queryDate = request.GET.get("date")
	queryPage = request.GET.get("p")
	singleNews = ENewsUpload.objects.filter(date=queryDate) | ENewsUpload.objects.filter(pageNumber=queryPage)
	dictionary = {
		'singleNews': singleNews
	}
	return render(request, 'eNewsToday.html', dictionary)

def specific(request):
	# queryCat = request.GET.get("cat")
	queryCat = "education"
	specify = ENewsUpload.objects.filter(category=queryCat)
	return render(request, 'specify.html', {'newsSpecific': specify, 'name':"Joy"})

#User Registration Request
class RegisterUserView(CreateView):
	form_class = RegisterUserForm
	template_name = "templates/registration.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseForbidden()
		
		return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		return HttpResponse('User registered')

def Registration(request):
	if request.method=='POST':
		form1 = Userform(request.POST)

		if form1.is_valid():
			username = form1.cleaned_data['username']
			first_name = form1.cleaned_data['first_name']
			last_name = form1.cleaned_data['last_name']
			email = form1.cleaned_data['email']
			password = form1.cleaned_data['password']
			User.objects.create_user(username = username, first_name=first_name, last_name=last_name, email=email, password=password)
			#sending mail information
			subject = 'New Account Confirmation Message'
			message = 'Hello Dear, congratulations for being our new member ! Welcome to the SoftTech Bangladesh !'
			from_email = settings.EMAIL_HOST_USER
			to_list = [from_email, 'joy.srijon@gmail.com']
			send_mail(subject,message,from_email,to_list,fail_silently=True)

			return HttpResponseRedirect('/home/e_news/')
	else:
		form1 = Userform()
	return render(request, 'registration.html', {'frm' : form1})

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect('/home/post_list')

	return render(request, "login.html", {"loginForm":form})

# ajax using registration
def home(request):
	form = tinyFormTest()
	if request.is_ajax():
		form = tinyFormTest(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			data = {
			'message':'form is saved'
			}
			return JsonResponse(data)
	context = {
	'form':form,
	}
	return render(request,'form.html',context)

def django_image_and_file_upload_ajax(request):
	if request.method == 'POST':
		form = ImageFileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': form.errors})
	else:
		form = ImageFileUploadForm()
		return render(request, 'django_image_upload_ajax.html', {'form': form})

def developerView(request):
	devInfo = Developer.objects.all()
	return render(request, 'developer.html', {'devInfo':devInfo})

def aboutView(request):

	return render(request, 'about.html')

def contactView(request):
	return render(request, 'contact.html')

def educationView(request):
	catNews = Education.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def businessView(request):
	catNews = Business.objects.all()
	numB = catNews.count()
	return render(request, 'categoryAll.html', {'catNews': catNews, 'num':numB})

def sportsView(request):
	catNews = Sports.objects.all()
	# numB = businessView()
	# allnum = Sports.objects.filter()
	num = catNews.count()
	return render(request, 'categoryAll.html', {'catNews': catNews, 'num':num})

def entertainmentView(request):
	catNews = Entertainment.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def scienceView(request):
	catNews = Science.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def lifestyleView(request):
	catNews = LifeStyle.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def comicsView(request):
	catNews = Comics.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def cartoonView(request):
	catNews = Cartoons.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def jobsView(request):
	catNews = Jobs.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def opinionView(request):
	catNews = Opinions.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def internationalView(request):
	catNews = International.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def circulationView(request):
	catNews = Circulation.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})

def advertisementView(request):
	catNews = Advertisement.objects.all()
	return render(request, 'categoryAll.html', {'catNews': catNews})
