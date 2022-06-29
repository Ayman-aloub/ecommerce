from rest_framework import pagination
from rest_framework.response import Response


class CustomPagenation(pagination.PageNumberPagination):
    page_size = 24

    def get_paginated_response(self, data):
        return Response({
            'totalpages': self.page.paginator.num_pages,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
