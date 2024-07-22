from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import EmployeeDetail, TimeSheet
from .serializers import EmployeeDetailSerializer, TimeSheetSerializer

class EmployeeDetailViewset(viewsets.ModelViewSet):
    queryset = EmployeeDetail.objects.all()
    serializer_class = EmployeeDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        emp_id = self.kwargs.get('pk')
        print(emp_id)
        try:
            employee = EmployeeDetail.objects.get(emp_id=emp_id)
        except EmployeeDetail.DoesNotExist:
            raise NotFound(detail="Employee detail not found.")
        
        serializer = self.get_serializer(employee)
        return Response(serializer.data)
    
class TimeSheetViewset(viewsets.ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        timesheet = self.get_object()
        timesheet.lead_approval = 'approved'
        timesheet.save()
        return Response({'status': 'approved'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        timesheet = self.get_object()
        timesheet.lead_approval = 'rejected'
        timesheet.save()
        return Response({'status': 'rejected'})
