from django.shortcuts import render
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from .models import Restaurant, Item
from django.views import View
from .forms import Query

def index(request):
    template = 'index.html'
    context = {}
    search_form = Query(request.GET)
    # if search_form.is_valid():
    #     query = search_form.cleaned_data.get('query')
    #     items = Item.objects.all()  # Retrieve all items from the database
    #     item_names = [item.name for item in items]  # Extract the item names
    #     results = process.extract(query, item_names, scorer=fuzz.ratio, limit=5)  # Limiting to 5 matches


    #     # Extract the item names and similarity scores from the results
    #     matched_items = [result[0].name for result in results]
    #     similarity_scores = [result[1] for result in results]

    #     context['matched_items'] = matched_items
    #     context['similarity_scores'] = similarity_scores

    context['search_form'] = search_form
    return render(request, template, context)
