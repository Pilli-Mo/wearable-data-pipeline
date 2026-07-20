Select Id, count(*) as days_tracked
From dailyActivity
Group by Id
Having count(*) < 25;