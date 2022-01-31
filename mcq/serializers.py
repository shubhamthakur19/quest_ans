# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Question_Sets, Questions, Option

# Create a model serializer


class OptionSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Option
        fields = '__all__'

    def validate(self, data):
        if data['option'] == "Abc":
            raise serializers.ValidationError({'error': "Option is wrong"})

        return data


class QuestionsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Questions
        fields = ('text', 'correct_ans', 'explanation')


class QuestionSetsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Question_Sets
        fields = '__all__'

    def validate(self, data):
        if len(data['section']) > 3:
            raise serializers.ValidationError(
                {'error': "Section size is greater than 3"})

        return data
