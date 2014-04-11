from django.test import TestCase
from django.contrib.auth.models import User

import datetime

from sly_users.models import Profile, Program, Chapter, ProgramYear, UserProgramYear
# Create your tests here.


class test_user_statuses(TestCase):
	def setUp(self):
		"""Create Programs"""
		Program.objects.create(
			name="CYIG"
			)
		Program.objects.create(
			name="FL"
			)

		"""Create Chapters"""
		Chapter.objects.create(
			name="Dr. Phillips"
			)
		Chapter.objects.create(
			name="American University"
			)

		"""Create Users"""
		User.objects.create(username="delegate", 
			email="delegate@delegate.com", 
			password="adfsjafhreuifhfr"
			)
		User.objects.create(username="delegate_inactive", 
			email="delegate_inactive@delegate_inactive.com", 
			password="dpjofwhdhfkjshd"
			)
		User.objects.create(username="delegate_paid", 
			email="delegate_paid@delegate_paid.com", 
			password="jdsofjiuheirfjdeadjlk"
			)
		User.objects.create(username="delegate_attending_assembly", 
			email="delegate_attending_assembly@delegate_attending_assembly.com", 
			password="asdjfipoewqeljdfsoj"
			)
		User.objects.create(username="alumni", 
			email="alumni@alumni.com", 
			password="joieduiehfdskja"
			)
		
		"""Create Profiles"""
		Profile.objects.create(
			user=User.objects.get(username="delegate"), 
			current_program=Program.objects.get(name="FL"), 
			chapter=Chapter.objects.get(name="Dr. Phillips"), 
			alumni_status=False
			)
		Profile.objects.create(
			user=User.objects.get(username="delegate_inactive"), 
			current_program=Program.objects.get(name="FL"), 
			chapter=Chapter.objects.get(name="Dr. Phillips"), 
			alumni_status=True
			)
		Profile.objects.create(
			user=User.objects.get(username="alumni"), 
			current_program=Program.objects.get(name="CYIG"), 
			chapter=Chapter.objects.get(name="American University"), 
			alumni_status=True
			)

		"""Create Program Years"""
		ProgramYear.objects.create(program=Program.objects.get(name="FL"), year="2012-2013")
		ProgramYear.objects.create(program=Program.objects.get(name="FL"), year="2013-2014")

		"""Create User Program Years"""
		UserProgramYear.objects.create(
			user=User.objects.get(username="delegate"),
			program_year=ProgramYear.objects.get(program=Program.objects.get(name="FL"), year="2013-2014"),
			dues_paid=False,
			attending_assembly=False
			)
		UserProgramYear.objects.create(
			user=User.objects.get(username="delegate_inactive"),
			program_year=ProgramYear.objects.get(program=Program.objects.get(name="FL"), year="2012-2013"),
			dues_paid=False,
			attending_assembly=False
			)
		UserProgramYear.objects.create(
			user=User.objects.get(username="delegate_paid"),
			program_year=ProgramYear.objects.get(program=Program.objects.get(name="FL"), year="2013-2014"),
			dues_paid=True,
			attending_assembly=False
			)
		UserProgramYear.objects.create(
			user=User.objects.get(username="delegate_attending_assembly"),
			program_year=ProgramYear.objects.get(program=Program.objects.get(name="FL"), year="2013-2014"),
			dues_paid=True,
			attending_assembly=True
			)

	def test_user_alumni_status(self):
		"""Test Alumni Status"""
		delegate = User.objects.get(username="delegate")
		alumni = User.objects.get(username="alumni")
		self.assertEqual(delegate.profile.is_alumni(), False)
		self.assertEqual(alumni.profile.is_alumni(), True)

	def test_user_dues_paid_status(self):
		"""Test Dues Paid Status"""
		delegate = User.objects.get(username="delegate")
		delegate_paid = User.objects.get(username="delegate_paid")
		self.assertEqual(delegate.program_year.dues_paid_status(), False)
		self.assertEqual(delegate_paid.program_year.dues_paid_status(), True)

	def test_user_attending_assembly_status(self):
		"""Test Attending Assembly Status"""
		delegate = User.objects.get(username="delegate")
		delegate_attending_assembly = User.objects.get(username="delegate_attending_assembly")
		self.assertEqual(delegate.program_year.attending_assembly_status(), False)
		self.assertEqual(delegate_attending_assembly.program_year.attending_assembly_status(), True)

	def test_is_current_year(self):
		program_year = ProgramYear.objects.get(program=Program.objects.get(name="FL"), year="2013-2014")
		self.assertEqual(program_year.is_current_year(), True)

	def test_is_user_active(self):
		delegate = Profile.objects.get(user=User.objects.get(username='delegate'))
		delegate_inactive = Profile.objects.get(user=User.objects.get(username='delegate_inactive'))
		delegate.is_active()
		delegate_inactive.is_active()
		self.assertEqual(delegate.user.active, True)
		self.assertEqual(delegate_inactive.user.active, False)






