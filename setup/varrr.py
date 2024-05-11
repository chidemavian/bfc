from django.shortcuts import render_to_response, get_object_or_404
from django.http import  Http404, HttpResponseRedirect, HttpResponse
from django.core.serializers.json import json
from bfc.assessment.forms import *
from bfc.academics.models import *
from bfc.sysadmin.models import *
from bfc.setup.models import *
from bfc.assessment.getordinal import *
from bfc.assessment.utils import *
from bfc.assessment.bsheet import *
from bfc.utilities.views import *
from django.db.models import Max,Sum
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL,'')
import xlwt

currse = currentsession.objects.get(id = 1)

def sublists(varuser,session,klass):
    data = subjectteacher.objects.filter(teachername = varuser,session=session,klass = klass)
    for j in data:
        j = j.subject
        s = {j:j}
        sdic.update(s)
    kb = sdic.values()
    return kb
