# Generated by Django 5.0.2 on 2024-02-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('API', 'API'), ('FULL STACK', 'FULL STACK')], default='API', max_length=255),
        ),
    ]
