from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.


def index(request):
    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        food = Food.objects.get(name=food_consumed)
        user = request.user
        Consume.objects.create(user=user, food_consumed=food)

    consumed_foods = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    return render(request, 'counter/index.html', {'foods': foods, 'consumed_foods': consumed_foods})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        if request.POST['delete'] == 'confirm':
            consumed_food.delete()
        return redirect('/')
    return render(request, 'counter/delete.html')