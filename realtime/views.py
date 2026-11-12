from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


def welcome_view(request):
    return render(request, 'realtime/welcome.html')


def screen_view(request, room_code):
    return render(request, 'realtime/screen.html', {'room_code': room_code.upper()})


def controller_view(request, room_code):
    return render(request, 'realtime/controller.html', {'room_code': room_code.upper()})


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        room = request.POST.get('room', 'ALPHA').upper()

        fs = FileSystemStorage()
        filename = fs.save(f"uploads/{room}/{uploaded_file.name}", uploaded_file)
        file_url = fs.url(filename)

        return JsonResponse({
            'status': 'success',
            'name': uploaded_file.name,
            'url': file_url,
            'size': uploaded_file.size,
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)