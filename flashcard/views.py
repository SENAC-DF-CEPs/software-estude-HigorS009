from django.shortcuts import render, redirect
from .models import Flashcard, Categoria
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/login')

    if request.method == 'GET':
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcards = Flashcard.objects.filter(user=request.user)

        return render(
            request,
            'novo_flashcard.html',
            {
                'categorias': categorias,
                'dificuldades': dificuldades,
                'flashcards': flashcards,
            }
            
        )
    elif request.method == 'POST':
        pergunta = request.POST.get('pergunta', '').strip()
        resposta = request.POST.get('resposta', '').strip()
        categoria = request.POST.get('categoria')
        dificuldade = request.POST.get('dificuldade')
        if len(pergunta) == 0 or len(resposta) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                'Preencha os campos de pergunta e resposta',
            )
            return redirect('/flashcard/novo_flashcard')

        flashcard = Flashcard(
            user=request.user,
            pergunta=pergunta,
            resposta=resposta,
            categoria_id=categoria,
            dificuldade=dificuldade,
        )

        flashcard.save()

        messages.add_message(
            request, constants.SUCCESS, 'Flashcard criado com sucesso'
        )
        return redirect('/flashcard/novo_flashcard')