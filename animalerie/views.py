from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Animal
from .controller import nourrir, divertir, coucher, reveiller


def index(request):
    animal_list = Animal.objects.all()
    action_list = ['nourrir', 'divertir', 'coucher', 'reveiller']
    context = {'animal_list': animal_list, 'action_list': action_list}
    return render(request, 'animalerie/index.html', context)


def action(request):

    try:
        selected_animal = Animal.objects.get(pk=request.POST['id_animal'])
        selected_action = request.POST['actions']
    except (KeyError, Animal.DoesNotExist):
        return render(request, 'animalerie/action.html', {'error_message': "You didn't select a choice."})
    else:
        aux = ''
        if selected_action == 'nourrir':
            aux = nourrir(selected_animal.NAME)
        elif selected_action == 'divertir':
            aux = divertir(selected_animal.NAME)
        elif selected_action == 'coucher':
            aux = coucher(selected_animal.NAME)
        elif selected_action == 'reveiller':
            aux = reveiller(selected_animal.NAME)
        if aux == '' or aux is None:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'animalerie/action.html', {'aux': aux})

# Create your views here.
