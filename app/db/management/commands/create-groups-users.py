from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


PERMISSIONS = [
	'Can view education',
	'Can view location lowongan',
	'Can view group',
	'Can view permission',
	'Can view content type',
	'Can view activation account',
	'Can view apply lowongan',
	'Can add apply lowongan',
	'Can view attachment notification',
	'Can view kategori lowongan',
	'Can view lowongan',
	'Can view notification',
	'Can change user',
	'Can view user',
	'Can add user',
	'Can view profile perusahaan',
	'Can view tipe lowongan',
	'Can view session',
]


class Command(BaseCommand):
	help = 'Buat Groups Untuk Permissions Users'
	def handle(self, *args, **options):
		for group in PERMISSIONS:
			print(group)
			new_group ,created = Group.objects.get_or_create(name='users')
			try:
				add_perms = Permission.objects.get(name=group)
				new_group.permissions.add(add_perms)
			except Permission.DoesNotExist as e:
				self.stdout.write(self.style.ERROR(f'Permission "{e}" does not exist.'))

		self.stdout.write(self.style.SUCCESS('Groups and permissions setup completed.'))