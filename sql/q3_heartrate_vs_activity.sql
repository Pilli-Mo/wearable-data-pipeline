-- Q3: does high heart rate come from high activity?
---1. dailyActivity table = have (saved table)
-- 2. daily avg heart rate = have the query, but not saved as a table
-- 3. need to join dailyActivity with that heart rate query result
-- 4. correlate TotalSteps vs avg_heartrate
-- 5. check for outliers


SELECT dailyActivity.Id, TotalSteps, avg_heartrate
From dailyActivity
JOIN (
    Select id, strftime('%Y-%m-%d', Time) as day, AVG(value) as avg_heartrate
    from heartrate
    Group by Id,day
) AS dailyHR
ON dailyActivity.Id = dailyHR.Id
    AND dailyActivity.ActivityDate = dailyHR.day;