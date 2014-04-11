from django.db import models
from django.contrib.auth.models import User
import datetime


# Program List
ALABAMA = 'AL'
ALASKA = 'AK'
ARIZONA = 'AZ'
ARKANSAS = 'AR'
CALIFORNIA = 'CA'
COLORADO = 'CO'
CONNECTICUT = 'CT'
DELAWARE = 'DE'
FLORIDA = 'FL'
GEORGIA = 'GA'
HAWAII = 'HI'
IDAHO = 'ID'
ILLINOIS = 'IL'
INDIANA = 'IN'
IOWA = 'IA'
KANSAS = 'KS'
KENTUCKY = 'KY'
LOUISIANA = 'LA'
MAINE = 'ME'
MARYLAND = 'MD'
MASSACHUSETTS = 'MA'
MICHIGAN = 'MI'
MINNESOTA = 'MN'
MISSISSIPPI = 'MS'
MISSOURI = 'MO'
MONTANA = 'MT'
NEBRASKA = 'NE'
NEVADA = 'NV'
NEW_HAMPSHIRE = 'NH'
NEW_JERSEY = 'NJ'
NEW_MEXICO = 'NM'
NEW_YORK = 'NY'
NORTH_CAROLINA = 'NC'
NORTH_DAKOTA = 'ND'
OHIO = 'OH'
OKLAHOMA = 'OK'
OREGON = 'OR'
PENNSYLVANIA = 'PA'
RHODE_ISLAND = 'RI'
SOUTH_CAROLINA = 'SC'
SOUTH_DAKOTA = 'SD'
TENNESSEE = 'TN'
TEXAS = 'TX'
UTAH = 'UT'
VERMONT = 'VT'
VIRGINIA = 'VA'
WASHINGTON = 'WA'
WEST_VIRGINIA = 'WV'
WISCONSIN = 'WI'
WYOMING = 'WY'
COLLEGEYIG = 'CYIG'

STATE_CHOICES = (
	(ALABAMA, 'Alabama'),
	(ALASKA, 'Alaska'),
	(ARIZONA, 'Arizona'),
	(CALIFORNIA, 'Californa'),
	(COLORADO, 'Colorado'),
	(CONNECTICUT, 'Connecticut'),
	(DELAWARE, 'Delaware'),
	(FLORIDA, 'Florida'),
	(GEORGIA, 'Georgia'),
	(HAWAII, 'Hawaii'),
	(IDAHO, 'Idaho'),
	(ILLINOIS, 'Illinois'),
	(INDIANA, 'Indiana'),
	(IOWA, 'Iowa'),
	(KANSAS, 'Kansas'),
	(KENTUCKY, 'Kentucky'),
	(LOUISIANA, 'Louisiana'),
	(MAINE, 'Maine'),
	(MARYLAND, 'Maryland'),
	(MASSACHUSETTS, 'Massachusetts'),
	(MICHIGAN, 'Michigan'),
	(MINNESOTA, 'Minnesota'),
	(MISSISSIPPI, 'Mississippi'),
	(MISSOURI, 'Missouri'),
	(MONTANA, 'Montana'),
	(NEBRASKA, 'Nebraska'),
	(NEVADA, 'Nevada'),
	(NEW_HAMPSHIRE, 'New Hampshire'),
	(NEW_JERSEY, 'New Jersey'),
	(NEW_MEXICO, 'New Mexico'),
	(NEW_YORK, 'New York'),
	(NORTH_CAROLINA, 'North Carolina'),
	(NORTH_DAKOTA, 'North Dakota'),
	(OHIO, 'Ohio'),
	(OKLAHOMA, 'Oklahoma'),
	(OREGON, 'Oregon'),
	(PENNSYLVANIA, 'Pennsylvania'),
	(RHODE_ISLAND, 'Rhode Island'),
	(SOUTH_CAROLINA, 'South Carolina'),
	(SOUTH_DAKOTA, 'South Dakota'),
	(TENNESSEE, 'Tennessee'),
	(TEXAS, 'Texas'),
	(UTAH, 'Utah'),
	(VERMONT, 'Vermont'),
	(VIRGINIA, 'Virginia'),
	(WASHINGTON, 'Washington'),
	(WEST_VIRGINIA, 'West Virginia'),
	(WISCONSIN, 'Wisconsin'),
	(WYOMING, 'Wyoming'),
)

