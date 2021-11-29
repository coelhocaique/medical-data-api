from sqlalchemy.orm import Session

from models import ProviderServiceStats
from schemas import ProviderStatsResponse


def create_hcpcs_dict(db, hcpcs_code, hcpcs_description):
    existing_entity = db.query(HcpcsDict).filter(HcpcsDict.code == hcpcs_code).first()

    if existing_entity is not None:
        return existing_entity

    entity = HcpcsDict(code=hcpcs_code, description=hcpcs_description)
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


def create(db: Session,
           provider_id,
           hcpcs_code,
           hcpcs_description,
           total_benes,
           total_srvcs,
           avg_submitted_charged,
           avg_medicare_pay_amount,
           avg_medicare_allowed_amount):
    create_hcpcs_dict(db, hcpcs_code, hcpcs_description)

    provider_service = ProviderService(provider_id=provider_id,
                                       hcpcs_code=hcpcs_code,
                                       total_benes=total_benes,
                                       total_srvcs=total_srvcs,
                                       avg_submitted_charged=avg_submitted_charged,
                                       avg_medicare_pay_amount=avg_medicare_pay_amount,
                                       avg_medicare_allowed_amount=avg_medicare_allowed_amount)
    db.add(provider_service)
    db.commit()
    db.refresh(provider_service)
    return provider_service


def find_stats_by_key(db: Session, stats_key: str):
    result: ProviderServiceStats = db.query(ProviderServiceStats) \
        .filter(ProviderServiceStats.stats_key == stats_key) \
        .first()

    if result is not None:
        return ProviderStatsResponse(
            hcpcs_code=result.hcpcs_code,
            hcpcs_description=result.hcpcs_description,
            avg_medicare_pay_amount_per_service=round(result.avg_medicare_pay_amount / result.total_services, 2),
            avg_submitted_charged_per_service=round(result.avg_submitted_charged / result.total_services,2),
            avg_medicare_allowed_amount_per_service=round(result.avg_medicare_allowed_amount / result.total_services, 2)
        )
    else:
        return ProviderStatsResponse(
            hcpcs_code=None,
            hcpcs_description=None,
            avg_medicare_pay_amount_per_service=0,
            avg_submitted_charged_per_service=0,
            avg_medicare_allowed_amount_per_service=0
        )


def create_stats(db: Session,
                 hcpcs_code,
                 hcpcs_description,
                 stats_key,
                 total_services,
                 avg_submitted_charged,
                 avg_medicare_pay_amount,
                 avg_medicare_allowed_amount):
    entity = ProviderServiceStats(hcpcs_code=hcpcs_code,
                                  hcpcs_description=hcpcs_description,
                                  stats_key=stats_key,
                                  total_services=total_services,
                                  avg_submitted_charged=avg_submitted_charged,
                                  avg_medicare_pay_amount=avg_medicare_pay_amount,
                                  avg_medicare_allowed_amount=avg_medicare_allowed_amount)
    db.add(entity)
    db.commit()
    db.refresh(entity)
