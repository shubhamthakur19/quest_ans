# Generated by Django 3.2.3 on 2022-01-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20220128_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question_sets',
            name='section',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correct_ans',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questions',
            name='explanation',
            field=models.TextField(max_length=250),
        ),
    ]
