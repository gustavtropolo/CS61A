CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child FROM parents, dogs ON parents.parent = dogs.name ORDER BY dogs.height DESC;
   --we need the parents table where we use the child col, then order descending from dogs


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size FROM dogs, sizes ON dogs.height > sizes.min AND dogs.height <= sizes.max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS sibling1, b.child AS sibling2 FROM parents AS a JOIN parents AS b ON a.child < b.child AND a.parent = b.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || sibling1 || " and " || sibling2 || ", have the same size: " || a.size 
  FROM siblings, size_of_dogs AS a, size_of_dogs AS b WHERE sibling1 = a.name AND sibling2 = b.name AND a.size = b.size;
--Get two size_of_dogs tables, and if the names are good and size are same
--The two siblings, bella and charlie, have the same size: standard

CREATE TABLE fur_types AS
  SELECT "short" AS fur UNION
  SELECT "long" UNION
  SELECT "curly";

CREATE TABLE avg_height AS 
  SELECT fur_types.fur AS fur, (SELECT AVG(dogs.height) FROM dogs WHERE dogs.fur = fur_types.fur) AS avg FROM fur_types;

CREATE TABLE min_max AS
  SELECT fur_types.fur AS fur, (SELECT MIN(dogs.height) FROM dogs WHERE dogs.fur = fur_types.fur) AS min,
  (SELECT MAX(dogs.height) FROM dogs WHERE dogs.fur = fur_types.fur) AS max FROM fur_types;

-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS --gpt's solution i want to understand
  SELECT fur, MAX(height) - MIN(height) AS height_range
  FROM dogs
  GROUP BY fur --this allows us to consider the min and max of the same fur
  HAVING MIN(height) >= 0.7 * AVG(height) AND MAX(height) <= 1.3 * AVG(height);
  -- SELECT fur_types.fur AS fur, 
  -- (SELECT min_max.max - min_max.min FROM min_max, dogs
  -- WHERE min_max.min >= 0.7 * avg_height.avg AND min_max.max <= 1.3 * avg_height.avg AND
  -- dogs.fur = fur_types.fur AND avg_height.fur = dogs.fur AND dogs.fur = min_max.fur
  -- ) AS height_range
  --  FROM fur_types, avg_height
  --  WHERE fur_types.fur = avg_height.fur AND (height_range) IS NOT NULL; --this prevents it from being repeated on each mix of these two
--the dog must have the same fur as the specified fur type and the value must be in the range

