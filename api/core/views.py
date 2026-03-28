from django.http import JsonResponse


def health(request):
    return JsonResponse({'status': 'ok', 'message': 'API running'})


def ping(request):
    return JsonResponse({'pong': 'OK'})


def hello(request):
    nome = request.GET.get('name', 'mundo')
    return JsonResponse({'hello': f'Olá, {nome}!'})
