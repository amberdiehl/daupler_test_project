# Generated by Django 3.0.4 on 2020-03-15 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of role', max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of team', max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=30)),
                ('last_name', models.CharField(help_text='Last name', max_length=30)),
                ('on_call_order', models.IntegerField(help_text='On call order')),
                ('role', models.ForeignKey(help_text='Employee role on team', null=True, on_delete=django.db.models.deletion.SET_NULL, to='water.Role')),
                ('team', models.ForeignKey(help_text='Member of team', null=True, on_delete=django.db.models.deletion.SET_NULL, to='water.Team')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'unique_together': {('team', 'on_call_order')},
            },
        ),
    ]