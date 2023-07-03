from django.utils.translation import gettext_lazy as _

FREQUENCY_CHOICES = [
    ("W", "Weekly"),
    ("BW", "Bi-Weekly"),
    ("M", "Monthly"),
    ("Q", "Quarterly"),
    ("HY", "Half a Year"),
    ("Y", "Yearly"),
]

ONCE = "Once"
RECURRING = "Recurring"

INVOICE_TYPE = ((ONCE, "Once"), (RECURRING, "Recurring"))


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
