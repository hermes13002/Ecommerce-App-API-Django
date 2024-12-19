from rest_framework.views import APIView  # Importing APIView for handling API requests
from rest_framework.response import Response  # Importing Response for sending API responses
from rest_framework import status  # Importing status for HTTP status codes
from .serializers import RegisterSerializer, LoginSerializer  # Importing the serializers

# View for user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new user
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid

# View for user login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid