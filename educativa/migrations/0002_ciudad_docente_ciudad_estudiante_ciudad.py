# Generated by Django 5.1.5 on 2025-02-10 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educativa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='docente',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docentes_ciudad', to='educativa.ciudad'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes_ciudad', to='educativa.ciudad'),
        ),
    ]
