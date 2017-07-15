from common.models import AbstractStatus


class ShowOnlyPublishedView(object):
    def get_queryset(self):
        queryset = super(ShowOnlyPublishedView, self).get_queryset()
        return queryset.filter(status=AbstractStatus.PUBLISHED)


class MetaContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MetaContextMixin, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context