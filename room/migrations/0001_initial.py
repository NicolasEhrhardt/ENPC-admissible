# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'room_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('maxPeople', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'room', ['Room'])

        # Adding model 'Slot'
        db.create_table(u'room_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Room'])),
            ('serie', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'room', ['Slot'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'room_room')

        # Deleting model 'Slot'
        db.delete_table(u'room_slot')


    models = {
        u'room.room': {
            'Meta': {'object_name': 'Room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxPeople': ('django.db.models.fields.IntegerField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'room.slot': {
            'Meta': {'object_name': 'Slot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Room']"}),
            'serie': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['room']