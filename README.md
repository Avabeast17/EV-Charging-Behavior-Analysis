# EV Charging Behavior Analysis

This project explores electric vehicle (EV) charging behavior in shared apartment garages using SQL. As EV adoption accelerates, understanding shared charging habits becomes crucial for improving infrastructure and energy management.

>  Powered by PostgreSQL | 💡 Real-world SQL analysis for smart urban planning


##  Project Overview

In this analysis, I have uncovered insights into how EV users interact with shared charging stations. I answer the following:

1. **Which garages have the highest number of unique shared users?**  
2. **When are users most likely to start charging on shared stations?**  
3. **Who are the users with the longest average charging durations?**  

These insights can help building managers reduce wait times, optimize charging port allocation, and anticipate peak demand.


## Key Findings

| Metric                              | Insight                                             |
|------------------------------------|-----------------------------------------------------|
| Top Garage                         | BI2 – 18 unique shared users                        |
| Peak Charging Time                 | Sunday @ 5 PM – 30 sessions                        |
| Longest Average Session Duration   | Share-9 – 16.85 hours per session                  |


## SQL Queries

This project includes three key SQL queries:

- `unique_users_per_garage`  
- `most_popular_shared_start_times`  
- `long_duration_shared_users`

Each query is optimized, sorted, and grouped for performance and clarity.


##  Sample Query (unique users)

```sql
SELECT garage_id, 
       COUNT(DISTINCT user_id) AS num_unique_users
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY garage_id
ORDER BY num_unique_users DESC;
