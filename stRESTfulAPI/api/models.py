from django.db import models

# Create your models here.
class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    video = models.FileField(upload_to='./')
    #Represent the user who created the code snippet + to store the highlighted HTML representation of the code
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']