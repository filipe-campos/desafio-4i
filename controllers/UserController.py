from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from utils.util import validate_cpf

import models
import crud
import schemas

router = APIRouter()

@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int,
                    current_user: models.User = Depends(deps.get_current_user),
                    db: Session = Depends(deps.get_db)) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=404, detail="User not found."
        )


@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(deps.get_db),
               skip: int = 0,
               limit: int = 100,
               current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)

    return users

@router.post("/", response_model=schemas.User, status_code=201)
def create_user(*,
                db: Session = Depends(deps.get_db),
                user_in: schemas.UserCreate) -> Any:
    """
    Create new user.
    """

    if not validate_cpf(user_in.cpf):
        raise HTTPException(
            status_code=400,
            detail="CPF is invalid.",
        )

    user = crud.user.get_by_cpf(db, cpf=user_in.cpf)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this cpf already exists in the system.",
        )

    user = crud.user.create(db, obj_in=user_in)

    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(*,
                db: Session = Depends(deps.get_db),
                user_id: int,
                user_in: schemas.UserUpdate,
                current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Update a user.
    """

    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    user = crud.user.update(db, db_obj=user, obj_in=user_in)

    return

@router.delete("/{user_id}", response_model=schemas.User)
def update_user(*,
                db: Session = Depends(deps.get_db),
                user_id: int,
                current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Update a user.
    """

    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    user = crud.user.delete(db, id=user_id)

    return user
