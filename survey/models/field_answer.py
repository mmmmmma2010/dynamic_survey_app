from django.db import models
from survey.models import SectionField, SurveyResponse

class FieldAnswer(models.Model):
    section_field = models.ForeignKey(SectionField, on_delete=models.CASCADE)
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer
