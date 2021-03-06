from django.contrib import admin
from faculty.models import Faculty_Time_Table
from general.models import Faculty

# Register your models here.

class TimeTableInLine(admin.TabularInline):
	model = Faculty_Time_Table
	extra = 1

class FacultyAdmin(admin.ModelAdmin):
	inlines = [TimeTableInLine]
	list_display = ('user', 'activation_key_expired','verified')

admin.site.register(Faculty, FacultyAdmin)

