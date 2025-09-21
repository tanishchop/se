from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Event, Schedule
from .forms import ScheduleForm

@login_required
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    schedules = Schedule.objects.filter(event=event).order_by('start_time')
    can_edit = request.user.is_authenticated and hasattr(request.user, 'organizer') and request.user.organizer == event.organizer
    return render(request, 'events/event_detail.html', {
        'event': event,
        'schedules': schedules,
        'can_edit': can_edit
    })

@login_required
def schedule_create(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        if not (hasattr(request.user, 'organizer') and request.user.organizer == event.organizer):
            return JsonResponse({'error': 'Permission denied.'}, status=403)
        
        form = ScheduleForm(request.POST, event=event)
        if form.is_valid():
            schedule = form.save()
            return JsonResponse({'success': True, 'id': schedule.id, 'title': schedule.title, 'start_time': schedule.start_time.strftime('%H:%M'), 'end_time': schedule.end_time.strftime('%H:%M'), 'description': schedule.description})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid method.'}, status=405)

@login_required
def schedule_update(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    event = schedule.event
    if request.method == 'POST':
        if not (hasattr(request.user, 'organizer') and request.user.organizer == event.organizer):
            return JsonResponse({'error': 'Permission denied.'}, status=403)
        
        form = ScheduleForm(request.POST, instance=schedule, event=event)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'id': schedule.id, 'title': schedule.title, 'start_time': schedule.start_time.strftime('%H:%M'), 'end_time': schedule.end_time.strftime('%H:%M'), 'description': schedule.description})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    elif request.method == 'GET':
        data = {
            'title': schedule.title,
            'start_time': schedule.start_time.strftime('%H:%M'),
            'end_time': schedule.end_time.strftime('%H:%M'),
            'description': schedule.description
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid method.'}, status=405)

@login_required
def schedule_delete(request, schedule_id):
    if request.method == 'POST':
        schedule = get_object_or_404(Schedule, id=schedule_id)
        event = schedule.event
        if not (hasattr(request.user, 'organizer') and request.user.organizer == event.organizer):
            return JsonResponse({'error': 'Permission denied.'}, status=403)
        
        schedule.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid method.'}, status=405)
