from django.db import models

class PythonFile(models.Model):
    file = models.FileField(upload_to='python_files')
