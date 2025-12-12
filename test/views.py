from django.shortcuts import render
from django_minify_html.decorators import no_html_minification

def blur_test(request):
    return render(request, 'blur_test.html')

@no_html_minification
def blur_test_unminified(request):
    return render(request, 'blur_test.html')
