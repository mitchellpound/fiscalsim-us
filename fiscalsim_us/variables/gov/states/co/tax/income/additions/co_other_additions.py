from fiscalsim_us.model_api import *


class co_other_additions(Variable):
    """
    Other additions to income DR 0104 form line 6
    These additions include the following:
    - Bond interest (non-Colorado state/ municipal)
    - Charitable gross conservation easement
    - Alien labor
    - Partnership/ Fiduciarty
    - Any expenses incurred by a taxpayer with respect
    to expenditures made at, or payments made to,
    a club that restrics membership on the basis of sex,
    sexual orientation, gender identity, gender expression,
    marital status, race, creed, religion, color, ancestry,
    or national origin.
    - Distributions from a medical savings account not made
    for an eligible expense
    - Federal deduction for food and beverage expenses
    """
    value_type = float
    entity = TaxUnit
    label = "Colorado other additions to income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
