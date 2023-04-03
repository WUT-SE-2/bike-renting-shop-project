from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import *
from .serializers import *

@api_view(['GET'])
def getBikedata(request):  
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCommentdata(request):  
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getComplaintdata(request):  
    complaints = Complaint.objects.all()
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReservationdata(request):  
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPaymentdata(request):  
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getConsumerdata(request):  
    consumers = Consumer.objects.all()
    serializer = ConsumerSerializer(consumers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getWorkerdata(request):  
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMechanicdata(request):  
    mechanics = Mechanic.objects.all()
    serializer = MechanicSerializer(mechanics, many=True)
    return Response(serializer.data)
