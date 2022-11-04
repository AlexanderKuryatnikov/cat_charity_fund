from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectCreate, CharityProjectUpdate


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
]):

    async def update(
            self,
            db_charity_project: CharityProject,
            charity_project_in: CharityProjectUpdate,
            session: AsyncSession,
    ) -> CharityProject:
        charity_project_data = jsonable_encoder(db_charity_project)
        update_data = charity_project_in.dict(exclude_unset=True)

        for field in charity_project_data:
            if field in update_data:
                setattr(db_charity_project, field, update_data[field])
        session.add(db_charity_project)
        await session.commit()
        await session.refresh(db_charity_project)
        return db_charity_project

    async def remove(
            self,
            db_charity_project: CharityProject,
            session: AsyncSession,
    ) -> CharityProject:
        await session.delete(db_charity_project)
        await session.commit()
        return db_charity_project
