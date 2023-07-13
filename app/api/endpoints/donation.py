from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from app.schemas.donation import DonationUserDB, DonationSuperUserDB, DonationCreate
from app.crud.donation import donation_crud
from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.models.user import User
from app.services.investing import check_projects_for_charity


router = APIRouter()


@router.post('/',
             response_model=DonationUserDB,
             response_model_exclude_none=True,
             )
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    new_donation = await check_projects_for_charity(donation, session)
    new_donation = await donation_crud.create(new_donation, session, user)
    return new_donation


@router.get(
    '/my',
    response_model=List[DonationUserDB],
    response_model_exclude={'user_id'},
)
async def get_all_user_donation(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    donations = await donation_crud.get_by_user(session, user=user)
    return donations


@router.get(
    '/',
    response_model=List[DonationSuperUserDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    donations = await donation_crud.get_multi(session)
    return donations
