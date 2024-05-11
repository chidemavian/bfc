# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'setup_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('ca', self.gf('django.db.models.fields.FloatField')()),
            ('exam', self.gf('django.db.models.fields.FloatField')()),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('category2', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('status', self.gf('django.db.models.fields.CharField')(default='INACTIVE', max_length=25, null=True)),
        ))
        db.send_create_signal(u'setup', ['Subject'])

        # Adding model 'Class'
        db.create_table(u'setup_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
        ))
        db.send_create_signal(u'setup', ['Class'])

        # Adding model 'Arm'
        db.create_table(u'setup_arm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('arm', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
        ))
        db.send_create_signal(u'setup', ['Arm'])

        # Adding model 'Subject_group'
        db.create_table(u'setup_subject_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_group', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'setup', ['Subject_group'])

        # Adding model 'Role'
        db.create_table(u'setup_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'setup', ['Role'])

        # Adding model 'Department'
        db.create_table(u'setup_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'setup', ['Department'])

        # Adding model 'House'
        db.create_table(u'setup_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'setup', ['House'])

        # Adding model 'School'
        db.create_table(u'setup_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phonenumber', self.gf('django.db.models.fields.CharField')(max_length=65, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(default='img/noimage.jpeg', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'setup', ['School'])

        # Adding model 'LGA'
        db.create_table(u'setup_lga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('lga', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'setup', ['LGA'])

        # Adding model 'subclass'
        db.create_table(u'setup_subclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('classsub', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'setup', ['subclass'])

        # Adding model 'gradingsys'
        db.create_table(u'setup_gradingsys', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classsub', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'setup', ['gradingsys'])

        # Adding model 'appused'
        db.create_table(u'setup_appused', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('secondary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'setup', ['appused'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'setup_subject')

        # Deleting model 'Class'
        db.delete_table(u'setup_class')

        # Deleting model 'Arm'
        db.delete_table(u'setup_arm')

        # Deleting model 'Subject_group'
        db.delete_table(u'setup_subject_group')

        # Deleting model 'Role'
        db.delete_table(u'setup_role')

        # Deleting model 'Department'
        db.delete_table(u'setup_department')

        # Deleting model 'House'
        db.delete_table(u'setup_house')

        # Deleting model 'School'
        db.delete_table(u'setup_school')

        # Deleting model 'LGA'
        db.delete_table(u'setup_lga')

        # Deleting model 'subclass'
        db.delete_table(u'setup_subclass')

        # Deleting model 'gradingsys'
        db.delete_table(u'setup_gradingsys')

        # Deleting model 'appused'
        db.delete_table(u'setup_appused')


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