from django.db import models

# Create your models here.
'''class person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)




class FAQ(models.Model):
	ques=models.CharField(max_length=30)
	an=models.CharField(max_length=30)
'''
class ContentCreator(models.Model):
	name=models.CharField(max_length=100)
	bio=models.TextField()
	website=models.URLField()
	image=models.ImageField(upload_to='contentcreators/',null=True,blank=True)
	def __str__(self):
		return self.name

class Blog(models.Model):
 	title=models.CharField(max_length=200)
 	content=models.TextField()
 	pub_date=models.DateTimeField('date published')
 	creator=models.ForeignKey(ContentCreator,on_delete=models.CASCADE,related_name='blogs')
 	image=models.ImageField(upload_to='blogs/',null=True,blank=True)
 	def __str__(self):
 		return self.title

class review(models.Model):
	title=models.CharField(max_length=200)
	message=models.TextField(max_length=1000)
	def __str__(self):
		return self.title

class contact(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)	
	email=models.EmailField(max_length=50)
	phone=models.CharField(max_length=20)
	message=models.TextField(max_length=500)
	def __str__(self):
		return self.first_name

class user_register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    age=models.CharField(max_length=50, blank=True, null=True)		
    bio=models.CharField(max_length=200, blank=True, null=True)		
    pincode=models.CharField(max_length=50, blank=True, null=True)		
    contact=models.CharField(max_length=20, blank=True, null=True)		
    dob=models.CharField(max_length=50, blank=True, null=True)		
    address=models.CharField(max_length=100, blank=True, null=True)	
    image=models.ImageField(upload_to="data",blank=True, null=True)	
    def __str__(self):
    	return self.name

class helpus(models.Model):
	heading=models.CharField(max_length=100)
	content=models.TextField(max_length=1000)
	def __str__(self):
		return self.heading

		