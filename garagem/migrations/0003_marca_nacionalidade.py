# Generated by Django 4.1.7 on 2023-03-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_remove_marca_nacionalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
