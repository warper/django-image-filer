# Only used to keep the next "useful" migration as 0003.
# Older migration data was dropped and contained 2 migrations incl. initial.
from south.db import db
from django.db import models
from image_filer.models import *

class Migration:
    def forwards(self, orm):
        pass
    def backwards(self, orm):
        pass
    complete_apps = ['image_filer']
