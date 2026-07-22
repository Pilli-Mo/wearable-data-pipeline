# wearable-data-pipeline

### Questions this Project investigate
1. Does higher daily step count lead to longer or better sleep that night?
(connects dailyActivity_merged and sleepDay_merged on the same user and date)
----there is a weak negative relationship — more active days are slightly associated with less sleep, but the effect is small and step count is not a strong predictor of sleep.

2. Do people who sleep more hours perform better in activity the following day — more steps, fewer sedentary minutes?
(same two tables, but flipping the direction of the question)

3. Does a high heart rate always come from high physical activity, or are there users with high heart rate and low step counts?
(connects heartrate_seconds_merged and dailyActivity_merged — the interesting outliers)

4. Which users stopped wearing their tracker before the end of the study period?
(just dailyActivity_merged — looking at who has gaps or disappears after week one)
---2347167796 (18 days), 3372868164 (20 days), 4057192912 (only 4 days — essentially abandoned the study), and 8253242879 (19 days). Everyone else stayed consistent at 26+ days.

5. On which days of the week are people most and least active?
(just dailyActivity_merged — extracting the day from the date column)
------Saturday is the most active day(8152,975avg Steps), Sunday is the least active (6933 avg steps)
