
from django.shortcuts import redirect
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view,renderer_classes


@api_view(['GET'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, ])
def redirect_view(request):
    response = redirect('https://unificater.com/#/')
    return response