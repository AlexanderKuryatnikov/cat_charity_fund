from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject, Donation


async def new_donation_investment(
        new_donation: Donation,
        session: AsyncSession,
) -> None:
    amount_left = new_donation.full_amount
    active_projects = await charity_project_crud.get_active(session)
    for project in active_projects:
        amount_to_invest = project.full_amount - project.invested_amount
        if amount_to_invest >= amount_left:
            project.invested_amount += amount_left
            if amount_to_invest == amount_left:
                project.fully_invested = True
                project.close_date = datetime.now()
            new_donation.invested_amount = new_donation.full_amount
            new_donation.fully_invested = True
            new_donation.close_date = datetime.now()
            break
        else:
            project.invested_amount = project.full_amount
            project.fully_invested = True
            project.close_date = datetime.now()
            new_donation.invested_amount += amount_to_invest
            amount_left -= amount_to_invest
