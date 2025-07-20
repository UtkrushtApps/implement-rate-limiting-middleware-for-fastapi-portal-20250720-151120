from fastapi import Request, HTTPException, status, Depends

def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    # In a real app, get user from database or token
    return "testuser"
