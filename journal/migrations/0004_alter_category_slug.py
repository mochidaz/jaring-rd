from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
