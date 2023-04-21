from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from main.models import Room, Reservation


# Create your views here.
class Main(View):
    def get(self, request):
        rooms = Room.objects.all()
        reservations = Reservation.objects.filter(date=datetime.now().strftime('%Y-%m-%d'))
        return render(request, 'main/main.html', {'rooms': rooms,
                                                  'reservations': reservations})


class AddRoom(View):
    def get(self, request):
        return render(request, 'main/add_room.html')

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = bool(request.POST.get('projector'))

        if not name:
            return HttpResponse('Name can not be empty!')
        try:
            capacity = int(capacity)
        except ValueError:
            return HttpResponse('Capacity must be an integer!')
        if capacity < 0:
            return HttpResponse('Capacity must be positive number!')
        if Room.objects.filter(name=name):
            return HttpResponse('This room already exists!')

        Room.objects.create(name=name, capacity=capacity, is_projector=projector)
        return redirect('main')


def detail_room(request, room_id):
    return render(request, 'main/detail.html',
                  {'room': Room.objects.get(pk=room_id),
                   'reservations': Reservation.objects.filter(room_id=room_id).order_by('date')})


def delete_room(request, room_id):
    Room.objects.get(pk=room_id).delete()
    return redirect('main')


class EditRoom(View, ):
    def get(self, request, room_id):
        return render(request, 'main/edit.html', {'room': Room.objects.get(pk=room_id)})

    def post(self, request, room_id):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = bool(request.POST.get('projector'))
        room = Room.objects.get(pk=room_id)

        if not name:
            return HttpResponse('Name can not be empty!')
        try:
            capacity = int(capacity)
        except ValueError:
            return HttpResponse('Capacity must be an integer!')
        if capacity < 0:
            return HttpResponse('Capacity must be positive number!')
        if Room.objects.filter(name=name):
            return HttpResponse('This room already exists!')

        room.name = name
        room.capacity = capacity
        room.is_projector = projector
        room.save()
        return redirect('main')


class ReserveRoom(View):
    def get(self, request, room_id):
        return render(request, 'main/reserve.html', {'room': Room.objects.get(pk=room_id),
                                                     'reservations': Reservation.objects.filter(room_id=room_id)})

    def post(self, request, room_id):
        date = request.POST.get('date')
        comment = request.POST.get('comment')

        if Reservation.objects.filter(date=date).filter(room_id=room_id):
            return HttpResponse('This room is already reserved in that date')

        if date < datetime.now().strftime('%Y-%m-%d'):
            return HttpResponse('This date is from past')

        Reservation.objects.create(date=date, comment=comment, room_id=room_id)
        return redirect('main')


def search(request):
    name = request.GET.get('name')
    capacity = request.GET.get('capacity')
    projector = request.GET.get('projector')
    c_name = request.GET.get('check_name')
    c_capacity = request.GET.get('check_capacity')
    rooms = Room.objects.all()

    if not c_name and not c_capacity and not projector:
        return HttpResponse('You have to tick the field of search')
    if c_name:
        rooms = rooms.filter(name=name)
    if c_capacity:
        rooms = rooms.filter(capacity__gte=capacity)
    if projector:
        rooms = rooms.filter(is_projector=True)

    return render(request, 'main/search.html', {'rooms':rooms})
