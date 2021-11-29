from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_connection
import provider_service

app = FastAPI()


@app.get("/provider-service-stats/hcpcs_code/{hcpcs_code}", status_code=200)
def find_provider_service_stats_by_hcpcs_code(hcpcs_code: str,
                                              db: Session = Depends(get_connection)):
    return provider_service.find_stats_by_key(db=db,
                                              stats_key=hcpcs_code)


@app.get("/provider-service-stats/hcpcs_code/{hcpcs_code}/city/{city}", status_code=200)
def find_provider_service_stats_by_hcpcs_code_and_city(hcpcs_code: str,
                                                       city: str,
                                                       db: Session = Depends(get_connection)):
    return provider_service.find_stats_by_key(db=db,
                                              stats_key='%s_%s' % (hcpcs_code, city))


@app.get("/provider-service-stats/hcpcs_code/{hcpcs_code}/country/{country_code}", status_code=200)
def find_provider_service_stats_by_hcpcs_code_and_country(hcpcs_code: str,
                                                          country_code: str,
                                                       db: Session = Depends(get_connection)):
    return provider_service.find_stats_by_key(db=db,
                                              stats_key='%s_%s' % (hcpcs_code, country_code))


@app.get("/provider-service-stats/hcpcs_code/{hcpcs_code}/state/{state_code}", status_code=200)
def find_provider_service_stats_by_hcpcs_code_and_country(hcpcs_code: str,
                                                          state_code: str,
                                                          db: Session = Depends(get_connection)):
    return provider_service.find_stats_by_key(db=db,
                                              stats_key='%s_%s' % (hcpcs_code, state_code))

