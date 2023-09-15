from django.utils.translation import gettext_lazy as _


AGENCY = "AGENCY"
AGRICULTURE = "AGRICULTURE"
ART = "ART AND DESIGN"
AUTOMOTIVE = "CONSTRUCTION"
CONSULTING = "CONSULTING"
EDUCATION = "EDUCATION"

INDUSTRY_TYPE = (
    (AGENCY, _("AGENCY")),
    (AGRICULTURE, _("AGRICULTURE")),
    (ART, _("ART")),
    (AUTOMOTIVE, _("AUTOMOTIVE")),
    (CONSULTING, _("CONSULTING")),
    (EDUCATION, _("EDUCATION")),
)

FREELANCING = "FREELANCING"
NGO = "NGO"
PROFIT_BUSINESS = "PROFIT BUSINESS"

BUSINESS_TYPE = (
    (FREELANCING, _("FREELANCING")),
    (NGO, _("NGO")),
    (PROFIT_BUSINESS, _("PROFIT_BUSINESS")),
)

CURRENCY_CHOICE = (
    (FREELANCING, _("FREELANCING")),
    (NGO, _("NGO")),
    (PROFIT_BUSINESS, _("PROFIT_BUSINESS")),
)

BLUE = "Blue"
RED = "Red"
GREEN = "Green"
PURPLE = "Purple"

COLOR_CHOICE = (
    (BLUE, _("BLUE")),
    (RED, _("RED")),
    (GREEN, _("GREEN")),
    (PURPLE, _("PURPLE")),
)
