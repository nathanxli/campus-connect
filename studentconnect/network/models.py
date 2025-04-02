from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Placeholder for now

    majors = models.CharField(max_length=200, help_text="Comma-separated if multiple")
    academic_interests = models.TextField(help_text="Comma-separated list")
    non_academic_interests = models.TextField(help_text="Comma-separated list")
    current_classes = models.TextField(help_text="Comma-separated list")

    connections = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username