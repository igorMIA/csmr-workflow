# Generated by Django 2.2.4 on 2019-09-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_workflow_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='corroborating_question',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='type',
            field=models.CharField(choices=[('without evidence url workflow', 'without evidence url workflow'), ('evidence url input workflow', 'evidence url input workflow'), ('evidence urls judgment workflow', 'evidence urls judgment workflow')], default='without evidence url workflow', max_length=255),
        ),
    ]
