# Generated by Django 4.2.3 on 2024-01-14 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_project_festival'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='projects.festival')),
            ],
        ),
    ]