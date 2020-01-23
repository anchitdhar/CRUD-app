from django.db import models
from __future__ import unicorn_literals


class blog_posts(models.Model):
    title = models.CharField(max_length= 100)
    tag = models.CharField(max_length=40)
    author = models.CharField(max_length= 30)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit',kwargs ={'pk' : self.pk})

