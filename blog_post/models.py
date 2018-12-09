from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='imageNews', blank=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary		= models.TextField(blank=False, null=False)
	featured	= models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Newusers(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	occupation = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.email

class Nuser(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	occupation = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=30)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.email

class ENewsUpload(models.Model):
	date = models.CharField(max_length=50)
	pageChoice = (
		('page1', 'Page1'),
		('page2', 'Page2'),
		('page3', 'Page3'),
		('page4', 'Page4'),
		('page5', 'Page5'),
		('page6', 'Page6'),
		('page7', 'Page7'),
		('page8', 'Page8'),
	)
	pageNumber = models.CharField(max_length=100, choices=pageChoice)
	positionChoice = (
		('r0c0', 'Page Topper'),
		('r1c1', 'Row 1 Column 1'),
		('r1c2', 'Row 1 Column 2'),
		('r1c3', 'Row 1 Column 3'),
		('r2c1', 'Row 2 Column 1'),
		('r2c2', 'Row 2 Column 2'),
		('r2c3', 'Row 2 Column 3'),
		('r3c1', 'Row 3 Column 1'),
		('r3c2', 'Row 3 Column 2'),
		('r3c3', 'Row 3 Column 3'),
	)
	position = models.CharField(max_length=100, choices=positionChoice)
	categoryChoice = (
		('topper', 'Topper Page'),
		('education', 'Education'),
		('business', 'Business'),
		('sports', 'Sports'),
		('entertainment', 'Entertainment'),
		('science_technology', 'Science & Technology'),
		('lifestyle', 'Lifestyle'),
		('comics', 'Comics'),
		('cartoons', 'Cartoons'),
		('jobs', 'Jobs'),
		('opinions', 'Opinions'),
		('international', 'International'),
		('circulations', 'Circulations'),
		('advertisement', 'Advertisement'),
	)
	category = models.CharField(max_length=100, choices=categoryChoice)
	news = models.ImageField(upload_to='news', blank=True)

	def __str__(self):
		return self.date


class EnewsPaper(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position0 = models.ImageField(upload_to='row0column0', blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class EnewsPaper02(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position0 = models.ImageField(upload_to='row0column0', blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class EnewsPaper03(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position0 = models.ImageField(upload_to='row0column0', blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class EnewsPaper04(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position0 = models.ImageField(upload_to='row0column0', blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

#new ajax code using
class tinytest(models.Model):
	name  = models.CharField(max_length=120)
	email = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Developer(models.Model):
	name = models.CharField(max_length=120)
	photo = models.ImageField(upload_to='profile_image', blank=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	photo = models.ImageField(upload_to="images")
	attachment = models.FileField(upload_to="attachments")
	phone = models.CharField(max_length=10)

class Education(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Business(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Sports(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Entertainment(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Science(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class LifeStyle(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Comics(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Cartoons(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Jobs(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Opinions(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class International(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Circulation(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date

class Advertisement(models.Model):
	date = models.CharField(max_length=50)
	pageNumber = models.IntegerField(blank=True)
	position1 = models.ImageField(upload_to='row1column1', blank=True)
	position2 = models.ImageField(upload_to='row1column2', blank=True)
	position3 = models.ImageField(upload_to='row1column3', blank=True)
	position4 = models.ImageField(upload_to='row2column1', blank=True)
	position5 = models.ImageField(upload_to='row2column2', blank=True)
	position6 = models.ImageField(upload_to='row2column3', blank=True)
	position7 = models.ImageField(upload_to='row3column1', blank=True)
	position8 = models.ImageField(upload_to='row3column2', blank=True)
	position9 = models.ImageField(upload_to='row3column3', blank=True)

	def __str__(self):
		return self.date