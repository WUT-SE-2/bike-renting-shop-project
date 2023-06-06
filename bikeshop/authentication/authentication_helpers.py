from .models import Consumer, Worker, Mechanic


def confirm_consumer(user_id):
    return Consumer.objects.filter(user__id=user_id).exists()


def confirm_worker(user_id):
    return Worker.objects.filter(user__id=user_id).exists()


def confirm_mechanic(user_id):
    return Mechanic.objects.filter(user__id=user_id).exists()
