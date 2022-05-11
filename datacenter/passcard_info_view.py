from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_raw = Visit.objects.filter(passcard=this_passcard)
    this_passcard_visits = []
    for visit in this_passcard_visits_raw:
        this_passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_long(visit.get_duration())
        }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': this_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
