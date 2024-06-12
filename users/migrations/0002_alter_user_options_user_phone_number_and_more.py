# Generated by Django 5.0.6 on 2024-06-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '회원', 'verbose_name_plural': '회원'},
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='01012345678', help_text='휴대전화 번호를 가급적이면 선호', max_length=128, verbose_name='전화번호'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]