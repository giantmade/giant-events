# Generated by Django 2.1.15 on 2020-07-07 15:07

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import mixins.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', mixins.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=False, help_text='Selecting this option will publish this item')),
                ('publish_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('intro', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_content', slotname='event_content', to='cms.Placeholder')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['start_at'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', mixins.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=12)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=12)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', mixins.fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='photo',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_event_images', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events_event_tags', to='events.Tag', verbose_name='Tags'),
        ),
    ]
