from rest_framework import viewsets,status
from rest_framework.decorators import api_view,action
from .serializers import UserRegSerializers,LoginSerializers,User,Company,CompanySerializers,CompanyApprentice,CompanyApprenticeSerializer,UserSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

class CompanyApprenticeView(viewsets.ModelViewSet):
    serializer_class=CompanyApprenticeSerializer
    queryset=CompanyApprentice.objects.all()
    
class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all()

class UserRegView(viewsets.ModelViewSet):
    serializer_class=UserRegSerializers
    queryset=User.objects.all()
    
    def create(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # This creates and saves the user instance

        # If you want to set the password separately (not recommended, as it's handled in the serializer)
        user.set_password(request.data.get('password'))
        user.save()
        return Response(
            serializer.data,status=status.HTTP_201_CREATED
        )

    @action(detail=False,methods=['PUT'])
    def password_rest(self, request, *args, **kwargs):
        username=request.data.get('username')
        user=User.objects.filter(username=username).first()
        if user is not None:
            user.set_password(request.data.get('password'))
            user.save()
            return Response(
                {
                    'success':'Password updated successfully',
                },status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {
                'invalid':'user does not exist'
            },status=status.HTTP_400_BAD_REQUEST
        ) 
    def perform_update(self, serializer):
        return serializer.save()
    
    def delete(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
    
    # def list(self, request, *args, **kwargs):
    #     raise MethodNotAllowed('GET')
    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLogin(viewsets.ModelViewSet):
    serializer_class=LoginSerializers
    queryset=User.objects.all()
    
    def get_serializer_class(self):
        if self.action=="create":
            return self.serializer_class
        if self.action=="login_view":
            return UserSerializers
        
    def create(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            tokens=get_tokens_for_user(user)
            return Response({
                'tokens':tokens,
                'user':user.id,
                'company':user.company.name
                    },status=status.HTTP_200_OK)
        else:
            return Response({
            'error':'invalid credentials'
            },status=status.HTTP_400_BAD_REQUEST)
    


    def perform_create(self, serializer):
        return serializer.save()
    
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')
    
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
    
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')
    

    @action(detail=False,methods=['POST'])   
    def login_view(request):
        if request.method == 'POST':
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                tokens = get_tokens_for_user(user)
                serializer = UserSerializers(user)
                user_data = serializer.data
                return Response({
                    'tokens': tokens,
                    'user': user_data,
                    'company': user.company.name if hasattr(user, 'company') else None
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            tokens = get_tokens_for_user(user)
            user_serializer = UserSerializers(user)
            # print(user.company.all())
            comp_serializer=CompanySerializers(user.company.all())
            user_data = user_serializer.data
            companies = user.company.all()

    # Serialize the companies
            company_serializers = CompanySerializers(companies, many=True)
            company_data = company_serializers.data

            return Response({
                # 'tokens': tokens,
                'user': user_data,
                'companies': company_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
   