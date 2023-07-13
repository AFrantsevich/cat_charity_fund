from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate,
                                         CharityProjectDB)
from app.crud.charity_project import charity_project_crud
from app.core.db import get_async_session
from app.api.validators import (check_charity_project_duplicate,
                                check_charity_project_exists_and_invested_amount)
from app.core.user import current_superuser
from services.investing import check_donations_for_charity


router = APIRouter()


@router.post('/',
             response_model=CharityProjectDB,
             response_model_exclude_none=True,
             dependencies=[Depends(current_superuser)]
             )
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    await check_charity_project_duplicate(charity_project.name, session)
    new_charity_project = await check_donations_for_charity(charity_project, session)
    new_charity_project = await charity_project_crud.create(
        new_charity_project, session)
    return new_charity_project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=False,
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    project = await check_charity_project_exists_and_invested_amount(
        project_id, session, flag=True)
    charity_project = await charity_project_crud.remove(project, session)
    return charity_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=False,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    project = await check_charity_project_exists_and_invested_amount(
        project_id, session, obj_in
    )

    if obj_in.name is not None:
        await check_charity_project_duplicate(obj_in.name, session)

    meeting_room = await charity_project_crud.update(
        project, obj_in, session
    )
    return meeting_room


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    charity_projects = await charity_project_crud.get_multi(session)
    return charity_projects
