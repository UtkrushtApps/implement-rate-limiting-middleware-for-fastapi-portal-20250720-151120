from fastapi import APIRouter, Depends, HTTPException, status, Request
from dependencies.auth import get_current_user

router = APIRouter()

@router.get("/auth-protected")
def protected_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": f"Authenticated as {current_user}"}
