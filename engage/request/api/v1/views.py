import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.request.api.v1.serializers import RespondCreateSerializer, RespondListSerializer
from engage.request.models import Request
from engage.utils.custom_pagination import StandardResultsSetPagination


class RespondAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print("RespondAPIView get method called")
        union = request.query_params.get('union')
        data = []
        print(f"Union ID: {union}")
        if union:
            responds = Request.objects.filter(union__id=union)
            paginator = StandardResultsSetPagination()
            paginated_data = paginator.paginate_queryset(responds, request)
            serialized_data = RespondListSerializer(paginated_data, many=True)
            response = paginator.get_paginated_response(serialized_data.data)
            # Add total_page to the response
            total_count = paginator.page.paginator.count
            page_size = paginator.get_page_size(request)
            total_page = (total_count + page_size - 1) // page_size if page_size else 1
            response.data['total_page'] = total_page
            return response

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        union = request.data.get('union')
        if union:
            serializer = RespondCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Respond created successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED
                )

        return Response(
            {
                "success": False,
                "message": "Respond not created",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

