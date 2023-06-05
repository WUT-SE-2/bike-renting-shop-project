from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *
from bike.models import Bike as bike
from comment.models import Comment as comment
from complaint.models import Complaint as complaint
from payment.models import Payment as payment
from reservation.models import Reservation as reservation
from authentication.models import Consumer as consumer
from authentication.models import Worker as worker


class Bikes(APIView):
    serializer_class = BikeSerializer

    def get(self, request, format=None):
        snippets = bike.objects.all()
        serializer = BikeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Bike(APIView):
    serializer_class = BikeSerializer

    def get_object(self, pk):
        try:
            return bike.objects.get(pk=pk)
        except bike.DoesNotExist:
            raise Http404

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
class Comments(APIView):
    serializer_class = CommentSerializer

    def get(self, request, format=None):
        snippets = comment.objects.all()
        serializer = CommentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return comment.objects.get(pk=pk)
        except comment.DoesNotExist:
            raise Http404

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Complaints(APIView):
    serializer_class = ComplaintSerializer

    def get(self, request, format=None):
        snippets = complaint.objects.all()
        serializer = ComplaintSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Complaint(APIView):
    serializer_class = ComplaintSerializer

    def get_object(self, pk):
        try:
            return complaint.objects.get(pk=pk)
        except complaint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Complaint = self.get_object(pk)
        serializer = ComplaintSerializer(Complaint)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Complaint = self.get_object(pk)
        serializer = ComplaintSerializer(Complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Complaint = self.get_object(pk)
        Complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Reservations(APIView):
    serializer_class = ReservationSerializer

    def get(self, request, format=None):
        snippets = reservation.objects.all()
        serializer = ReservationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Reservation(APIView):
    serializer_class = ReservationSerializer

    def get_object(self, pk):
        try:
            return reservation.objects.get(pk=pk)
        except reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Reservation = self.get_object(pk)
        serializer = ReservationSerializer(Reservation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Reservation = self.get_object(pk)
        serializer = ReservationSerializer(Reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Reservation = self.get_object(pk)
        Reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Payments(APIView):
    serializer_class = PaymentSerializer

    def get(self, request, format=None):
        Payments = payment.objects.all()
        serializer = PaymentSerializer(Payments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Payment(APIView):
    serializer_class = PaymentSerializer

    def get_object(self, pk):
        try:
            return payment.objects.get(pk=pk)
        except payment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Payment = self.get_object(pk)
        serializer = PaymentSerializer(Payments)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Payments = self.get_object(pk)
        serializer = PaymentSerializer(Payments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Payments = self.get_object(pk)
        Payments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Consumers(APIView):
    serializer_class = ConsumerSerializer

    def get(self, request, format=None):
        Consumers = consumer.objects.all()
        serializer = ConsumerSerializer(Consumers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Consumer(APIView):
    serializer_class = ConsumerSerializer

    def get_object(self, pk):
        try:
            return consumer.objects.get(pk=pk)
        except consumer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Consumer = self.get_object(pk)
        serializer = ConsumerSerializer(Consumer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Consumer = self.get_object(pk)
        serializer = ConsumerSerializer(Consumer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Consumer = self.get_object(pk)
        Consumer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Workers(APIView):
    # renderer_classes = [TemplateHTMLRenderer]  #for frontend
    serializer_class = WorkerSerializer

    def get(self, request, format=None):
        Workers = worker.objects.all()
        serializer = WorkerSerializer(Workers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Worker(APIView):
    serializer_class = WorkerSerializer

    def get_object(self, pk):
        try:
            return worker.objects.get(pk=pk)
        except worker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Worker = self.get_object(pk)
        serializer = WorkerSerializer(Worker)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Worker = self.get_object(pk)
        serializer = WorkerSerializer(Worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Worker = self.get_object(pk)
        Worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
