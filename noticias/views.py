from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/lista.html', {'artigos': artigos})


def detalhe_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    return render(request, 'noticias/detalhe.html', {'artigo': artigo})


def comentarios(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        Comentario.objects.create(artigo=artigo, texto=texto)
        return redirect(f'/artigo/{id}/comentarios/')

    comentarios = artigo.comentarios.all()
    return render(request, 'noticias/comentarios.html', {
        'artigo': artigo,
        'comentarios': comentarios
    })