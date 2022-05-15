from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    workers_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for worker in workers_in_storage:
        non_closed_visit = {
                'who_entered': worker.passcard.owner_name,
                'entered_at': worker.entered_at,
                'duration': format_duration(worker.get_duration()),
            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
