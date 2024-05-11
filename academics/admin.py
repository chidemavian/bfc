__author__ = 'yusuf'

from django.contrib import admin
from bfc.academics.models import *


admin.site.register([StudentAcademicRecord, PsychomotorSkill, AffectiveSkill, SubjectScore])
