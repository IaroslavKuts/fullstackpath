from django.views.generic import TemplateView
import logging



logger = logging.getLogger(__name__)


class BaseView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.exception('msg')
            return super().dispatch(request, *args, **kwargs)
        
