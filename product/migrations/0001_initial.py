# Generated by Django 4.2.3 on 2024-03-23 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=50)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_image', models.ImageField(upload_to='media/images')),
                ('prod_desc', models.TextField()),
                ('prod_price', models.FloatField(blank=True, default=None, null=True)),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.subcategory')),
            ],
        ),
    ]
