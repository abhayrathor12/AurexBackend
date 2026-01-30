
from rest_framework import viewsets, permissions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import StartupApplication,Contact,InvestorApplication
from .serializers import StartupApplicationSerializer,InvestorApplicationSerializer,ContactSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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