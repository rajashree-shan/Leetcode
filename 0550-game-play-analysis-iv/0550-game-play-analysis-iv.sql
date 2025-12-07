# Write your MySQL query statement below
SELECT
    ROUND(
        AVG(
            CASE 
                WHEN a2.player_id IS NOT NULL THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS fraction
FROM (
    -- First login date per player
    SELECT 
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) first
LEFT JOIN Activity a2
    ON a2.player_id = first.player_id
   AND a2.event_date = DATE_ADD(first.first_login, INTERVAL 1 DAY);
