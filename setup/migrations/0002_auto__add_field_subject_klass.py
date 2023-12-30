# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subject.klass'
        db.add_column(u'setup_subject', 'klass',
                      self.gf('django.db.models.fields.CharField')(default='SS', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Subject.klass'
        db.delete_column(u'setup_subject', 'klass')


    models = {
        u'setup.appused': {
            'Meta': {'object_name': 'appused'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'setup.arm': {
            'Meta': {'ordering': "['arm']", 'object_name': 'Arm'},
            'arm': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'setup.class': {
            'Meta': {'ordering': "['klass']", 'object_name': 'Class'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        u'setup.department': {
            'Meta': {'object_name': 'Department'},
            'department': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'setup.gradingsys': {
            'Meta': {'ordering': "['classsub', 'id']", 'object_name': 'gradingsys'},
            'classsub': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'setup.house': {
            'Meta': {'object_name': 'House'},
            'house': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'setup.lga': {
            'Meta': {'ordering': "['state', 'lga']", 'object_name': 'LGA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lga': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'setup.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        u'setup.school': {
            'Meta': {'ordering': "['id']", 'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "'img/noimage.jpeg'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'setup.subclass': {
            'Meta': {'object_name': 'subclass'},
            'classsub': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'setup.subject': {
            'Meta': {'ordering': "['category', 'subject']", 'object_name': 'Subject'},
            'ca': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'category2': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'exam': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.CharField', [], {'default': "'SS'", 'max_length': '75'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'INACTIVE'", 'max_length': '25', 'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'setup.subject_group': {
            'Meta': {'ordering': "['subject_group']", 'object_name': 'Subject_group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_group': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['setup']