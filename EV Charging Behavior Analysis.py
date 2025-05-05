
-- 1. unique_users_per_garage
SELECT garage_id, 
       COUNT(DISTINCT user_id) AS num_unique_users
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY garage_id
ORDER BY num_unique_users DESC;

-- 2. most_popular_shared_start_times
SELECT weekdays_plugin,
       start_plugin_hour, 
       COUNT(*) AS num_charging_sessions
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY weekdays_plugin, start_plugin_hour
ORDER BY num_charging_sessions DESC
LIMIT 10;

3. long_duration_shared_users
SELECT user_id, 
       AVG(duration_hours) AS avg_charging_duration
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY user_id
HAVING AVG(duration_hours) > 10
ORDER BY avg_charging_duration DESC;
