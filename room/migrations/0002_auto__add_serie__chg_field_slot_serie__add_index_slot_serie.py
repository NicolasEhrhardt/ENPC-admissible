# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Serie'
        db.create_table(u'room_serie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serie', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'room', ['Serie'])


        # Renaming column for 'Slot.serie' to match new field type.
        db.rename_column(u'room_slot', 'serie', 'serie_id')
        # Changing field 'Slot.serie'
        db.alter_column(u'room_slot', 'serie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Serie']))
        # Adding index on 'Slot', fields ['serie']
        db.create_index(u'room_slot', ['serie_id'])


    def backwards(self, orm):
        # Removing index on 'Slot', fields ['serie']
        db.delete_index(u'room_slot', ['serie_id'])

        # Deleting model 'Serie'
        db.delete_table(u'room_serie')


        # Renaming column for 'Slot.serie' to match new field type.
        db.rename_column(u'room_slot', 'serie_id', 'serie')
        # Changing field 'Slot.serie'
        db.alter_column(u'room_slot', 'serie', self.gf('django.db.models.fields.IntegerField')())

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
            'serie': ('django.db.models.fields.IntegerField', [], {})
        },
        u'room.slot': {
            'Meta': {'object_name': 'Slot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Room']"}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Serie']"})
        }
    }

    complete_apps = ['room']