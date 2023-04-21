from allauth.account.utils import send_email_confirmation
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from rest_auth.app_settings import PasswordChangeSerializer
from rest_auth.serializers import PasswordResetConfirmSerializer
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_auth.serializers import PasswordResetConfirmSerializer
from rest_auth.views import sensitive_post_parameters_m, PasswordChangeView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from allauth.account.models import EmailAddress, EmailConfirmation
from allauth.account.utils import send_email_confirmation
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@swagger_auto_schema(
    request_body=openapi.Schema(
        title="Name",
        type=openapi.TYPE_OBJECT,
        properties={'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING)}),
    operation_summary='update user profile', methods=['POST'])
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_user(request):
    """
    post:
    Update user profile
    """
    first_name = request.data["first_name"] if "first_name" in request.data else None
    last_name = request.data["last_name"] if "last_name" in request.data else None
    user = request.user
    if first_name is None or first_name == "":
        pass
    else:
        user.first_name = first_name
    if last_name is None or last_name == "":
        pass
    else:
        user.last_name = last_name
    user.save()
    return Response({"detail": "Name updated."})


@swagger_auto_schema(operation_summary='send verification email', methods=['POST'])
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def send_verification_email(request):
    """
    post:
    Send verification email
    """
    send_email_confirmation(request, request.user)
    return Response({"detail": "Verification email sent"})


@swagger_auto_schema(operation_summary='delete user account', methods=['DELETE'])
@api_view(["DELETE"])
@permission_classes([IsAuthenticated, ])
def delete_user(request):
    """
    delete:
    Delete user account
    """
    user = request.user
    try:
        user.delete()
    # catch-all exception
    # if not logged in, the authentication wrapper should return 403 instead
    except Exception:
        return Response({"detail": "User cannot be deleted"}, status=status.HTTP_400_BAD_REQUEST)
    # return success if deletion successful
    return Response({"detail": "User has been deleted"})


@swagger_auto_schema(
    request_body=openapi.Schema(
        title="Name",
        type=openapi.TYPE_OBJECT,
        properties={'new_password1': openapi.Schema(type=openapi.TYPE_STRING),
                    'new_password2': openapi.Schema(type=openapi.TYPE_STRING),
                    'token': openapi.Schema(type=openapi.TYPE_STRING),
                    'uid': openapi.Schema(type=openapi.TYPE_STRING)}),
    operation_summary='Reset password', methods=['POST'])
@api_view(["POST"])
@permission_classes([AllowAny, ])
def forget_password(request):
    serializer_class = PasswordResetConfirmSerializer
    serializer = serializer_class(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(
            {"detail": "Password has been reset with the new password."}, status=status.HTTP_200_OK
        )
    except ValidationError:
        error_msgs = []
        error_code = []
        exception = str(ValidationError(serializer.errors))
        for msg in exception.split(":")[1].split("ErrorDetail"):
            if msg.__contains__("string"):
                error_msgs.append(msg.split(",")[0].split("=")[1].split("'")[1])
        for err in error_msgs:
            if err == 'This password is too short. It must contain at least 8 characters.':
                error_code.append(1)
            elif err == 'This password is too common.':
                error_code.append(2)
            elif err == 'This password is entirely numeric.':
                error_code.append(3)
            elif err == 'This field may not be blank.':
                error_code.append(4)
            elif err == 'The two password fields didn’t match.':
                error_code.append(5)
            else:
                error_code.append(6)  # Unknown error, please try again
        return JsonResponse({'Message': error_code}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated, ])
def reset_password(request):
    serializer_class = PasswordChangeSerializer
    serializer = serializer_class(data=request.data)
    try:
        serializer.user = getattr(request, 'user', None)
        serializer.is_valid(raise_exception=True)
        serializer.set_password_form.save()
        print('success')
        return JsonResponse({"detail": "New password has been saved."}, status=status.HTTP_200_OK)
    except ValidationError:
        error_msgs = []
        error_code = []
        exception = str(ValidationError(serializer.errors))
        for msg in exception.split(":")[1].split("ErrorDetail"):
            if msg.__contains__("string"):
                error_msgs.append(msg.split(",")[0].split("=")[1].split("'")[1])
        for err in error_msgs:
            if err == 'This password is too short. It must contain at least 8 characters.':
                error_code.append(1)
            elif err == 'This password is too common.':
                error_code.append(2)
            elif err == 'This password is entirely numeric.':
                error_code.append(3)
            elif err == 'This field may not be blank.':
                error_code.append(4)
            elif err == 'The two password fields didn’t match.':
                error_code.append(5)
            elif err == 'Invalid password':
                error_code.append(6)
            else:
                error_code.append(7)  # Unknown error, please try again
        return JsonResponse({'Message': error_code}, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(["POST"])
    # @permission_classes([AllowAny, ])
    # def resend_email_confirmation(request):
    #     # 获取当前用户对象
    #     user = request.user
    #
    #     # 获取当前用户的未确认的电子邮件
    #     email = user.emailaddress_set.get(primary=True)
    #
    #     # 如果当前电子邮件已经确认，则返回错误信息
    #     if email.verified:
    #         return HttpResponseBadRequest('Your email address has already been verified.')
    #
    #     # 获取当前电子邮件的确认对象
    #     email_confirmation = EmailConfirmation.objects.filter(email_address=email).first()
    #
    #     # 如果不存在对应的确认对象，则返回错误信息
    #     if not email_confirmation:
    #         return HttpResponseBadRequest('Invalid email address.')
    #
    #     # 调用 send_email_confirmation 函数重新发送验证邮件
    #     send_email_confirmation(request, email_confirmation)
    #
    #     # 返回成功信息
    #     return HttpResponse('Verification email sent.')


# @csrf_exempt

@swagger_auto_schema(
    request_body=openapi.Schema(
        title="resend verification email",
        type=openapi.TYPE_OBJECT,
        properties={'email': openapi.Schema(type=openapi.TYPE_STRING)}),
    operation_summary='Reset password', methods=['POST'])
@api_view(["POST"])
@permission_classes([AllowAny, ])
def resend_email_verification(request):
    email = request.data.get('email')
    if email:
        user = User.objects.filter(email=email).first()
        if user:
            send_email_confirmation(request, user)
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'})
    # try:

    #     # email_address = EmailAddress.objects.get(user=request.user, email=email)
    #     email_address = EmailAddress.objects.get(email=email)
    # except EmailAddress.DoesNotExist:
    #     return JsonResponse({'error': 'Email address not found.'}, status=400)
    # if email_address.verified:
    #     return JsonResponse({'error': 'Email address already verified.'}, status=400)
    # send_email_confirmation(request, email_address)
    # return JsonResponse({'success': 'Verification email sent.'})

