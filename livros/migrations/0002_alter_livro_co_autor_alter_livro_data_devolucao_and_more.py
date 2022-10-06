# Generated by Django 4.1.2 on 2022-10-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_devolucao',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livro',
            name='tempo_emprestado',
            field=models.DateField(blank=True),
        ),
    ]
