from django.db import models

# Create your models here.


class Option(models.Model):
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option


class Questions(models.Model):
    option = models.ManyToManyField(Option)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    correct_ans = models.CharField(max_length=50)
    explanation = models.TextField(max_length=250)

    def __str__(self):
        return self.text


class Question_Sets(models.Model):
    question = models.ManyToManyField(Questions)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.section
