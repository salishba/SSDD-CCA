import jwt

token = jwt.encode(
    {"user_id": 999},
    "hardcoded_secret_123",
    algorithm="HS256"
)

print(token)