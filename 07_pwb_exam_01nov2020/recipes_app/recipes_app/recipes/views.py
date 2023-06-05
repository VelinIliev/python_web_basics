from django.http import HttpResponse
from django.shortcuts import render, redirect

from recipes_app.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes_app.recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def recipe_create(request):
    if request.method == "GET":
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def recipe_edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def recipe_delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
    else:
        recipe.delete()
        return redirect('index')
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    ingredients = recipe.ingredients.split(", ")
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
