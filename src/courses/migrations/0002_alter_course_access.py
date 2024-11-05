# Generated by Django 5.1.1 on 2024-09-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="access",
            field=models.CharField(
                choices=[("any", "Anyone"), ("email", "Email required")],
                default="email",
                max_length=5,
            ),
        ),
    ]