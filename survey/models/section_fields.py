from django.db import models
from survey.models import Section

class SectionField(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio'),
        ('select', 'Select'),
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    lable = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255, choices=TYPES,default=TYPES[0][0])
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.lable