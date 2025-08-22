from django.db import models

# Create your models here.

class Process(models.Model):
    hostname = models.CharField(max_length=255)
    pid = models.IntegerField()
    ppid = models.IntegerField()  # parent process id
    name = models.CharField(max_length=255)
    cpu = models.FloatField()
    memory = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (PID: {self.pid}) on {self.hostname}"

