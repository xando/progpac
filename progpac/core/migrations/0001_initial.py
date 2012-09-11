# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tier'
        db.create_table('core_tier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('core', ['Tier'])

        # Adding model 'Level'
        db.create_table('core_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Tier'])),
            ('hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('maxsize', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['Level'])

        # Adding model 'Result'
        db.create_table('core_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Level'])),
            ('program', self.gf('django.db.models.fields.TextField')()),
            ('program_length', self.gf('django.db.models.fields.IntegerField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('commited', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Tier'
        db.delete_table('core_tier')

        # Deleting model 'Level'
        db.delete_table('core_level')

        # Deleting model 'Result'
        db.delete_table('core_result')


    models = {
        'core.level': {
            'Meta': {'object_name': 'Level'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxsize': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'tier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Tier']"})
        },
        'core.result': {
            'Meta': {'object_name': 'Result'},
            'commited': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Level']"}),
            'program': ('django.db.models.fields.TextField', [], {}),
            'program_length': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        'core.tier': {
            'Meta': {'object_name': 'Tier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['core']