class ProviderStatsResponse:
    def __init__(self,
                 hcpcs_code,
                 hcpcs_description,
                 avg_medicare_pay_amount_per_service,
                 avg_submitted_charged_per_service,
                 avg_medicare_allowed_amount_per_service):
        self.hcpcs_code = hcpcs_code
        self.hcpcs_description = hcpcs_description
        self.avg_medicare_pay_amount_per_service = avg_medicare_pay_amount_per_service
        self.avg_submitted_charged_per_service = avg_submitted_charged_per_service
        self.avg_medicare_allowed_amount_per_service = avg_medicare_allowed_amount_per_service
