from django.shortcuts import redirect, render
from .models import MaziiWordTranslate, KanjiMeaning, Kanji
from .forms import SearchForm, SuggestionsForm
from django.db import models
from django.http import HttpResponse
from .utils import fetchWordMeaning, fetchWordSuggestion

class SearchField(models.Model):
    myRef = any
    result_mazzii = models.ManyToManyField(MaziiWordTranslate)  # Danh sách kết quả của MaziiWordTranslate
    result_kanji = models.ManyToManyField(KanjiMeaning)  # Danh sách kết quả của KanjiMeaning

def searchWordMeaning(request):
    results = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data.get('search_word')
            lang = form.cleaned_data.get('lang')
            search_type = form.cleaned_data.get('type')
            results = fetchWordMeaning(search_word, lang, search_type)
            return HttpResponse(f"<h1>{results}</h1>")
    else:
        return render(request, 'search.html', {'form': SearchForm})
    
def searchWordSuggestion(request):
    if request.method == 'POST':
        form = SuggestionsForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data.get('search_word')
            lang = form.cleaned_data.get('lang')
            suggestions = fetchWordSuggestion(search_word, lang)
            return HttpResponse(f"<h1>{suggestions}</h1>")
    else:
        return render(request, 'suggestions.html', {'form': SuggestionsForm})