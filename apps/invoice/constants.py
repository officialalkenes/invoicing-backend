from django.utils.translation import gettext_lazy as _

FREQUENCY_CHOICES = [
    ("W", "Weekly"),
    ("BW", "Bi-Weekly"),
    ("M", "Monthly"),
    ("Q", "Quarterly"),
    ("HY", "Half a Year"),
    ("Y", "Yearly"),
]

GOODS = "Goods"
SERVICES = "Services"

ITEM_TYPES = (
    (GOODS, "Goods"),
    (SERVICES, "Services"),
)


FIXED = "Fixed Cost"
HOURS = "Based on Project Hours"
TASKS = "Based on Task Hours"
STAFF = "Based on Staff Hours"

BILLING_METHOD = (
    (FIXED, "FIXED"),
    (HOURS, "HOURS"),
    (TASKS, "TASKS"),
    (STAFF, "STAFF"),
)
