# Generated by Django 4.1.1 on 2022-09-13 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnuncioVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prod', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('descricao_prod', models.TextField(verbose_name='Descrição do Produto')),
                ('quantidade_prod', models.IntegerField(default=1, verbose_name='Quantidade do Produto')),
                ('categoria', models.CharField(default='Outros', max_length=100, verbose_name='Categoria do Produto')),
                ('img_prod', models.ImageField(blank=True, null=True, upload_to='marketplace', verbose_name='Imagem do Produto')),
                ('estado', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=1, verbose_name='Estado do Anúncio')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade do Produto')),
                ('preco_prod', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do Produto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Anúncios de Venda',
            },
        ),
        migrations.CreateModel(
            name='AnuncioDoacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prod', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('descricao_prod', models.TextField(verbose_name='Descrição do Produto')),
                ('quantidade_prod', models.IntegerField(default=1, verbose_name='Quantidade do Produto')),
                ('categoria', models.CharField(default='Outros', max_length=100, verbose_name='Categoria do Produto')),
                ('img_prod', models.ImageField(blank=True, null=True, upload_to='marketplace', verbose_name='Imagem do Produto')),
                ('estado', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=1, verbose_name='Estado do Anúncio')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade do Produto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Anúncios de Doação',
            },
        ),
    ]