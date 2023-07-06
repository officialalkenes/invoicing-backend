from datetime import datetime, timedelta
from calendar import monthrange


def calculate_date_range(filter_by):
    today = datetime.now().date()
    filter_by = filter_by.lower()

    if filter_by == "today":
        start_date = today
        end_date = today
    elif filter_by == "weekly":
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
    elif filter_by == "monthly":
        start_date = datetime(today.year, today.month, 1).date()
        end_date = datetime(
            today.year, today.month, monthrange(today.year, today.month)[1]
        ).date()
    elif filter_by == "yearly":
        start_date = datetime(today.year, 1, 1).date()
        end_date = datetime(today.year, 12, 31).date()
    else:
        # Default to Today if filter_by value is not recognized
        start_date = today
        end_date = today

    return start_date, end_date
