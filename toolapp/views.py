from django.shortcuts import render,redirect
from toolapp.models import Blog
from toolapp.models import ContentCreator
from toolapp.models import review
from toolapp.models import contact
from toolapp.models import user_register
from toolapp.models import helpus
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		user=user_register.objects.filter(email=e, password=p)
		if len(user) >0:
			request.session['email'] = e
			return render(request,'myprofile.html')
		else:
			return render(request,'login.html',{'msg':"invalid candidate"})
	else:
		return render(request,'login.html')

def myprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	user=user_register.objects.get(email=request.session['email'])
	if request.method=="POST":
		print("yes")
		user.image=request.FILES['file1']
		user.save()
		return render(request,'myprofile.html',{'user':user,'msg':'success'})
	else:
		return render(request,'myprofile.html',{'user':user})


def register(request):
	if request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pass')
		c=request.POST.get('cpass')
		if user_register.objects.filter(email=e, password=p).exists():
			msg="Email Id is already exists"
			return render(request,'register.html',{'msg: msg'})
		else:
			if p == c:
				x=user_register()
				x.name=n
				x.email=e
				x.password=p
				x.save()
				msg="User successfully register"
				return render(request,'register.html',{'msg':msg})
			else:
				msg="Password and Confirm Password does'nt match"
				return render(request,'register.html',{'msg':msg})
	else:
		return render(request,'register.html')

def contactus(request):
	if request.method =="POST":
		x=contact()
		x.first_name=request.POST.get('fn')
		x.last_name=request.POST.get('ln')
		x.email=request.POST.get('em')
		x.phone=request.POST.get('ph')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'contactus.html',{'msg':1})
	else:
	    return render(request,'contactus.html')

def footer(request):
	return render(request,'footer.html')

def base(request):
    return render(request,'base.html')

def allblogs(request):
	res=Blog.objects.all()
	return render(request,'allblogs.html',{'data':res})


def allcontentcreators(request):
	res=ContentCreator.objects.all()
	return render(request,'allcontentcreators.html',{'data':res})

def detailblog(request,id):
	res=Blog.objects.get(id=id)
	print(res)
	return render(request,'detailblog.html',{'i':res})

def myreview(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method =="POST":
		x=review()
		x.title=request.POST.get('ti')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'review.html',{'msg':1})
	else:
	    return render(request,'review.html')

def sidebar(request):
    return render(request,'sidebar.html')  

def changepassword(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method=="POST":
		o=request.POST.get('op')
		n=request.POST.get('np')
		c=request.POST.get('cp')
		if n==c:
			user=user_register.objects.get(email=request.session['email'])
			p=user.password
			if p==o:
				user.password=n
				user.save()
				msg="Password Successfully Changed"
				return render(request,'changepassword.html',{'msg': msg})
			else:
				msg="Old Password doesn't match"
				return render(request,'changepassword.html',{'msg' : msg}) 
		else:
			msg="Password and Confirm Password is not same"
			return render(request,'changepassword.html',{'msg' : msg})
	else:
		return render(request,'changepassword.html') 


def help(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method =="POST":
		x=helpus()
		x.heading=request.POST.get('hd')
		x.content=request.POST.get('con')
		x.save()
		return render(request,'help.html',{'msg':1})
	else:
	    return render(request,'help.html')


def editprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	detail=user_register.objects.get(email=request.session['email'])
	if request.method=="POST":
		detail.name=request.POST.get('nm')
		detail.age=request.POST.get('age')
		detail.bio=request.POST.get('bio')
		detail.pincode=request.POST.get('pin')
		detail.contact=request.POST.get('cont')
		detail.DOB=request.POST.get('date')
		detail.address=request.POST.get('add')
		detail.save()
		print("Successfully edited")
		return redirect('/myprofile/')
	else:
		return render(request,'editprofile.html',{'i':detail}) 

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	del request.session['email']
	return redirect('/login/')

def forget(request):
	if (request.method=='POST'):
		em=request.POST.get('em')
		user=user_register.objects.filter(email=em)
		if(len(user)>0):
			password=user[0].password
			subject="Password"
			message="Welcome! Your password is"+password
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[em]
			send_mail(subject,message,email_from,recipient_list)
			res="Your password sent to your respective email account"
			return render(request,'forget.html',{'res':res})
		else:
			res='This Email Id is not registered'
			return render(request,'Forget.html',{'res':res})
	else:
		return render(request,'Forget.html')

