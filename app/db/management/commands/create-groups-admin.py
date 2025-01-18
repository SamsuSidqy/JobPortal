from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission





class Command(BaseCommand):
	help = 'Buat Groups Untuk Permissions Users'
	def handle(self, *args, **options):
		permission = Permission.objects.all()
		print("Wait A Minute ....... || .....")
		for group in permission:
			new_group ,created = Group.objects.get_or_create(name='admin')
			try:				
				new_group.permissions.add(group)
			except Permission.DoesNotExist as e:
				self.stdout.write(self.style.ERROR(f'Permission "{e}" does not exist.'))

		self.stdout.write(self.style.SUCCESS('Groups and permissions setup completed.'))
