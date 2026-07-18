SELECT dailyActivity.Id, TotalSteps, TotalMinutesAsleep
FROM dailyActivity
JOIN sleepDay ON dailyActivity.Id = sleepDay.Id
              AND dailyActivity.ActivityDate = sleepDay.SleepDay;