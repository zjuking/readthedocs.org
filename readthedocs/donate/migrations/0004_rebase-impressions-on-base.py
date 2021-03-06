# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_add-impressions')
    ]

    operations = [
        migrations.RenameModel(
            'SupporterImpressions',
            'PromoImpressions',
        ),
        migrations.CreateModel(
            name='ProjectImpressions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('offers', models.IntegerField(default=0, verbose_name='Offer')),
                ('views', models.IntegerField(default=0, verbose_name='View')),
                ('clicks', models.IntegerField(default=0, verbose_name='Clicks')),
                ('project', models.ForeignKey(related_name='impressions', blank=True, to='projects.Project', null=True)),
                ('promo', models.ForeignKey(related_name='project_impressions', blank=True, to='donate.SupporterPromo', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectimpressions',
            unique_together=set([('project', 'promo', 'date')]),
        ),
    ]
