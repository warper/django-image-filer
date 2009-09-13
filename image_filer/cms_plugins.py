from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from image_filer.models import ImagePublication, FolderPublication

class ImagePlugin(CMSPluginBase):
    model = ImagePublication
    name = _("Image from Image Filer")
    render_template = "image_filer/image.html"
    text_enabled = True
    #change_form_template = 'admin/image_filer/cms/image_plugin/change_form.html'
    raw_id_fields = ('image',)
    
    def render(self, context, instance, placeholder):
        return {'image_publication':instance, 'placeholder':placeholder}
    def icon_src(self, instance):
        return instance.image.file.extra_thumbnails['admin_tiny_icon']
plugin_pool.register_plugin(ImagePlugin)

class ImageFolderPlugin(CMSPluginBase):
    model = FolderPublication
    name = _("Image Folder from Filer")
    render_template = "image_filer/folder.html"
    text_enabled = True
    #change_form_template = 'admin/image_filer/cms/image_plugin/change_form.html'
    raw_id_fields = ('folder',)
    
    def render(self, context, instance, placeholder):
        context.dicts.append({'image_folder_publication':instance, 'placeholder':placeholder})
        return context
    def icon_src(self, instance):
        return "(none)"
plugin_pool.register_plugin(ImageFolderPlugin)

class FolderSlideshowPlugin(ImageFolderPlugin):
    name = _("Slideshow of image folder")
    class Meta:
        proxy = True
    render_template = "image_filer/slideshow2.html"
plugin_pool.register_plugin(FolderSlideshowPlugin)
