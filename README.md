# wearable-data-pipeline

### Questions this Project investigate
1. Does higher daily step count lead to longer or better sleep that night?
(connects dailyActivity_merged and sleepDay_merged on the same user and date)

2. Do people who sleep more hours perform better in activity the following day — more steps, fewer sedentary minutes?
(same two tables, but flipping the direction of the question)

3. Does a high heart rate always come from high physical activity, or are there users with high heart rate and low step counts?
(connects heartrate_seconds_merged and dailyActivity_merged — the interesting outliers)

4. Which users stopped wearing their tracker before the end of the study period?
(just dailyActivity_merged — looking at who has gaps or disappears after week one)

5. On which days of the week are people most and least active?
(just dailyActivity_merged — extracting the day from the date column)
