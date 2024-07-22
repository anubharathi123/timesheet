from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeDetailViewset, TimeSheetViewset

router = DefaultRouter()
router.register(r'employees', EmployeeDetailViewset, basename='employee')
router.register(r'timesheets', TimeSheetViewset, basename='timesheet')

urlpatterns = [
    path('', include(router.urls)),  # Prefix API routes with 'api/'
]
