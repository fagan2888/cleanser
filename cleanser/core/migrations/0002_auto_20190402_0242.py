# Generated by Django 2.2a1 on 2019-04-02 02:42

import cleanser.core.models.utils
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('description', models.TextField(blank=True, default='')),
                ('source', models.CharField(blank=True, default='', max_length=128)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('source_url', models.URLField()),
                ('url', models.URLField()),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schema', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='JSON Schema for `inputs` and `outputs` of the model', null=True)),
            ],
            options={
                'db_table': 'model',
            },
            bases=(cleanser.core.models.utils.TimeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImageAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('confidence', models.FloatField(blank=True, default=None, null=True)),
                ('source', models.CharField(max_length=128)),
                ('concept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Concept')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(cleanser.core.models.utils.TimeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Embedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vector', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Model')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Dataset')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Image')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='images',
            field=models.ManyToManyField(through='core.DatasetImage', to='core.Image'),
        ),
    ]