from django.urls import re_path
from django.http import JsonResponse


def openid_configuration(request):
    return JsonResponse(
        {
            'issuer': 'https://awx.example.com',
            'jwks_uri': 'https://awx.example.com/job_tokens/.well-known/jwks',
            'response_types_supported': [
                'id_token',
            ],
            'subject_types_supported': [
                'public',
            ],
            'id_token_signing_alg_values_supported': [
                'RS256',
            ],
            'scopes_supported': [
                'openid',
            ],
            'claims_supported': [
                'sub',
                'aud',
                'exp',
                'iat',
                'iss',
                'job_id',
            ],
        }
    )


urls = [
    re_path(r'^job_tokens/.well-known/openid-configuration$', openid_configuration, name='tokens_server_configuration'),
]

__all__ = ['urls']
