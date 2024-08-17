from django.db import models
from survey.models import Survey


class Section(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    display = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name