from fastapi import APIRouter

from database import get_session, User
from models.user.user_get_dto import UserGetDto
from models.user.user_post_dto import UserPostDto
from models.user.user_put_dto import UserPutDto

user_router = APIRouter(
    prefix="/user",
    tags=["user"])


@user_router.post("/", response_model=UserGetDto)
def create_user(user_dto: UserPostDto):
    session = get_session()
    # new_user = User(login=user_dto.login,
    #                 password=user_dto.password,
    #                 first_name=user_dto.first_name,
    #                 middle_name=user_dto.middle_name,
    #                 last_name=user_dto.last_name,
    #                 email=user_dto.email)
    new_user = User(**user_dto.model_dump())
    session.add(new_user)
    session.commit()
    response = UserGetDto(**new_user.to_dict())
    session.close()
    return response


@user_router.get("/", response_model=UserGetDto)
def get_user(id: int):
    session = get_session()
    user = session.query(User).get(id)
    response = UserGetDto(**user.to_dict())
    session.close()
    return response


@user_router.put("/", response_model=UserGetDto)
def put_user(id: int, user_dto: UserPutDto):
    session = get_session()
    user = session.query(User).get(id)
    user.update_by_pydantic(user_dto)
    session.commit()
    response = UserGetDto(**user.to_dict())
    session.close()
    return response


@user_router.delete("/")
def delete_user(id: int):
    session = get_session()
    user = session.query(User).get(id)
    session.delete(user)
    session.commit()
    session.close()
