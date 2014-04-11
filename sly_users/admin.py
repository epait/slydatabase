from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from sly_users.models import Profile, Alumni, UserProgramYear


# Register your models here.
class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = "Profile"

class UserProgramYearInline(admin.StackedInline):
	model = UserProgramYear
	can_delete = False
	verbose_name_plural = "Program Year"

class AlumniInline(admin.StackedInline):
	model = Alumni
	can_delete = False
	verbose_name_plural = "Alumni"

class UserAdmin(UserAdmin):
	inlines = (ProfileInline, UserProgramYearInline, AlumniInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)