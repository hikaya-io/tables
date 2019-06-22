# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-31 05:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth2client.contrib.django_orm
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name=b'Celery task id')),
                ('task_status', models.CharField(blank=True, choices=[(b'CREATED', b'CREATED'), (b'IN_PROGRESS', b'IN_PROGRESS'), (b'FINISHED', b'FINISHED'), (b'FAILED', b'FAILED')], max_length=25, null=True, verbose_name=b'Celery task status')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, verbose_name=b'Country Name')),
                ('code', models.CharField(blank=True, max_length=4, verbose_name=b'2 Letter Country Code')),
                ('description', models.TextField(blank=True, max_length=765, verbose_name=b'Description/Notes')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Latitude')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Longitude')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('country',),
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('map_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('map_long', models.CharField(blank=True, max_length=100, null=True)),
                ('map_zoom', models.CharField(blank=True, max_length=10, null=True)),
                ('column_charts', models.TextField(default=b'[]')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedSilos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_time', models.DateTimeField()),
                ('silo_name_id', models.CharField(max_length=255)),
                ('silo_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormulaColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping', models.TextField()),
                ('operation', models.TextField()),
                ('column_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GoogleCredentialsModel',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='google_credentials', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.contrib.django_orm.CredentialsField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HikayaSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('agency_name', models.CharField(blank=True, max_length=255, null=True)),
                ('agency_url', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_url', models.CharField(blank=True, max_length=255, null=True)),
                ('hikaya_report_url', models.CharField(blank=True, max_length=255, null=True)),
                ('hikaya_activity_user', models.CharField(blank=True, max_length=255, null=True)),
                ('hikaya_activity_token', models.CharField(blank=True, max_length=255, null=True)),
                ('privacy_disclaimer', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='HikayaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hikaya_user_uuid', models.CharField(default=uuid.uuid4, max_length=255, unique=True, verbose_name=b'Hikaya User UUID')),
                ('title', models.CharField(blank=True, choices=[(b'mr', b'Mr.'), (b'mrs', b'Mrs.'), (b'ms', b'Ms.')], max_length=3, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Given Name')),
                ('employee_number', models.IntegerField(blank=True, null=True, verbose_name=b'Employee Number')),
                ('tables_api_token', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_api_token', models.CharField(blank=True, max_length=255, null=True)),
                ('privacy_disclaimer_accepted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Country')),
            ],
        ),
        migrations.CreateModel(
            name='MergedSilosFieldMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merge_type', models.CharField(blank=True, choices=[(b'merge', b'Merge'), (b'append', b'Append')], max_length=60, null=True)),
                ('mapping', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_uuid', models.CharField(default=uuid.uuid4, max_length=255, unique=True, verbose_name=b'Organization UUID')),
                ('name', models.CharField(blank=True, default=b'HikayaData', max_length=255, verbose_name=b'Organization Name')),
                ('description', models.TextField(blank=True, max_length=765, null=True, verbose_name=b'Description/Notes')),
                ('organization_url', models.CharField(blank=True, max_length=255, null=True)),
                ('level_1_label', models.CharField(blank=True, default=b'Program', max_length=255, verbose_name=b'Project/Program Organization Level 1 label')),
                ('level_2_label', models.CharField(blank=True, default=b'Project', max_length=255, verbose_name=b'Project/Program Organization Level 2 label')),
                ('level_3_label', models.CharField(blank=True, default=b'Component', max_length=255, verbose_name=b'Project/Program Organization Level 3 label')),
                ('level_4_label', models.CharField(blank=True, default=b'Activity', max_length=255, verbose_name=b'Project/Program Organization Level 4 label')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='PIIColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_name', models.CharField(blank=True, default=b'', max_length=100, verbose_name=b'source name')),
                ('description', models.TextField(blank=True, null=True)),
                ('read_url', models.CharField(blank=True, default=b'', max_length=250, verbose_name=b'source url')),
                ('resource_id', models.CharField(blank=True, max_length=200, null=True)),
                ('gsheet_id', models.CharField(blank=True, max_length=200, null=True)),
                ('onedrive_file', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, help_text=b'Enter username only if the data at this source is protected by a login', max_length=20, null=True)),
                ('password', models.CharField(blank=True, help_text=b'Enter password only if the data at this source is protected by a login', max_length=40, null=True)),
                ('token', models.CharField(blank=True, max_length=254, null=True)),
                ('file_data', models.FileField(blank=True, null=True, upload_to=b'uploads', verbose_name=b'Upload CSV File')),
                ('autopull_frequency', models.CharField(blank=True, choices=[(b'DISABLED', b'Disabled'), (b'daily', b'Daily'), (b'weekly', b'Weekly')], max_length=25, null=True)),
                ('autopush_frequency', models.CharField(blank=True, choices=[(b'DISABLED', b'Disabled'), (b'daily', b'Daily'), (b'weekly', b'Weekly')], max_length=25, null=True)),
                ('autopull_expiration', models.DateTimeField(blank=True, null=True)),
                ('autopush_expiration', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('edit_date', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='ReadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_type', models.CharField(blank=True, max_length=135)),
                ('description', models.CharField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Silo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('share_with_organization', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('public', models.BooleanField()),
                ('form_uuid', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'CustomForm UUID')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('columns', models.TextField(default=b'[]')),
                ('hidden_columns', models.TextField(default=b'[]')),
                ('rows_to_hide', models.TextField(default=b'[]')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Country')),
                ('formulacolumns', models.ManyToManyField(blank=True, related_name='silos', to='silo.FormulaColumn')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Organization')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reads', models.ManyToManyField(related_name='silos', to='silo.Read')),
                ('shared', models.ManyToManyField(blank=True, related_name='silos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPartyTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60, null=True)),
                ('token', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('edit_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('silo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unique_fields', to='silo.Silo')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowLevel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level1_uuid', models.CharField(max_length=255, unique=True, verbose_name=b'WorkflowLevel1 UUID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name=b'Name')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Country')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Organization')),
            ],
            options={
                'ordering': ('country',),
                'verbose_name_plural': 'Workflowlevel 1',
            },
        ),
        migrations.CreateModel(
            name='WorkflowLevel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level2_uuid', models.CharField(max_length=255, unique=True, verbose_name=b'WorkflowLevel2 UUID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name=b'Name')),
                ('activity_id', models.IntegerField(blank=True, null=True, verbose_name=b'ID')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Country')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Organization')),
                ('workflowlevel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silo.WorkflowLevel1')),
            ],
            options={
                'ordering': ('country',),
                'verbose_name_plural': 'Workflowlevel 2',
            },
        ),
        migrations.AddField(
            model_name='silo',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='silos', to='silo.Tag'),
        ),
        migrations.AddField(
            model_name='silo',
            name='workflowlevel1',
            field=models.ManyToManyField(blank=True, to='silo.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='read',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silo.ReadType'),
        ),
        migrations.AddField(
            model_name='mergedsilosfieldmapping',
            name='from_silo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_mappings', to='silo.Silo'),
        ),
        migrations.AddField(
            model_name='mergedsilosfieldmapping',
            name='merged_silo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='merged_silo_mappings', to='silo.Silo'),
        ),
        migrations.AddField(
            model_name='mergedsilosfieldmapping',
            name='to_silo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_mappings', to='silo.Silo'),
        ),
        migrations.AddField(
            model_name='hikayauser',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Organization'),
        ),
        migrations.AddField(
            model_name='hikayauser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hikaya_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hikayauser',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='deletedsilos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silo.Silo'),
        ),
        migrations.AddField(
            model_name='country',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='silo.Organization'),
        ),
    ]
