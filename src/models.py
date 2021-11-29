from sqlalchemy import Column, Integer, String, Float

from database import Base


class ProviderServiceStats(Base):
    __tablename__ = "provider_service_stats"

    id = Column(Integer, primary_key=True, index=True)
    hcpcs_code = Column(String, index=True)
    hcpcs_description = Column(String)
    stats_key = Column(String, index=True)
    total_services = Column(Integer)
    avg_submitted_charged = Column(Float)
    avg_medicare_pay_amount = Column(Float)
    avg_medicare_allowed_amount = Column(Float)
