from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('master', models.CharField(max_length=100)),
                ('est_year', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('key_members', models.TextField(help_text='Pisahkan dengan koma')),
                ('theme_color', models.CharField(default='#8a1c1c', help_text='Kode Hex warna border', max_length=20)),
            ],
        ),
    ]
