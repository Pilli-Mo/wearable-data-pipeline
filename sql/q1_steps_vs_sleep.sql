--- Does higher daily step count lead to longer or better sleep that night?
---(connects dailyActivity_merged and sleepDay_merged on the same user and date)

SELECT dailyActivity.Id, TotalSteps, TotalMinutesAsleep
FROM dailyActivity
JOIN sleepDay ON dailyActivity.Id = sleepDay.Id
              AND dailyActivity.ActivityDate = sleepDay.SleepDay;