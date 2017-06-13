from django.db import models

class PageView(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user_agent = models.TextField(default='unknown')
    ip = models.GenericIPAddressField()
    tag = models.CharField(max_length=140)


