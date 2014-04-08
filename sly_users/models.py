from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female')
	)
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
	user = models.OneToOneField(User)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	phone_number = models.CharField(max_length=11)
	school = models.CharField(max_length=150)
	major = models.CharField(max_length=150)
	minor = models.CharField(max_length=150)
	graduating_class = models.IntegerField(max_length=4)
	alumni_status = models.BooleanField(default=False)
	state_program = models.CharField(max_length=2, choices=STATE_CHOICES)

	class Meta(object):
		ordering = ('user__username',)

	def __unicode__(self):
		return U'%s' %(self.user.username)
