from django.db import models
from django.contrib.auth.models import User

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='schedules')
    title = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.event.name}'


# Slot model for each schedule
class Slot(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='slots')
    capacity = models.PositiveIntegerField(default=1)
    registered_users = models.ManyToManyField(User, blank=True, related_name='registered_slots')

    def __str__(self):
        return f'Slot for {self.schedule.title}'

    def is_full(self):
        return self.registered_users.count() >= self.capacity

    def remaining(self):
        return self.capacity - self.registered_users.count()
