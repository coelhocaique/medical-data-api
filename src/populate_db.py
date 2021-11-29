import csv

from database import get_connection
import provider_service


def execute():
    db = get_connection()

    stats_dict = dict()
    index = 0

    with open('./data/Medicare_Physician_Other_Practitioners_by_Provider_and_Service_2019.csv', encoding="ISO-8859-1") as csvFile:
        data = csv.DictReader(csvFile, delimiter=',')

        for row in data:
            city = row['Rndrng_Prvdr_City']
            state = row['Rndrng_Prvdr_State_Abrvtn']
            country_code = row['Rndrng_Prvdr_Cntry']
            hcpcs_code = row['HCPCS_Cd']
            hcpcs_description = row['HCPCS_Desc']
            total_services = int(row['Tot_Srvcs'].replace(",", "").replace(".", ""))
            avg_submitted_charged = float(row['Avg_Sbmtd_Chrg'].replace("$", "").replace(",", ""))
            avg_medicare_pay_amount = float(row['Avg_Mdcr_Pymt_Amt'].replace("$", "").replace(",", ""))
            avg_medicare_allowed_amount = float(row['Avg_Mdcr_Alowd_Amt'].replace("$", "").replace(",", ""))

            stats_dict_keys = [hcpcs_code,
                               '%s_%s' % (hcpcs_code, country_code),
                               '%s_%s' % (hcpcs_code, state),
                               '%s_%s' % (hcpcs_code, city)]

            for key in stats_dict_keys:
                stats_dict[key] = {
                    'total_services': total_services + stats_dict.get('total_services', 0),
                    'avg_submitted_charged': avg_submitted_charged + stats_dict.get('avg_submitted_charged', 0),
                    'avg_medicare_pay_amount': avg_medicare_pay_amount + stats_dict.get('avg_medicare_pay_amount', 0),
                    'avg_medicare_allowed_amount': avg_medicare_allowed_amount + stats_dict.get('avg_medicare_allowed_amount', 0),
                    'hcpcs_description': hcpcs_description,
                    'hcpcs_code': hcpcs_code,
                    'city': city,
                    'state': state,
                    'country_code': country_code
                }

            print('line %d processed' % index)
            index += 1

    for stats_key in stats_dict.keys():
        provider_service.create_stats(
            db=db,
            hcpcs_code=stats_dict[stats_key]['hcpcs_code'],
            hcpcs_description=stats_dict[stats_key]['hcpcs_description'],
            total_services=stats_dict[stats_key]['total_services'],
            avg_submitted_charged=stats_dict[stats_key]['avg_submitted_charged'],
            avg_medicare_pay_amount=stats_dict[stats_key]['avg_medicare_pay_amount'],
            avg_medicare_allowed_amount=stats_dict[stats_key]['avg_medicare_allowed_amount'],
            stats_key=stats_key
        )


execute()