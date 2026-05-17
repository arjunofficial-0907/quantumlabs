from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from cloudinary.uploader import upload

from app.auth.dependencies import (
    admin_required
)

from app.utils.response import (
    success_response
)

router = APIRouter(
    prefix="/api/uploads",
    tags=["Uploads"]
)


@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    current_user = Depends(admin_required)
):

    allowed_types = [
        "image/png",
        "image/jpeg",
        "image/webp"
    ]

    if file.content_type not in allowed_types:

        raise HTTPException(
            status_code=400,
            detail="Invalid image format"
        )

    result = upload(
        file.file,
        folder="quantum-labs"
    )

    return success_response(
        "Image uploaded successfully",
        {
            "url": result["secure_url"]
        }
    )