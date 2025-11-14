import json
from datetime import date, timedelta

notices = []
start_date = date(2025, 3, 1)
union_id = 1165
file_path = "uploads/বস_বরদদর_নটশ_4c4EtTb.pdf"

for i in range(30):
    day = start_date + timedelta(days=i)
    notices.append({
        "model": "notification.notice",
        "pk": i + 1,
        "fields": {
            "title": f"নোটিশ {i + 1}",
            "date": day.isoformat(),
            "file": file_path,
            "union": union_id,
            "is_active": True
        }
    })

with open("notices_march_2025.json", "w", encoding="utf-8") as f:
    json.dump(notices, f, ensure_ascii=False, indent=2)
