from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        date_filter = self.request.query_params.get('date_filter')

        if date_filter == 'week':
            start_date = timezone.now() - timedelta(weeks=1)
            queryset = queryset.filter(date__gte=start_date)
        elif date_filter == 'month':
            start_date = timezone.now() - timedelta(days=30)
            queryset = queryset.filter(date__gte=start_date)
        elif date_filter == '3months':
            start_date = timezone.now() - timedelta(days=90)
            queryset = queryset.filter(date__gte=start_date)
        elif date_filter == 'custom':
            start_date = self.request.query_params.get('start_date')
            end_date = self.request.query_params.get('end_date')
            if start_date and end_date:
                try:
                    start_date = timezone.datetime.fromisoformat(start_date)
                    end_date = timezone.datetime.fromisoformat(end_date)
                    queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
                except ValueError:
                    queryset = queryset.none()  # Devuelve un queryset vacío en caso de error

        return queryset