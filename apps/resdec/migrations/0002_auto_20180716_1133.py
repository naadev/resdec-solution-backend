# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 16:33


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resdec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.CharField(choices=[(b'A', b'Active'), (b'I', b'Inactive')], max_length=1)),
                ('relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resdec.RelationshipType')),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TrendsItemsNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=40)),
                ('status', models.CharField(choices=[(b'A', b'Active'), (b'I', b'Inactive')], max_length=1)),
                ('trend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resdec.Trend')),
            ],
        ),
        migrations.AlterField(
            model_name='variabilityenvironmentdata',
            name='file',
            field=models.FileField(upload_to=b'../resources/data/uploaded'),
        ),
    ]
