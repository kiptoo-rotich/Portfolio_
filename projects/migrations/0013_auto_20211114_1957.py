# Generated by Django 3.2.5 on 2021-11-14 16:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20211112_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school_web',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Flask', 'Flask'), ('Angular', 'Angular'), ('Bootstrap', 'Bootstrap'), ('Git', 'Git'), ('Javascript', 'Javascript'), ('Postgresql', 'Postgresql'), ('DjangoREST', 'DjangoREST'), ('Typescript', 'Typescript'), ('CSS', 'CSS'), ('HTML', 'HTML')], max_length=200, null=True),
        ),
    ]
