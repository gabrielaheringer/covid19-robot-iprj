# Generated by Django 3.0.5 on 2020-09-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0008_auto_20200901_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avisoporemail',
            name='autor',
            field=models.TextField(blank=True, null=True),
        ),
    ]
