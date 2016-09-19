from __future__ import unicode_literals

from django.db import models

class Secrets(models.Model):
	secret = models.CharField(max_length=500)
	likes = models.IntegerField(blank=True, null=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)