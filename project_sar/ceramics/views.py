from typing import List  # , Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from models import scoped_session_dependency
from schemas import (
    SObjectStudy,
    SObjectStudyOut,
    SPackage,
    SVesselTypes,
    SPackageOut,
    SPartPot,
    SColorAfterFiring,
    SAnalogyOut,
    SAnalogy,
)
from schemas.package import SPackageOutFull, SPackageAnalogies
from . import crud

router = APIRouter(
    tags=["Ceramics"],
)


@router.get("/object_study/", response_model=List[SObjectStudyOut])
async def get_objects(
    session: AsyncSession = Depends(scoped_session_dependency),
) -> list[SObjectStudyOut]:
    return await crud.get_objects_study(session)


@router.post(
    "/object_study/",
    response_model=SObjectStudyOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "model": SObjectStudyOut,
        }
    },
)
async def add_object_study(
    object_study_in: SObjectStudy,
    session: AsyncSession = Depends(scoped_session_dependency),
):
    return await crud.create_object_study(session, object_study_in)


@router.get(
    "/object_study/get_by_id/{object_study_id}/", response_model=SObjectStudyOut
)
async def get_object_study_by_id(
    object_study_id: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> SObjectStudyOut:
    object_study = await crud.get_object_study_by_id(session, object_study_id)
    if object_study:
        return object_study
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Object of study id={object_study_id} doesn't exist",
    )


@router.put("/object_study/update_object_study/{object_study_id}/")
async def update_object_study(
    object_study_id: int,
    object_study_new: SObjectStudy,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> dict:
    if await get_object_study_by_id(object_study_id, session):
        object_study = await crud.update_object_study(
            session, object_study_id, object_study_new
        )
        if object_study:
            return {
                "message": f"Object of study id={object_study_id} updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Object of study id={object_study_id} doesn't exist",
    )


@router.get("/package/", response_model=List[SPackageOutFull])
async def get_packages(
    session: AsyncSession = Depends(scoped_session_dependency),
) -> list[SPackageOutFull]:
    return await crud.get_packages(session)


@router.post(
    "/package/",
    # response_model=SPackageOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "model": SPackageOut,
        }
    },
)
async def add_package(
    package_in: SPackage,
    vessel_types_in: SVesselTypes,
    part_port_in: SPartPot,
    color_firing_in: SColorAfterFiring,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> dict:
    package = await crud.create_package(
        session=session,
        package_in=package_in,
        vessel_types_in=vessel_types_in,
        part_port_in=part_port_in,
        color_firing_in=color_firing_in,
    )
    if package:
        return {"message": "Package added successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Package doesn't added"
    )


@router.get("/package/get_by_obj_id/{obj_id}/", response_model=list[SPackageOutFull])
async def get_packages_by_obj_id(
    obj_id: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> list[SPackageOutFull]:
    packages = await crud.get_packages_by_obj_id(session, obj_id)
    if packages:
        return packages
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Packages object id={obj_id} doesn't added",
    )


@router.get("/package/get_by_id/{package_id}/", response_model=SPackageOut)
async def get_package_by_id(
    package_id: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> SPackageOut:
    package = await crud.get_package_by_id(session, package_id)
    if package:
        return package
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Package id={package_id} doesn't exist",
    )


@router.get("/package/get_by_id_full/{package_id}/", response_model=SPackageOutFull)
async def get_package_by_id_full(
    package_id: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> SPackageOut:
    package = await crud.get_package_by_id_full(session, package_id)
    if package:
        return package
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Package id={package_id} doesn't exist",
    )


@router.put("/package/update_package/{package_id}/")
async def update_package(
    package_id: int,
    package_new: SPackage,
    vessel_types_new: SVesselTypes,
    part_port_new: SPartPot,
    color_firing_new: SColorAfterFiring,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> dict:
    if await crud.get_package_by_id_full(session, package_id):
        package = await crud.update_package(
            session=session,
            package_id=package_id,
            package_new=package_new,
            vessel_types_new=vessel_types_new,
            part_port_new=part_port_new,
            color_firing_new=color_firing_new,
        )
        if package:
            return {"message": f"Package id={package_id} update successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Package doesn't update"
    )


@router.get("/analogy/", response_model=List[SAnalogyOut])
async def get_analogies(
    session: AsyncSession = Depends(scoped_session_dependency),
) -> list[SAnalogyOut]:
    return await crud.get_analogy(session)


@router.post("/analogy/", status_code=status.HTTP_201_CREATED)
async def create_analogy(
    analogy_in: SAnalogy, session: AsyncSession = Depends(scoped_session_dependency)
) -> dict:
    analogy = await crud.create_analogy(
        session=session,
        analogy_in=analogy_in,
    )
    if analogy:
        return {"message": "Analogy added successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Analogy doesn't added"
    )


@router.get("/analogy/get_by_id/{analogy_id}/", response_model=SAnalogyOut)
async def get_analogy_by_id(
    analogy_id: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> SAnalogyOut:
    analogy = await crud.get_analogy_by_id(session, analogy_id)
    if analogy:
        return analogy
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Analogy id={analogy_id} doesn't exist",
    )


@router.post("/packages_analogies/", status_code=status.HTTP_201_CREATED)
async def create_association_layers_analogies(
    analogy_id: int,
    layer_number: int,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> dict:
    # analogy = await get_analogy_by_id(analogy_id, session)
    result = await crud.create_association_package_analogy(
        session=session,
        analogy_id=analogy_id,
        layer_number=layer_number,
    )
    if result > 0:
        return {"message": "Associations added successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Association analog id {analogy_id}, layer number {layer_number} doesn't added",
    )


@router.get("/layers-analogies/", response_model=List[SPackageAnalogies])
async def show_layers_analogies(
    session: AsyncSession = Depends(scoped_session_dependency),
) -> list[SPackageAnalogies]:
    return await crud.show_layers_analogies(session)


@router.put("/analogy/update_analogy/{analogy_id}/")
async def update_analogy(
    analogy_id: int,
    analogy_new: SAnalogy,
    session: AsyncSession = Depends(scoped_session_dependency),
) -> dict:
    if await get_analogy_by_id(analogy_id, session):
        analogy = await crud.update_analogy(session, analogy_id, analogy_new)
        if analogy:
            return {"message": f"Analogy id {analogy_id} updated successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Analogy id={analogy_id} doesn't exist",
    )
