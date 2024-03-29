from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Festival, Ticket, Pledge
from .serializers import FestivalSerializer, FestivalDetailSerializer, TicketSerializer, PledgeSerializer, TicketDetailSerializer, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, isSupporterOrReadOnly, IsTicketOwnerOrReadOnly

# --------- Festival Views --------- 
class FestivalList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        festivals = Festival.objects.all()
        serializer = FestivalSerializer(festivals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FestivalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FestivalDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            festival = Festival.objects.get(pk=pk)
            self.check_object_permissions(self.request, festival)
            return festival
        except Festival.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        festival = self.get_object(pk)
        serializer = FestivalDetailSerializer(festival)
        return Response(serializer.data)

    def put(self, request, pk):
        festival = self.get_object(pk)
        serializer = FestivalDetailSerializer(
            instance=festival,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        # try:
        festival = self.get_object(pk)
        festival.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # except Festival.DoesNotExist:
        #     raise Http404

# --------- Ticket Views --------- 
class TicketList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ticket_owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class TicketDetial(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTicketOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
            self.check_object_permissions(self.request, ticket)
            return ticket
        except Ticket.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketDetailSerializer(ticket)
        return Response(serializer.data)
    
    def put(self,request,pk):
        ticket = self.get_object(pk)
        serializer = TicketDetailSerializer(
            instance=ticket,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# --------- Pledge Views --------- 

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        Pledges = Pledge.objects.all()
        serializer = PledgeSerializer(Pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetial(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isSupporterOrReadOnly]
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)
    
    def put(self,request,pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
