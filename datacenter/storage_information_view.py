from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    serialized_non_closed_visits = []
    for visit in non_closed_visits:
        serialized_visit = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
            }
        serialized_non_closed_visits.append(serialized_visit)
    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
