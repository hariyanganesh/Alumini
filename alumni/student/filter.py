import django_filters
from .models import student

class studentfilter(django_filters.filterSet);

  class meta:
     model=student
     fields=('Branch')
