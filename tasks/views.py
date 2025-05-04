from rest_framework import viewsets
from .serializer import TaskSerialize
from django.utils.dateparse import parse_date
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    # Create your views here.
    queryset = Task.objects.all()
    serializer_class = TaskSerialize



    def get_queryset(self):


    # 1) /api/tasks/?sort_by_date=true
    # 2) /api/tasks/?search_date=YYYY-MM-DD
    # 3) /api/tasks/?search=something
        qs = super().get_queryset()

        sort_by_date = self.request.query_params.get('sort_by_date')
        search_date = self.request.query_params.get('search_date')
        search = self.request.query_params.get('search')

        if sort_by_date and sort_by_date.lower() == 'true':
            qs = qs.order_by('date')

        if search_date:
            parsed_date = parse_date(search_date)
            if parsed_date:
                qs = qs.filter(date=parsed_date)

        if search:
            qs = qs.filter(title__icontains=search)

        return qs