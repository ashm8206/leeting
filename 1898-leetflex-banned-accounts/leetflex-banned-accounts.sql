-- Write your PostgreSQL query statement below
SELECT
  DISTINCT l1.account_id
FROM
  LogInfo l1
CROSS JOIN
  LogInfo l2
WHERE
  l1.account_id = l2.account_id AND
  l1.ip_address != l2.ip_address AND
  l2.login between l1.login and l1.logout