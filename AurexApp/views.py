
from rest_framework import viewsets, permissions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import StartupApplication,Contact,InvestorApplication
from .serializers import StartupApplicationSerializer,InvestorApplicationSerializer,ContactSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import EventRegistration,WebinarRegistration
from .serializers import EventRegistrationSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class EventRegistrationCreateView(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer


class EventRegistrationListView(generics.ListAPIView):
    queryset = EventRegistration.objects.all().order_by('-created_at')
    serializer_class = EventRegistrationSerializer

class StartupApplicationViewSet(viewsets.ModelViewSet):
    """
    list      -> GET    /api/startups/
    retrieve  -> GET    /api/startups/{id}/
    create    -> POST   /api/startups/
    update    -> PUT    /api/startups/{id}/
    partial   -> PATCH  /api/startups/{id}/
    destroy   -> DELETE /api/startups/{id}/
    """
    queryset = StartupApplication.objects.all().order_by("-created_at")
    serializer_class = StartupApplicationSerializer
    permission_classes = [permissions.AllowAny]  # change later to IsAuthenticated
    
    
class ContactViewSet(viewsets.ModelViewSet):  # allow POST
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    


class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)

       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
def contact_list(request):
    contacts = Contact.objects.all().order_by("-id")  # latest first
    return render(request, "contact.html", {"contacts": contacts})    



def startup_list(request):
    startups = StartupApplication.objects.all().order_by("created_at")
    print(startups)
    return render(request, "startup.html", {
        "startups": startups,
    })



class InvestorApplicationViewSet(viewsets.ModelViewSet):
    queryset = InvestorApplication.objects.all().order_by("-created_at")
    serializer_class = InvestorApplicationSerializer
    permission_classes = [permissions.AllowAny]
    
    
    
    
def investor_list(request):
    investors = InvestorApplication.objects.all().order_by("-created_at")
    return render(request, "investor.html", {
        "investors": investors,
    })
    
    
    


def startup_detail(request, pk):
    startup = get_object_or_404(StartupApplication, pk=pk)
    return render(request, "startup_detail.html", {
        "startup": startup
    })
    
    
    
def investor_detail(request, pk):
    investor = get_object_or_404(InvestorApplication, pk=pk)
    return render(request, "investor_detail.html", {
        "investor": investor
    })    
    
    
class EventRegistrationCreateView(generics.CreateAPIView):

    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()
        
from django.views.generic import ListView, DetailView
from .models import EventRegistration
from .serializers import EventRegistrationSerializer  # if you still want API

class EventRegistrationListView(ListView):
    model = EventRegistration
    template_name = "registrations.html"
    context_object_name = "registrations"
    ordering = ["-created_at"]

class EventRegistrationDetailView(DetailView):
    model = EventRegistration
    template_name = "registration_detail.html"
    context_object_name = "registration"
    
from django.urls import reverse_lazy
from django.views.generic import DeleteView
    
class EventRegistrationDeleteView(DeleteView):
    model = EventRegistration
    success_url = reverse_lazy('event-registrations')
    
    
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import WebinarRegistration
from .serializers import WebinarRegistrationSerializer


class WebinarRegistrationViewSet(viewsets.ModelViewSet):
    queryset = WebinarRegistration.objects.all().order_by('-created_at')
    serializer_class = WebinarRegistrationSerializer

    # ✅ CREATE (Register user)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ GET ALL (List)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # ✅ MARK ATTENDED
    @action(detail=True, methods=['patch'])
    def mark_attended(self, request, pk=None):
        registration = self.get_object()

        # 🔥 get value from request
        attended_value = request.data.get("attended")

        # if not provided → default True
        if attended_value is None:
            attended_value = True

        registration.attended = attended_value
        registration.save()

        return Response({
            "message": "Attendance updated",
            "id": registration.id,
            "attended": registration.attended
        })
    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        ids = request.data.get("ids", [])

        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        deleted_count, _ = WebinarRegistration.objects.filter(id__in=ids).delete()

        return Response({
            "message": f"{deleted_count} records deleted successfully"
        }, status=status.HTTP_200_OK)
def webinar_list(request):
    Webinar = WebinarRegistration.objects.all().order_by("-id")  # latest first
    return render(request, "webinar_contact.html", {"registrations": Webinar})