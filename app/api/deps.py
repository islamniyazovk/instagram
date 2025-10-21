from fastapi import HTTPException
from starlette import status
from starlette.requests import Request


async def check_auth(request: Request) -> int:
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    print(token)
