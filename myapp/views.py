import jwt
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .serializers import ImageSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Image
from django.core import serializers

from rest_framework import viewsets
from rest_framework import generics

# login fucntion
@api_view(["POST"])
def user_auth(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User Not Found")
        if not user.check_password(password):
            raise AuthenticationFailed("Password is not valid")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        return Response(
            {
                "message": "Login Successfully",
                "jwt": token,
            }
        )
    except Exception as e:
        e = str(e)

        return Response(
            {
                "message": "Login Failed",
                "error": e,
            }
        )

# get users list
@api_view(["GET"])
def user_list(request):
    try:
        all_users = User.objects.all()
        # Serialize a QuerySet
        data = serializers.serialize('json', all_users)
        print(all_users)
        return Response(
            {data}
        )
    except Exception as e:
        e = str(e)

        return Response(
            {
                "message": "Errror",
                "error": e,
            }
        )



# user registraion
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer 

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer       

  

# def upload_image
@api_view(['POST'])
# @permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def upload_image(request):
    request_data = request.data
    request_data["User"] = request_data["user_id"]

    # Create an Image object and associate it with the user    
    serializer = ImageSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(status=400)