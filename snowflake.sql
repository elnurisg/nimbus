SELECT et.email
FROM data_table AS dt
JOIN email_table AS et 
WHERE dt.join_id = et.join_id
    AND dt.column_1 % 2 = 0
    AND dt.column_2 < dt.column_1
    AND dt.column_3 LIKE '%1'