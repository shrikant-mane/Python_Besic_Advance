import time
import jwt
#
# def validate_token(payload):
#     if not isinstance(payload, dict):
#         return False
#
#     if 'user_id' not in payload:
#         return False
#
#     if 'role' not in payload:
#         return False
#
#     if 'exp' not in payload:
#         return False
#
#     # validate values
#     if payload['user_id'] is None or payload['role'] is None:
#         return False
#
#     if time.time() > payload['exp']:
#         return False
#
#     return True
#
#
# def authorize(payload, required_role):
#     if payload['role'] != required_role:
#         return False
#     return True
#
# exp_time = time.time() + 5
# token_payload = {
#     "user_id": 101,
#     "role": "admin",
#     "exp": exp_time
# }
#
# time.sleep(5)
#
# print(validate_token(token_payload))
# print(authorize(token_payload, required_role="admin"))



SECRET_KEY = 'my-secret-key'
ALGORITHM = 'HS256'

def create_token():
    try:

        payload = {
            'user_id': 101,
            'role': 'admin',
            'exp': int(time.time()) + 3600,
        }
    except Exception as err:
        raise err

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except jwt.ExpiredSignatureError as err:
        raise err

    except jwt.InvalidSignatureError as err:
        raise err

    except jwt.InvalidTokenError as err:
        raise err


token = create_token()
print(token)

payload = verify_token(token)
print(payload)