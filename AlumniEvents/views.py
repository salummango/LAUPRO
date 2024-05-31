from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AlumniEvents:lists')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = EventForm()
    # return render(request, 'events/create_event.html', {'form': form})
    # return render(request, 'events/event2.html', {'form': form})
    return render(request, 'events/createEvent3.html', {'form': form})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


# for calender
# from django.http import JsonResponse
# def events(request):
#     events = Event.objects.all()
#     data = [{'id': event.id, 'title': event.title, 'start': event.start_date.isoformat(), 'end': event.end_date.isoformat()} for event in events]
#     return JsonResponse(data, safe=False)

# from django.shortcuts import render
# from schedule.models import Event as ScheduleEvent
# from django.core.serializers import serialize
# from django.http import JsonResponse

# def event_calendar(request):
#     # Fetch events from the database
#     events = ScheduleEvent.objects.all()
#     # Serialize events to JSON format
#     serialized_events = serialize('json', events)
#     return render(request, 'events/Calendar.html', {'serialized_events': serialized_events})
