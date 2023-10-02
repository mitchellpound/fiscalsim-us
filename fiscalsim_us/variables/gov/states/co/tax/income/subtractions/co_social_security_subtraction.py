from fiscalsim_us.model_api import *


class co_social_securty_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado social securtity subtraction from income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2022.pdf"
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.co.tax.subtractions
        # asuume that the head is receiving the social security beneifts
        age = tax_unit("age_head", period)
        taxable_ss_benefits = tax_unit("tax_unit_taxable_social_security", period)

        return where(
            age <= p.social_security_age_limit,
            min(taxable_ss_benefits, p.social_security_subctraction_limit),
            taxable_ss_benefits
        )
