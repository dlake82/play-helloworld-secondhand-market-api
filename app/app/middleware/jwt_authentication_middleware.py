from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


from ..utils.log import log


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 쿠키에서 JWT 토큰 데이터를 읽기
        access_token_value = request.COOKIES.get("access")

        if access_token_value:
            try:
                # JWT 토큰을 디코딩하여 사용자 데이터를 가져옴
                access_token = AccessToken(access_token_value)
                user = access_token.payload.get("user_id")

                # HTTP Authorization 헤더에 JWT ACCESS 헤더 추가
                request.META["Authorization"] = f"Bearer {access_token_value}"
                print("Authorization")
            except Exception as e:
                # JWT 토큰 디코딩 실패
                log.info("Failed to decode JWT token")
                pass

        response = self.get_response(request)

        return response
