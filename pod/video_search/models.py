from pod.video_search.utils import index_es, delete_es
from pod.video.models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save


# do it  with contributor, overlay, chapter etc.
@receiver(post_save, sender=Video)
def update_video_index(sender, instance=None, created=False, **kwargs):
    if instance.is_draft == False:
        index_es(instance)
    else:
        delete_es(instance)