# Generated by Django 2.2.5 on 2019-09-26 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='team_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
    ]