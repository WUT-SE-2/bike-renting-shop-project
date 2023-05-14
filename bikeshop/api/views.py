from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *
from bike.models import Bike
from bike.models import Bike
from comment.models import Comment
from complaint.models import Complaint
from payment.models import Payment
from reservation.models import Reservation
from authentication.models import Person, Worker

class BikeDataREST(APIView):
    ID = 1
    @api_view(['GET'])
    def getBikeData(request):
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def postBikeData(self, request, *args, **kwargs):
            data = {
                #'bike_ID' :  BikeDataREST.ID,
                'name': request.data.get('name'), 
                'usable': request.data.get('usable'), 
                'location' : request.data.get('location'),
                'purchase_date' : request.data.get('purchase_date'),
            }
            serializer = BikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                BikeDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentDataREST(APIView):
    ID = 1
    @api_view(['GET'])
    def getCommentData(request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def postCommentData(self, request, *args, **kwargs):
            data = {
                'comm_ID' :  CommentDataREST.ID,
                'description': request.data.get('description'), 
            }
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                CommentDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComplaintDataREST(APIView):
    @api_view(['GET'])
    def getComplaintData(request):
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def postComplaintData(self, request, *args, **kwargs):
            data = {
                'comp_ID' :  ComplaintDataREST.ID,
                'description': request.data.get('description'), 
                'comments' : request.data.get('comments'), 
                'last_updated' : timezone.now,
                'status' : Complaint.Status.opened
            }
            serializer = ComplaintSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                ComplaintDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDataREST(APIView):
    ID = 1
    @api_view(['GET'])
    def getReservationData(request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def postReservationData(self, request, *args, **kwargs):
            data = {
                'reservation_ID' :  ReservationDataREST.ID,
                'reservation_date_request': request.data.get('reservation_date_request'), 
                'reservation_date_end' : request.data.get('reservation_date_end'), 
                'reserved_bike' : request.data.get('reserved_bike'),
                'reservationStatus' : Reservation.ReservationStatus.pending
            }
            serializer = ReservationSerializer(data=data) 
            if serializer.is_valid():
                serializer.save()
                ReservationDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDataREST(APIView):
    ID = 1
    @api_view(['GET'])
    def getPaymentData(request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def postReservationData(self, request, *args, **kwargs):
            data = {
                'payment_ID' :  PaymentDataREST.ID,
                'payment_date' : timezone.now
            }
            serializer = PaymentSerializer(data=data) 
            if serializer.is_valid():
                serializer.save()
                PaymentDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDataREST(APIView):
    @api_view(['GET'])
    def getPersonData(request):
        consumers = Person.objects.all()
        serializer = PersonSerializer(consumers, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def postPersonData(self, request, *args, **kwargs):
            data = {
                'person_ID' :  PersonDataREST.ID,
                'name' : request.data.get('name'),
                'surname' : request.data.get('surname'),
                'email' : request.data.get('email'),
                'phoneNumber' : request.data.get('phoneNumber'),
                'comments' : request.data.get('comments')
            }
            serializer = PersonSerializer(data=data) 
            if serializer.is_valid():
                serializer.save()
                PersonDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WorkerDataREST(APIView):
    @api_view(['GET'])
    def getWorkerData(request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def postWorkerData(self, request, *args, **kwargs):
            data = {
                'person_ID' :  PersonDataREST.ID,
                'name' : request.data.get('name'),
                'surname' : request.data.get('surname'),
                'email' : request.data.get('email'),
                'phoneNumber' : request.data.get('phoneNumber'),
                'comments' : request.data.get('comments'),
                'reservations' : request.data.get('reservations')
            }
            serializer = WorkerSerializer(data=data) 
            if serializer.is_valid():
                serializer.save()
                PersonDataREST.ID =+ 1
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(['GET'])
# def getMechanicData(request):
#     mechanics = Mechanic.objects.all()
#     serializer = MechanicSerializer(mechanics, many=True)
#     return Response(serializer.data)