PROGRAM_CHOICES = (
	(COLLEGEYIG, 'College Youth In Government'),
	(FLORIDA, 'Florida'),
	(KENTUCKY, 'Kentucky'),
	(MARYLAND, 'Maryland'),
	(NEW_MEXICO, 'New Mexico'),
)


# Class Year Choices
SIXTH = '6'
SEVENTH = '8'
EIGHTH = '9'
FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
GRADE_CHOICES = (
	(SIXTH, '6th Grade'),
	(SEVENTH, '7th Grade'),
	(EIGHTH, '8th Grade'),
	(FRESHMAN, 'HS Freshman'),
	(SOPHOMORE, 'HS Sophomore'),
	(JUNIOR, 'HS Junior'),
	(SENIOR, 'HS Senior'),
)

# Gender choices
MALE = 'M'
FEMALE = 'F'
GENDER_CHOICES = (
	(MALE, 'Male'),
	(FEMALE, 'Female'),
)


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	current_program = models.ForeignKey('Program')
	chapter = models.ForeignKey('Chapter')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	phone_number = models.CharField(max_length=11)
	school = models.CharField(max_length=150)
	major = models.CharField(max_length=150, null=True, blank=True)
	minor = models.CharField(max_length=150, null=True, blank=True)
	grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=True, blank=True)
	graduating_class = models.IntegerField(max_length=4, null=True, blank=True)
	alumni_status = models.BooleanField(default=False, verbose_name='YIG Alumni?')

	def is_alumni(self):
		"Returns the user's alumni status"
		if self.alumni_status == True:
			return True
		else:
			return False

	def is_active(self):
		"Returns whether the user is active"
		# latest_program_year = self.user.program_year.program_year
		program_year_list = UserProgramYear.objects.filter(user=User.objects.get(username=self.user))
		latest_program_year = program_year_list.last().program_year
		# latest_year = latest_program_year.program_year.year.split('-')[1]
		# print latest_year
		if latest_program_year.is_current_year() == True:
			self.user.active = True
			self.user.save()
		else: 
			self.user.active = False
			self.user.save()

	class Meta(object):
		ordering = ('user__username',)

	def __unicode__(self):
		return U'%s' %(self.user.username)


class Alumni(models.Model):
	user = models.OneToOneField(User)
	state_program = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='High School Program', null=True, blank=True)
	cyig_alumni = models.BooleanField(default=False, verbose_name='College YIG Alumni?')
	occupation = models.CharField(max_length=150, null=True, blank=True)
	company = models.CharField(max_length=150, null=True, blank=True)
	current_city = models.CharField(max_length=150, null=True, blank=True)
	current_state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)

	class Meta(object):
		ordering = ('user__username',)

	def __unicode__(self):
		return U'%s' %(self.user.username)


class ProgramYear(models.Model):
	program = models.ForeignKey('Program')
	year = models.CharField(max_length=9, null=True, blank=True)

	def __unicode__(self):
		return U'%s %s' %(self.year, self.program)

	def is_current_year(self):
		"Returns whether or not a program year is the current year"
		y = self.year.split('-')
		d = datetime.date.today()
		if d.month < 8:
			if int(y[1]) == d.year:
				return True
			else:
				return False
		else:
			if int(y[0]) == d.year:
				return True
			else:
				return False

class UserProgramYear(models.Model):
	user = models.OneToOneField(User, related_name='program_year')
	program_year = models.ForeignKey('ProgramYear')
	dues_paid = models.BooleanField(default=False)
	attending_assembly = models.BooleanField(default=False, verbose_name='Planning to Attend Assembly?')

	def dues_paid_status(self):
		"Returns if the user's dues are paid"
		if self.dues_paid == True:
			return True
		else:
			return False

	def attending_assembly_status(self):
		"Returns if the user intends to attend Assembly"
		if self.attending_assembly == True:
			return True
		else:
			return False

	class Meta(object):
		ordering = ('user__username', 'program_year__year')

	def __unicode__(self):
		return U'%s %s' %(self.program_year.year, self.user.username)


class Chapter(models.Model):
	name = models.CharField(max_length=150)

	def __unicode__(self):
		return U'%s' %(self.name)


class Program(models.Model):
	name = models.CharField(max_length=4, choices=PROGRAM_CHOICES, primary_key=True)

	def __unicode__(self):
		return U'%s' %(self.name)


class Event(models.Model):
	name = models.CharField(max_length=150)
	host_program = models.ForeignKey('Program')

	def __unicode__(self):
		return U'%s' %(self.name)



