-- FUNCTION TO GET A MEMBER FROM JASEN TABLE BY JASEN_ID

-- Create a function and set arguments
CREATE FUNCTION public.get_member(
	id integer
)
-- Define the type of result set -> jasen table's structure
RETURNS SETOF public.jasen
-- Set language to standard SQL
LANGUAGE SQL
AS $$ -- $$ is the start of code block (BEGIN)
SELECT * FROM public.jasen WHERE jasen_id = id;
$$; -- $$ is the end of the block (END)
