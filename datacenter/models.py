import datetime

from django.db import models
from django.utils.timezone import localtime


def format_duration(duration):
    return datetime.timedelta(seconds=duration)


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if not self.leaved_at:
            time_in_storage = localtime() - localtime(self.entered_at)
        else:
            time_in_storage = localtime(self.leaved_at) - localtime(
                self.entered_at)
        return int(time_in_storage.total_seconds())

    @staticmethod
    def is_long(duration, minutes=60):
        return duration >= minutes * 60     # convert duration to seconds
