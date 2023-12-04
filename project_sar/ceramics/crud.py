from sqlalchemy import select, Result, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload, load_only

from models import (
    ObjectStudy,
    Package,
    VesselType,
    PartPot,
    ColorAfterFiring,
    Analogy,
)
from schemas import (
    SObjectStudy,
    SPackage,
    SVesselTypes,
    SPartPot,
    SColorAfterFiring,
    SAnalogy,
)


async def create_object_study(
    session: AsyncSession,
    object_study_in: SObjectStudy,
) -> ObjectStudy:
    object_study = ObjectStudy(**object_study_in.model_dump())
    session.add(object_study)
    await session.commit()
    return object_study


async def get_objects_study(session: AsyncSession) -> list[ObjectStudy]:
    stmt = select(ObjectStudy).order_by(ObjectStudy.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_object_study_by_id(
    session: AsyncSession, obj_id: int
) -> ObjectStudy | None:
    return await session.get(ObjectStudy, obj_id)


async def create_package(
    session: AsyncSession,
    package_in: SPackage,
    vessel_types_in: SVesselTypes,
    part_port_in: SPartPot,
    color_firing_in: SColorAfterFiring,
):
    if not get_object_study_by_id(session, package_in.object_study_id):
        return None
    package = Package(**package_in.model_dump())
    session.add(package)
    try:
        await session.commit()
    except IntegrityError:
        return None
    await create_vessel_types(
        session=session, package_id=package.id, vessel_types_in=vessel_types_in
    )
    await create_part_pot(
        session=session, package_id=package.id, part_port_in=part_port_in
    )
    await create_color_firing(
        session=session, package_id=package.id, color_firing_id=color_firing_in
    )
    return package


async def create_vessel_types(
    session: AsyncSession,
    package_id: int,
    vessel_types_in: SVesselTypes,
) -> None:
    vessel_types = VesselType(package_id=package_id, **vessel_types_in.model_dump())
    session.add(vessel_types)
    await session.commit()


async def create_part_pot(
    session: AsyncSession,
    package_id: int,
    part_port_in: SPartPot,
) -> None:
    part_port = PartPot(package_id=package_id, **part_port_in.model_dump())
    session.add(part_port)
    await session.commit()


async def create_color_firing(
    session: AsyncSession,
    package_id: int,
    color_firing_id: SColorAfterFiring,
) -> None:
    color_firing = ColorAfterFiring(
        package_id=package_id, **color_firing_id.model_dump()
    )
    session.add(color_firing)
    await session.commit()


async def get_packages(session: AsyncSession) -> list[Package]:
    stmt = (
        select(Package)
        .options(joinedload(Package.vessel_types))
        .options(joinedload(Package.part_of_the_pots))
        .options(joinedload(Package.color_after_firing))
        .order_by(Package.object_study_id, Package.id)
    )
    # stmt = select(Package).order_by(Package.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_packages_by_obj_id(
    session: AsyncSession, obj_id: int
) -> list[Package] | None:
    stmt = (
        select(Package)
        .where(Package.object_study_id == obj_id)
        .options(joinedload(Package.vessel_types))
        .options(joinedload(Package.part_of_the_pots))
        .options(joinedload(Package.color_after_firing))
        .order_by(Package.id)
    )
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_package_by_id(session: AsyncSession, package_id: int):
    return await session.get(Package, package_id)


async def get_package_by_id_full(
    session: AsyncSession, package_id: int
) -> Package | None:
    stmt = (
        select(Package)
        .where(Package.id == package_id)
        .options(joinedload(Package.vessel_types))
        .options(joinedload(Package.part_of_the_pots))
        .options(joinedload(Package.color_after_firing))
    )
    package = await session.execute(stmt)
    return package.scalar()


async def get_analogy(session: AsyncSession) -> list[Analogy]:
    stmt = select(Analogy).order_by(Analogy.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())


async def create_analogy(session: AsyncSession, analogy_in: SAnalogy) -> Analogy:
    analogy = Analogy(**analogy_in.model_dump())
    session.add(analogy)
    await session.commit()
    return analogy


async def get_analogy_by_id(session: AsyncSession, analogy_id: int) -> Analogy | None:
    return await session.get(Analogy, analogy_id)


async def update_object_study(
    session: AsyncSession, object_study_id: int, object_study_new: SObjectStudy
) -> bool:
    stmt = (
        update(ObjectStudy)
        .where(ObjectStudy.id == object_study_id)
        .values(**object_study_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()
    return True


async def create_association_package_analogy(
    session: AsyncSession,
    analogy_id: int,
    layer_number: int,
) -> int:
    analogy = await get_analogy_by_id(session=session, analogy_id=analogy_id)
    cnt = 0
    if analogy:
        stmt = (
            select(Package)
            .where(Package.layer_number == layer_number)
            .options(selectinload(Package.analogies))
            .order_by(Package.id)
        )

        packages = await session.scalars(stmt)
        for package in packages:
            if analogy not in package.analogies:
                package.analogies.append(analogy)
                cnt += 1
        await session.commit()
    return cnt


async def update_package(
    session: AsyncSession,
    package_id: int,
    package_new: SPackage,
    vessel_types_new: SVesselTypes,
    part_port_new: SPartPot,
    color_firing_new: SColorAfterFiring,
) -> bool:
    stmt = (
        update(Package)
        .where(Package.id == package_id)
        .values(**package_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()
    await update_vessel_types(session, package_id, vessel_types_new)
    await update_part_port(session, package_id, part_port_new)
    await update_color_firing(session, package_id, color_firing_new)
    return True


async def update_vessel_types(
    session: AsyncSession,
    package_id: int,
    vessel_types_new: SVesselTypes,
) -> None:
    stmt = (
        update(VesselType)
        .where(VesselType.package_id == package_id)
        .values(**vessel_types_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()


async def update_part_port(
    session: AsyncSession,
    package_id: int,
    part_port_new: SPartPot,
) -> None:
    stmt = (
        update(PartPot)
        .where(PartPot.package_id == package_id)
        .values(**part_port_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()


async def update_color_firing(
    session: AsyncSession,
    package_id: int,
    color_firing_new: SPartPot,
) -> None:
    stmt = (
        update(ColorAfterFiring)
        .where(ColorAfterFiring.package_id == package_id)
        .values(**color_firing_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()


async def show_layers_analogies(session: AsyncSession) -> list[Package]:
    stmt = (
        select(Package)
        .options(selectinload(Package.analogies))
        .options(load_only(Package.layer_number))
        .order_by(Package.layer_number)
    )
    packages = list(await session.scalars(stmt))
    layers = []
    result: list[Package] = []
    for package in packages:
        if package.layer_number not in layers:
            result.append(package)
            layers.append(package.layer_number)
    return result


async def update_analogy(session: AsyncSession, analogy_id: int, analogy_new: SAnalogy):
    stmt = (
        update(Analogy)
        .where(Analogy.id == analogy_id)
        .values(**analogy_new.model_dump())
    )
    await session.execute(stmt)
    await session.commit()
    return True
