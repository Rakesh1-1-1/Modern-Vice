# Generated by Django 4.1.4 on 2022-12-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=25)),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.register')),
            ],
        ),
    ]
