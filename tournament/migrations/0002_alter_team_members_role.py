# Generated by Django 4.2.5 on 2023-09-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tournament", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team_members",
            name="role",
            field=models.CharField(max_length=100),
        ),
    ]