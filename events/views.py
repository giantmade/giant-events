from django.views.generic import DetailView, ListView

from .models import Event


class EventIndex(ListView):
    """
    Index view for events queryset
    """

    model = Event
    context_object_name = "event_index"
    template_name = "events/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Add published queryset to the context
        """
        context = super().get_context_data(
            object_list=Event.objects.published(), **kwargs
        )
        return context


class EventDetail(DetailView):
    """
    Detail view for an events object
    """

    queryset = Event.objects.published()
    template_name = "events/detail.html"
