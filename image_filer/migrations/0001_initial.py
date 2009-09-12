
from south.db import db
from django.db import models
from image_filer.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ImagePublication'
        db.create_table('cmsplugin_filer', (
            ('cmsplugin_ptr', orm['image_filer.ImagePublication:cmsplugin_ptr']),
            ('image', orm['image_filer.ImagePublication:image']),
            ('alt_text', orm['image_filer.ImagePublication:alt_text']),
            ('caption', orm['image_filer.ImagePublication:caption']),
            ('width', orm['image_filer.ImagePublication:width']),
            ('height', orm['image_filer.ImagePublication:height']),
            ('show_author', orm['image_filer.ImagePublication:show_author']),
            ('show_copyright', orm['image_filer.ImagePublication:show_copyright']),
        ))
        db.send_create_signal('image_filer', ['ImagePublication'])
        
        # Adding model 'Folder'
        db.create_table('image_filer_folder', (
            ('id', orm['image_filer.Folder:id']),
            ('parent', orm['image_filer.Folder:parent']),
            ('name', orm['image_filer.Folder:name']),
            ('owner', orm['image_filer.Folder:owner']),
            ('uploaded_at', orm['image_filer.Folder:uploaded_at']),
            ('created_at', orm['image_filer.Folder:created_at']),
            ('modified_at', orm['image_filer.Folder:modified_at']),
            ('lft', orm['image_filer.Folder:lft']),
            ('rght', orm['image_filer.Folder:rght']),
            ('tree_id', orm['image_filer.Folder:tree_id']),
            ('level', orm['image_filer.Folder:level']),
        ))
        db.send_create_signal('image_filer', ['Folder'])
        
        # Adding model 'FolderPermission'
        db.create_table('image_filer_folderpermission', (
            ('id', orm['image_filer.FolderPermission:id']),
            ('folder', orm['image_filer.FolderPermission:folder']),
            ('type', orm['image_filer.FolderPermission:type']),
            ('user', orm['image_filer.FolderPermission:user']),
            ('group', orm['image_filer.FolderPermission:group']),
            ('everybody', orm['image_filer.FolderPermission:everybody']),
            ('can_edit', orm['image_filer.FolderPermission:can_edit']),
            ('can_read', orm['image_filer.FolderPermission:can_read']),
            ('can_add_children', orm['image_filer.FolderPermission:can_add_children']),
        ))
        db.send_create_signal('image_filer', ['FolderPermission'])
        
        # Adding model 'Image'
        db.create_table('image_filer_image', (
            ('id', orm['image_filer.Image:id']),
            ('folder', orm['image_filer.Image:folder']),
            ('original_filename', orm['image_filer.Image:original_filename']),
            ('name', orm['image_filer.Image:name']),
            ('owner', orm['image_filer.Image:owner']),
            ('uploaded_at', orm['image_filer.Image:uploaded_at']),
            ('modified_at', orm['image_filer.Image:modified_at']),
            ('file', orm['image_filer.Image:file']),
            ('_height_field', orm['image_filer.Image:_height_field']),
            ('_width_field', orm['image_filer.Image:_width_field']),
            ('date_taken', orm['image_filer.Image:date_taken']),
            ('contact', orm['image_filer.Image:contact']),
            ('default_alt_text', orm['image_filer.Image:default_alt_text']),
            ('default_caption', orm['image_filer.Image:default_caption']),
            ('author', orm['image_filer.Image:author']),
            ('must_always_publish_author_credit', orm['image_filer.Image:must_always_publish_author_credit']),
            ('must_always_publish_copyright', orm['image_filer.Image:must_always_publish_copyright']),
            ('can_use_for_web', orm['image_filer.Image:can_use_for_web']),
            ('can_use_for_print', orm['image_filer.Image:can_use_for_print']),
            ('can_use_for_teaching', orm['image_filer.Image:can_use_for_teaching']),
            ('can_use_for_research', orm['image_filer.Image:can_use_for_research']),
            ('can_use_for_private_use', orm['image_filer.Image:can_use_for_private_use']),
            ('usage_restriction_notes', orm['image_filer.Image:usage_restriction_notes']),
            ('notes', orm['image_filer.Image:notes']),
            ('has_all_mandatory_data', orm['image_filer.Image:has_all_mandatory_data']),
        ))
        db.send_create_signal('image_filer', ['Image'])
        
        # Adding model 'Clipboard'
        db.create_table('image_filer_clipboard', (
            ('id', orm['image_filer.Clipboard:id']),
            ('user', orm['image_filer.Clipboard:user']),
        ))
        db.send_create_signal('image_filer', ['Clipboard'])
        
        # Adding model 'ClipboardItem'
        db.create_table('image_filer_clipboarditem', (
            ('id', orm['image_filer.ClipboardItem:id']),
            ('file', orm['image_filer.ClipboardItem:file']),
            ('clipboard', orm['image_filer.ClipboardItem:clipboard']),
            ('is_checked', orm['image_filer.ClipboardItem:is_checked']),
        ))
        db.send_create_signal('image_filer', ['ClipboardItem'])
        
        # Creating unique_together for [parent, name] on Folder.
        db.create_unique('image_filer_folder', ['parent_id', 'name'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [parent, name] on Folder.
        db.delete_unique('image_filer_folder', ['parent_id', 'name'])
        
        # Deleting model 'ImagePublication'
        db.delete_table('cmsplugin_filer')
        
        # Deleting model 'Folder'
        db.delete_table('image_filer_folder')
        
        # Deleting model 'FolderPermission'
        db.delete_table('image_filer_folderpermission')
        
        # Deleting model 'Image'
        db.delete_table('image_filer_image')
        
        # Deleting model 'Clipboard'
        db.delete_table('image_filer_clipboard')
        
        # Deleting model 'ClipboardItem'
        db.delete_table('image_filer_clipboarditem')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cms.cmsplugin': {
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'image_filer.clipboard': {
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['image_filer.Image']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clipboards'", 'to': "orm['auth.User']"})
        },
        'image_filer.clipboarditem': {
            'clipboard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Clipboard']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'image_filer.folder': {
            'Meta': {'unique_together': "(('parent', 'name'),)"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_folders'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'image_filer.folderpermission': {
            'can_add_children': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_edit': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_read': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'everybody': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Folder']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'image_filer.image': {
            '_height_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_use_for_print': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_private_use': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_research': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_teaching': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_web': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_of_files'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('thumbnail_fields.ImageWithThumbnailsField', [], {'width_field': "'_width_field'", 'height_field': "'_height_field'", 'extra_thumbnails': "{'admin_clipboard_icon':{'size':(32,32),'options':['crop','upscale']},'admin_sidebar_preview':{'size':(210,210),'options':['crop',]},'admin_directory_listing_icon':{'size':(48,48),'options':['crop','upscale']},'admin_tiny_icon':{'size':(32,32),'options':['crop','upscale']},}", 'blank': 'True', 'null': 'True', 'thumbnail': "{'size':(50,50)}"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_files'", 'blank': 'True', 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_images'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'usage_restriction_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'image_filer.imagepublication': {
            'Meta': {'db_table': "'cmsplugin_filer'"},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('ImageFilerModelImageField', [], {}),
            'show_author': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'show_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['image_filer']
