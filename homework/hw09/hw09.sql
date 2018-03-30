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
create table stacks as
  with 
    stack_recur(dogs, total, n, max) as (
      select name, height, 1, height from dogs union
      select dogs || ', ' || name, total+height, n+1, height 
        from stack_recur, dogs
        where n < 4 and max < height
    )
select dogs, total from stack_recur 
  where total >= 170 and n = 4 order by total;


create table tallest as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


