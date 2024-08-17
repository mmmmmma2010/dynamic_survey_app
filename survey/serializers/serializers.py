from rest_framework import serializers
from survey.models import Survey, Section, SectionField,SurveyResponse,FieldAnswer

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionField
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Section
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Survey
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldAnswer
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = '__all__'
