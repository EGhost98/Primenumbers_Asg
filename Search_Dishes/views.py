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
    search_form.fields['query'].label = False 
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        items = Item.objects.all()  # Retrieve all items from the database
        # items = Item.objects.values_list('name', flat=True)
        results = process.extract(query, items, scorer=fuzz.partial_token_set_ratio, limit=5)  # Limiting to 5 matches
        matched_items = []
        similarity_scores = []
        for result in results:
            item = result[0]
            similarity_score = result[1]
            if(similarity_score<80 ):
                continue
            matched_items.append(item)
            # similarity_scores.append(similarity_score)
        restaurants = []
        context['results'] = matched_items
        # context['similarity_scores'] = similarity_scores
    context['search_form'] = search_form
    return render(request, template, context)
