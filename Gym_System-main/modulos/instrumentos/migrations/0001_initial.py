# Generated by Django 4.1.4 on 2023-03-05 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('peso', models.CharField(max_length=100, verbose_name='peso')),
                ('precio_instrumento', models.IntegerField(default=0)),
                ('fecha_compra_instrumento', models.DateField(default=django.utils.timezone.now)),
                ('unidades', models.CharField(blank=True, choices=[('kg', ' Kilogramos'), ('Lb', 'Libras')], default=' Kilogramos', max_length=18, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]