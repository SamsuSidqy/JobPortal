from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from uuid import uuid4
from django.utils.text import slugify
from datetime import datetime,timedelta


class DisabeldForm(models.Model):
	education = models.BooleanField(default=False)
	kategori = models.BooleanField(default=False)
	location = models.BooleanField(default=False)
	tipe = models.BooleanField(default=False)
	
	class Meta:
		permissions = [
			('only_admin',"Can Kategori")
		]

class KategoriLowongan(models.Model):
	name = models.CharField(max_length=255,unique=True)

	class Meta:
		permissions = [
			('only_admin',"Can Kategori")
		]

	def __str__(self):
		return f"{self.name}"

class LocationLowongan(models.Model):
	name = models.CharField(max_length=255,unique=True)
	class Meta:
		permissions = [
			('only_admin',"Can Location")
		]

	def __str__(self):
		return f"{self.name}"

class Education(models.Model):
	name = models.CharField(max_length=100,unique=True)
	class Meta:
		permissions = [
			('only_admin',"Can Education")
		]

	def __str__(self):
		return f"{self.name}"

class TipeLowongan(models.Model):
	name = models.CharField(max_length=100,unique=True)
	class Meta:
		permissions = [
			('only_admin',"Can Education")
		]
		
	def __str__(self):
		return f"{self.name}"



class UserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('email is require')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,password,**extra_fields):
		extra_fields.setdefault('is_admin',True)
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_verify',True)
		return self.create_user(email, password, **extra_fields)

class Pengguna(AbstractUser):
	username = models.CharField(max_length=255,unique=True)
	unique_token = models.TextField(unique=True,default=uuid4())
	complete_name = models.CharField(max_length=255,null=True)
	email = models.EmailField(unique=True)
	password = models.TextField()
	no_telp = models.TextField(unique=True,max_length=12,null=True)
	profile = models.TextField(null=True),
	skills = models.TextField(null=True)
	date_birth = models.DateTimeField(null=True)
	last_education = models.ForeignKey(Education,on_delete=models.CASCADE,null=True)
	jurusan = models.CharField(max_length=255,null=True)
	about = models.TextField(null=True)
	photo_formal = models.TextField(blank=True,null=True)
	file_cv = models.TextField(blank=True,null=True)
	linkedln = models.TextField(null=True)
	website = models.TextField(null=True)
	is_admin = models.BooleanField(default=False)
	is_verify = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['no_telp']

	objects = UserManager()


	def save(self,*args,**kwargs):
		if self.id:
			oldEmail = Pengguna.objects.get(pk=self.id)	
			if oldEmail.email != self.email:
				self.is_verify = False
		super(Pengguna,self).save(*args,**kwargs)

class Lowongan(models.Model):
	title = models.CharField(max_length=255)
	category = models.ForeignKey(KategoriLowongan,on_delete=models.CASCADE)
	location = models.ForeignKey(LocationLowongan,on_delete=models.CASCADE)
	tipe = models.ForeignKey(TipeLowongan,on_delete=models.CASCADE)
	description = models.TextField()
	slug = models.TextField(null=True,blank=True)
	is_close = models.BooleanField(default=False)
	max_apply = models.IntegerField(null=True)
	salary = models.CharField(max_length=255)
	is_salary = models.BooleanField(default=False)
	is_apply = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		permissions = [
			('only_admin',"Can Lowongan")
		]

	def save(self):
		self.slug = slugify(self.title)		
		super(Lowongan,self).save()


class ProfilePerusahaan(models.Model):
	tentang = models.TextField()
	slogan = models.CharField(max_length=100,null=True)
	name = models.CharField(max_length=255)
	web = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=12)
	address = models.TextField()
	images = models.TextField(null=True,blank=True)

	class Meta:
		permissions = [
			('only_admin',"Can Profile Company")
		]



class ActivationAccount(models.Model):
	token = models.TextField()
	user = models.OneToOneField(Pengguna,on_delete=models.CASCADE,primary_key=True)
	expired_at = models.DateTimeField(default=datetime.now()+timedelta(hours=1))


class ApplyLowongan(models.Model):
	to = models.ForeignKey(Lowongan,on_delete=models.CASCADE,related_name='data_lowongan')
	user = models.ForeignKey(Pengguna,on_delete=models.CASCADE,related_name='user_apply')
	status = models.IntegerField(default=1)
	is_closed = models.BooleanField(default=False)
	unique_token = models.TextField(default=uuid4())
	date_interview = models.DateTimeField(blank=True,null=True)
	accept = models.BooleanField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		permissions = [
			('only_user',"Can Apply")
		]

class Notification(models.Model):
	readed = models.BooleanField(default=False)	
	aply = models.ForeignKey(ApplyLowongan,on_delete=models.CASCADE,related_name='applyment_to_notifications')
	accept_to = models.ForeignKey(Pengguna,on_delete=models.CASCADE,related_name='accepted_to_notifications')
	subject = models.TextField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		permissions = [
			('only_admin',"Can Notif")
		]

class AttachmentNotification(models.Model):
	name_file = models.TextField()
	notification = models.ForeignKey(Notification,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		permissions = [
			('only_admin',"Can Notif")
		]

