create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
SELECT name, size FROM dogs, sizes WHERE height >= MIN AND height <= MAX;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
SELECT child FROM parents, dogs WHERE parent = name ORDER BY height DESC;


-- Sentences about siblings that are the same size
create table sentences as
    WITH siblings(first, second) AS (
        SELECT a.child, b.child from parents as a, parents as b
            WHERE a.parent = b.parent AND a.child > b.child
        )
    SELECT first || ' and ' || second || ' are ' || a.size || ' siblings '
        FROM siblings, size_of_dogs as a, size_of_dogs as b
        WHERE a.size = b.size AND a.name = first AND b.name = second;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH
    tower_of_dogs(dogs, total, n, max) AS (
      SELECT name, height, 1, height FROM dogs UNION
      SELECT dogs || ', ' || name, total+height, n+1, height 
        FROM tower_of_dogs, dogs
        WHERE n < 4 AND max < height
    )
SELECT dogs, total FROM tower_of_dogs 
  WHERE total >= 170 ORDER BY total;


CREATE TABLE tallest AS
    SELECT height, name FROM dogs 
        GROUP BY height / 10 HAVING MAX(height % 10) AND COUNT(*) > 1;



-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS 
  WITH
    non_parents(ancestor, descendent) AS (
      SELECT a.parent, b.child FROM parents AS a, parents AS b
	    WHERE a.child = b.parent UNION
	  SELECT ancestor, child FROM non_parents, parents 
	    WHERE parent = descendent
	)
  SELECT ancestor, descendent FROM non_parents UNION
  SELECT descendent, ancestor FROM non_parents;

SELECT a.ancestor, a.descendent
  FROM non_parents AS a, dogs as b, dogs as c
  WHERE a.ancestor = b.name AND a.descendent = c.name  
  ORDER BY b.height - c.height;
