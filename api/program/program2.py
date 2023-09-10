from rest_framework.views import APIView


class t1APIView(APIView):
    # renderer_classes = []
    # parser_classes = []
    authentication_classes = []
    # throttle_classes = []
    permission_classes = []
    # content_negotiation_class = []

    def get(self, request):
        pass

    # API policy instantiation methods
    # def get_renderers(self):
    #     return super().get_renderers()

    # def get_parsers(self):
    #     return super().get_parsers()

    # def get_authenticators(self):
    #     return super().get_authenticators()

    # def get_throttles(self):
    #     return super().get_throttles()

    # def get_permissions(self):
    #     return super().get_permissions()

    # def get_content_negotiator(self):
    #     return super().get_content_negotiator()

    # def get_exception_handler(self):
    #     return super().get_exception_handler()

    # API policy implementation methods
    # def check_permissions(self, request):
    #     return super().check_permissions(request)

    # def check_throttles(self, request):
    #     return super().check_throttles(request)

    # def perform_content_negotiation(self, request, force=False):
    #     return super().perform_content_negotiation(request, force)
