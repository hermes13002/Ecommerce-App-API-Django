from rest_framework.views import APIView  # Importing APIView for handling API requests
from rest_framework.response import Response  # Importing Response for sending API responses
from rest_framework import status  # Importing status for HTTP status codes
from .serializers import RegisterSerializer, LoginSerializer  # Importing the serializers
from rest_framework_simplejwt.tokens import RefreshToken  # Importing RefreshToken for generating tokens

# View for user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            user = serializer.save()  # Save the new user
            refresh = RefreshToken.for_user(user)  # Generate a token for the user
            return Response(
                {
                    "message": "User registered successfully",
                    "username": serializer.data['username'],
                    "first_name": serializer.data['first_name'],
                    "last_name": serializer.data['last_name'],
                    "email": serializer.data['email'],
                    "phonenumber": serializer.data['phonenumber'],
                    "address": serializer.data['address'],
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                }, 
                status=status.HTTP_201_CREATED
            )  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid


# View for user login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            user = serializer.validated_data["user"]  # Get the user object from validated data
            refresh = RefreshToken.for_user(user)  # Generate a token for the user
            return Response(
                {
                    "message": "Login successful",
                    "username": user.username,  # Access username from the user object
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phonenumber": user.phonenumber,
                    "address": user.address,
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                },
                status=status.HTTP_200_OK
            )  # Return success response with user details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid

