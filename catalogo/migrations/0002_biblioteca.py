from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('catalogo', '0001_initial')]

    operations = [
        migrations.RenameModel(old_name='Categoria', new_name='Autor'),
        migrations.RenameField(model_name='autor', old_name='descricao', new_name='biografia'),
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nome'], 'verbose_name': 'autor', 'verbose_name_plural': 'autores'},
        ),
        migrations.RenameModel(old_name='Produto', new_name='Livro'),
        migrations.RenameField(model_name='livro', old_name='nome', new_name='titulo'),
        migrations.RenameField(model_name='livro', old_name='descricao', new_name='sinopse'),
        migrations.RenameField(model_name='livro', old_name='categoria', new_name='autor'),
        migrations.RemoveField(model_name='livro', name='preco'),
        migrations.RemoveField(model_name='livro', name='estoque'),
        migrations.AddField(model_name='livro', name='isbn', field=models.CharField(blank=True, max_length=13)),
        migrations.AddField(model_name='livro', name='ano_publicacao', field=models.PositiveIntegerField(blank=True, null=True)),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=models.PROTECT, related_name='livros', to='catalogo.autor'),
        ),
        migrations.AlterModelOptions(name='livro', options={'ordering': ['titulo']}),
    ]
