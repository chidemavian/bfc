from django.contrib import admin
from bfc.lesson.models import *

admin.site.register([tbltopic, 
	tblcontents,
	tblir, 
	tblobjectives,
	tblteachersActivities,
	tblstudentActivities,
	tblevaluation])
