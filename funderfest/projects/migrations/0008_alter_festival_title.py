# Generated by Django 4.2.3 on 2024-01-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_ticket_ticket_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]