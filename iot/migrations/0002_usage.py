# Generated by Django 3.0.2 on 2020-02-03 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_roomplan'),
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('appliace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Appliances')),
            ],
        ),
    ]
