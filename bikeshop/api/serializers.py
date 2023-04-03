from rest_framework import serializers
from models import *


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '_all_'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '_all_'
        
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '_all_'
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '_all_'
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '_all_'
        
class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '_all_'
        
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '_all_'
        
class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '_all_'
        
