from common.models import AbstractStatus


class ShowOnlyPublishedView(object):
    def get_queryset(self):
        queryset = super(ShowOnlyPublishedView, self).get_queryset()
        return queryset.filter(status=AbstractStatus.PUBLISHED)