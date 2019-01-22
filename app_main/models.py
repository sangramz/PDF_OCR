from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    file_path = models.CharField(max_length=250, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)