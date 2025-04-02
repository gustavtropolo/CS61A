CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

--CREATE TABLE test AS
  --SELECT f1.course, f2.course, f1.hall, f2.hall FROM finals as f1, finals as f2 WHERE f1.hall = f2.hall AND f1.course != f2.course;

CREATE TABLE sharing AS --we want to count the halls shared that are distinct
  SELECT f1.course, COUNT(DISTINCT f1.hall) FROM finals as f1, finals as f2 WHERE f1.hall = f2.hall AND f1.course != f2.course GROUP BY f1.course;

CREATE TABLE pairs AS
  SELECT s1.room || ' and ' || s2.room || ' together have ' || (s1.seats + s2.seats) || ' seats' 
  FROM sizes as s1, sizes as s2 WHERE s1.room < s2.room and s1.seats + s2.seats >= 1000;

CREATE TABLE big AS
  SELECT course FROM finals, sizes WHERE sizes.room = finals.hall GROUP BY course HAVING SUM(seats) >= 1000;

CREATE TABLE remaining AS
SELECT f1.course, 
       SUM(CASE WHEN s1.seats != (
           SELECT MAX(s2.seats)
           FROM finals AS f2
           JOIN sizes AS s2 ON f2.hall = s2.room
           WHERE f2.course = f1.course
       ) THEN s1.seats ELSE 0 END) AS remaining
FROM finals AS f1
LEFT JOIN sizes AS s1 ON f1.hall = s1.room
GROUP BY f1.course;

