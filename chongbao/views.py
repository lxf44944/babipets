
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'browsingPageAPI': reverse('browsingPageAPI:browse-page', request=request, format=format),
       'detailPageAPI': reverse('detailPageAPI:detail-page', request=request, format=format),
    })
