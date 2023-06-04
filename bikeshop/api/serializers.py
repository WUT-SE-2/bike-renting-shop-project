from rest_framework import serializers
from bike.models import Bike
from comment.models import Comment
from complaint.models import Complaint
from payment.models import Payment
from reservation.models import Reservation
from authentication.models import Person, Worker, Consumer
# from comment.models import  Comment

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


# class MechanicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mechanic
#         fields = '__all__'
