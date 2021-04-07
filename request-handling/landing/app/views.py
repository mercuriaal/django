from collections import Counter

from django.shortcuts import render


counter_show = Counter()
counter_click = Counter()


def index(request):
    version = request.GET.get('from-landing')
    if version == 'original':
        counter_click['original'] += 1
    elif version == 'test':
        counter_click['test'] += 1
    return render(request, 'index.html')


def landing(request):
    version = request.GET.get('ab-test-arg')
    if version == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    elif version == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    test_conversion = 0
    original_conversion = 0
    if counter_show['test'] != 0:
        test_conversion = counter_click['test']/counter_show['test']
    if counter_show['original'] != 0:
        original_conversion = counter_click['original'] / counter_show['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
