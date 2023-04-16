from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from bike.models import Bike
from bike.models import Bike
from comment.models import Comment
from complaint.models import Complaint
from payment.models import Payment
from reservation.models import Reservation
from authentication.models import Person, Worker

@api_view(['GET'])
def getBikeData(request):
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCommentData(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getComplaintData(request):
    complaints = Complaint.objects.all()
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getReservationData(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPaymentData(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getConsumerData(request):
    consumers = Consumer.objects.all()
    serializer = PersonSerializer(consumers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getWorkerData(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def getMechanicData(request):
#     mechanics = Mechanic.objects.all()
#     serializer = MechanicSerializer(mechanics, many=True)
#     return Response(serializer.data)
