# Generated by Django 2.2.4 on 2019-08-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='system_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_nic', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]