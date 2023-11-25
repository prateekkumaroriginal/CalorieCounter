from django.shortcuts import render
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