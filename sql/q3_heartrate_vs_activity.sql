Select id, strftime('%Y-%m-%d', Time) as day, AVG(value) as avg_heartrate
from heartrate
Group by Id,day;