import json 

from django.shortcuts import get_object_or_404

from datetime import datetime, timedelta

from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.utils.jwt_token import decode_jwt
from engage.accounts.models import User
from engage.request.serializers import RespondCreateSerializer, RespondListSerializer, RespondImageSerializer
from engage.request.models import Request, RespondImage
from engage.utils.custom_pagination import StandardResultsSetPagination
from pytz import timezone


class RespondAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print("RespondAPIView get method called")
        union = request.query_params.get('union')
        is_best = request.query_params.get('filter', None)
        data = []
        if union and union.isdigit():
            responds = Request.objects.filter(union__id=union)
            if is_best == "love":
                responds = responds.filter(is_best=True)
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
        # If Authorization header contains a Bearer token, decode and validate it
        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '')
        payload = None
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ', 1)[1].strip()
            try:
                payload = decode_jwt(token)
            except AuthenticationFailed as e:
                # Raised when token is invalid or expired
                raise ValidationError(str(e))
        if payload:
            user = get_object_or_404(User, id=payload.get('nid'))
        else:
            raise ValidationError("Authentication credentials were not provided or invalid.")

        if union:
            request.data['requested_citizen'] = user.id
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


class RespondDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            respond = Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            return Response(
                {"success": False, "message": "Respond not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RespondListSerializer(respond)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )


class RespondImageListView(APIView):
    def get(self, request, respond_id):
        images = RespondImage.objects.filter(respond_id=respond_id)
        serializer = RespondImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ActivityListView(APIView):
    """
    API to return a list of dummy activities with separate date and time in BD time (12-hour format with AM/PM)
    """
    def get(self, request, respond_id):
        bd_tz = timezone('Asia/Dhaka')
        dummy_activities = [
            {"id": 1002, "user": "Zisan Islam", "action": "Created a request", "timestamp": datetime.now()},
            {"id": 1002, "user": "Zisan Islam", "action": "Uploaded a image", "timestamp": datetime.now() - timedelta(hours=1)},
            {"id": 2001, "user": "Razzak", "action": "The member Accepted this respond", "timestamp": datetime.now() - timedelta(days=1)},
            {"id": 2001, "user": "Razzak", "action": "On going to find best solution", "timestamp": datetime.now() - timedelta(days=1)},
            {"id": 1001, "user": "Shahadot Hosen", "action": "Given a solution", "timestamp": datetime.now() - timedelta(days=1)},
            {"id": 2001, "user": "Razzak", "action": "Analyzis this solution", "timestamp": datetime.now() - timedelta(days=1)},
        ]
        activities = []
        for activity in dummy_activities:
            bd_time = activity["timestamp"].astimezone(bd_tz)
            activities.append({
                "id": activity["id"],
                "user": activity["user"],
                "action": activity["action"],
                "date": bd_time.strftime("%Y-%m-%d"),
                "time": bd_time.strftime("%I:%M %p"),
            })
        return Response(activities, status=status.HTTP_200_OK)
