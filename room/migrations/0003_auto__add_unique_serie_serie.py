# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Serie', fields ['serie']
        db.create_unique(u'room_serie', ['serie'])


    def backwards(self, orm):
        # Removing unique constraint on 'Serie', fields ['serie']
        db.delete_unique(u'room_serie', ['serie'])


    models = {
        u'room.room': {
            'Meta': {'object_name': 'Room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxPeople': ('django.db.models.fields.IntegerField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'series': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['room.Serie']", 'through': u"orm['room.Slot']", 'symmetrical': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'room.serie': {
            'Meta': {'object_name': 'Serie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serie': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'room.slot': {
            'Meta': {'object_name': 'Slot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Room']"}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Serie']"})
        }
    }

    complete_apps = ['room']