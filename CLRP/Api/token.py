from rest_framework_simplejwt.tokens import RefreshToken


def generate_token(customer):
    refresh = RefreshToken.for_user(customer)
    access_token = refresh.access_token

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }
