from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class KategoriLowongan(models.Model):
	name = models.CharField(max_length=255)
	is_publish = models.BooleanField(default=False)

	class Meta:
		permissions = [
			('only_admin',"Can Kategori")
		]

class LocationLowongan(models.Model):
	name = models.CharField(max_length=255)
	is_publish = models.BooleanField(default=False)
	class Meta:
		permissions = [
			('only_admin',"Can Location")
		]

class Education(models.Model):
	name = models.CharField(max_length=100)
	is_publish = models.BooleanField(default=False)
	class Meta:
		permissions = [
			('only_admin',"Can Education")
		]




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
	unique_token = models.TextField(unique=True)
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
	photo_formal = models.TextField(null=True)
	file_cv = models.TextField(null=True)
	linkedln = models.TextField(null=True)
	website = models.TextField(null=True)
	is_admin = models.BooleanField(default=False)
	is_verify = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['no_telp']

	objects = UserManager()


class Lowongan(models.Model):
	title = models.CharField(max_length=255)
	category = models.ForeignKey(KategoriLowongan,on_delete=models.CASCADE)
	location = models.ForeignKey(LocationLowongan,on_delete=models.CASCADE)
	description = models.TextField()
	max_apply = models.IntegerField()
	number_recruits = models.IntegerField()
	salary = models.CharField(max_length=255)
	is_salary = models.BooleanField(default=False)
	is_apply = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		permissions = [
			('only_admin',"Can Lowongan")
		]


class ProfilePerusahaan(models.Model):
	tentang = models.TextField()
	about = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	web = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=12)
	address = models.TextField()
	images = models.TextField(null=True)

	class Meta:
		permissions = [
			('only_admin',"Can Profile Company")
		]



class ActivationAccount(models.Model):
	token = models.TextField()
	user = models.OneToOneField(Pengguna,on_delete=models.CASCADE,primary_key=True)


class ApplyLowongan(models.Model):
	to = models.ForeignKey(Lowongan,on_delete=models.CASCADE,related_name='data_lowongan')
	user = models.ForeignKey(Pengguna,on_delete=models.CASCADE,related_name='user_apply')
	status = models.IntegerField(default=1)
	is_closed = models.BooleanField(default=False)
	accept = models.BooleanField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		permissions = [
			('only_user',"Can Apply")
		]

class Notification(models.Model):
	readed = models.BooleanField(default=False)
	send_form = models.ForeignKey(Pengguna,on_delete=models.CASCADE,related_name='send_from_notifications')
	accept_to = models.ForeignKey(Pengguna,on_delete=models.CASCADE,related_name='accepted_to_notifications')
	subject = models.TextField()
	message = models.TextField()

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

