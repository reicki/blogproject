# Generated by Django 3.1.3 on 2024-01-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_blogmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('hobby', '趣味'), ('study', '学習'), ('other', 'その他')], default='other', max_length=50),
            preserve_default=False,
        ),
    ]