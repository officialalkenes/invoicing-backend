from datetime import datetime, timedelta
from calendar import monthrange


def calculate_date_range(filter_by):
    today = datetime.now().date()
    filter_by = filter_by.lower()

    if filter_by == "today":
        start_date = today
        end_date = today
    elif filter_by == "yesterday":
        start_date = today - timedelta(days=1)
        end_date = start_date
    elif filter_by == "weekly":
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
    elif filter_by == "previous week":
        start_date = today - timedelta(days=today.weekday() + 7)
        end_date = start_date + timedelta(days=6)
    elif filter_by == "monthly":
        start_date = datetime(today.year, today.month, 1).date()
        end_date = datetime(
            today.year, today.month, monthrange(today.year, today.month)[1]
        ).date()
    elif filter_by == "previous month":
        if today.month == 1:
            start_date = datetime(today.year - 1, 12, 1).date()
            end_date = datetime(
                today.year - 1, 12, monthrange(today.year - 1, 12)[1]
            ).date()
        else:
            start_date = datetime(today.year, today.month - 1, 1).date()
            end_date = datetime(
                today.year, today.month - 1, monthrange(today.year, today.month - 1)[1]
            ).date()
    elif filter_by == "quarterly":
        start_date = datetime(today.year, ((today.month - 1) // 3) * 3 + 1, 1).date()
        end_date = datetime(
            today.year,
            ((today.month - 1) // 3) * 3 + 3,
            monthrange(today.year, ((today.month - 1) // 3) * 3 + 3)[1],
        ).date()
    elif filter_by == "previous quarter":
        if today.month in [1, 2, 3]:
            start_date = datetime(today.year - 1, 10, 1).date()
            end_date = datetime(today.year - 1, 12, 31).date()
        else:
            start_date = datetime(
                today.year, ((today.month - 1) // 3 - 1) * 3 + 1, 1
            ).date()
            end_date = datetime(
                today.year,
                ((today.month - 1) // 3 - 1) * 3 + 3,
                monthrange(today.year, ((today.month - 1) // 3 - 1) * 3 + 3)[1],
            ).date()
    else:
        # Default to Today if filter_by value is not recognized
        start_date = today
        end_date = today

    return start_date, end_date
