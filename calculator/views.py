from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pizza': {
        'тесто, г': 250,
        'колбаса, г': 100,
        'сыр, г': 120,
        'помидор, шт': 1,
        'кетчуп, ст.л.': 2,
    },
}


def home_view(request):
    template_name = 'home.html'
    pages = {
        'Омлет': 'omlet/',
        'Паста': 'pasta/',
        'Бутерброд': 'buter/',
        'Пицца': 'pizza/'
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipe(request, food_type):
    food_type_new = food_type.rstrip('/')
    dish = DATA[food_type_new]
    recipe = {}
    for key, value in dish.items():
        recipe[key] = value
    context = {
        'recipe': recipe
    }
    serving = int(request.GET.get('servings', 1))
    for key, value in recipe.items():
        count = round(value * serving, 2)
        recipe[key] = count
    return render(request, 'index.html', context)
