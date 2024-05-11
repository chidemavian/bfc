

from django.contrib import admin
from bfc.student.models import Student, WithdrawnStudent


admin.site.register([Student, WithdrawnStudent])
