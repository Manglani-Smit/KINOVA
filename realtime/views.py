from django.shortcuts import render

def screen_view(request, room_code):
    return render(request, 'realtime/screen.html', {'room_code': room_code})

def controller_view(request, room_code):
    return render(request, 'realtime/controller.html', {'room_code': room_code})

def welcome_view(request):
    return render(request, 'realtime/welcome.html')