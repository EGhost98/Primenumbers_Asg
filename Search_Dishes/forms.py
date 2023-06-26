from django import forms

class Query(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Dishes'})) 

    # csv_path = 'Search_Dishes/restaurants_small.csv'
    # Restaurant.DB_From_CSV(csv_path)