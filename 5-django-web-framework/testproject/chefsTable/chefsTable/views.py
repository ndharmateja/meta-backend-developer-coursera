from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("<h1>Not Found!!!</h1><p>Be more careful</p>")