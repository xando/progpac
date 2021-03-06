# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Level.script'
        db.add_column('core_level', 'script',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Level.script'
        db.delete_column('core_level', 'script')


    models = {
        'core.level': {
            'Meta': {'object_name': 'Level'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxsize': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'script': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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