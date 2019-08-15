# Generated by Django 2.2.4 on 2019-08-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upstream_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=64, null=True)),
                ('port', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('max_fails', models.IntegerField()),
                ('fail_timeout', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='proxy_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_id', models.CharField(max_length=64, null=True)),
                ('protocols', models.BooleanField(default=False)),
                ('proxy_name', models.CharField(max_length=128, null=True)),
                ('status', models.BooleanField(default=False)),
                ('listen', models.IntegerField()),
                ('server_name', models.CharField(max_length=128, null=True)),
                ('access_log', models.CharField(max_length=128, null=True)),
                ('error_log', models.CharField(max_length=128, null=True)),
                ('ssl_cert', models.TextField(null=True)),
                ('ssl_cert_path', models.CharField(max_length=128, null=True)),
                ('ssl_key', models.TextField(null=True)),
                ('ssl_key_path', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(null=True)),
                ('balancer_type', models.CharField(max_length=64, null=True)),
                ('host', models.CharField(max_length=64, null=True)),
                ('check_type', models.CharField(max_length=64, null=True)),
                ('update_time', models.FloatField()),
                ('upstream_list', models.ManyToManyField(to='proxy.upstream_config')),
            ],
        ),
    ]
