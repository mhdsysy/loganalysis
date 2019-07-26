# Log Analysis

## * Views created :

#### helper1:
`Create view helper1 as `
                
                select authors.id as authors_id,name as author_name,
                 title as articles_title,
                 slug,path,status,log.time::Date as day

                 from authors,articles,log
                 where log.path like concat('%', articles.slug,'%')
                 and authors.id = articles.author;`

Which joins the tables authors,articles,log on the rows where the path column in the log table is like(similar to not necessairly the same as)
	 the slug column in the articles table and where the id column in the authors table is equal to the author column in the articles table.


## * The Questions and Queries :
### What are the most popular three articles of all time? :
For this i selected the articles_title column from the view helper1 , and counted the rows where
status of http response was '200 OK' because in the case of '404 NOT FOUND' no one viewed the article.

### Who are the most popular article authors of all time?
For this i selected the authors_name column from the view helper1 , and counted the rows where
status of http response was '200 OK' because in the case of '404 NOT FOUND' no one viewed the article.

### On which days did more than 1% of requests lead to errors?

For this question i selected from the view helper1 the day and the status column, count number of responses.
The results were ordered in descending order and for each day there are two rows,
the first one containing the number of '200 OK' responses
and the seconds contains the number of '404 NOT FOUND' responses.

**`select day,status,count(*) as sum
                  from helper1
                  group by day,status
                  order by day desc;""")
`**

After that i fetched the data in a temporary array and looped through the indexes(rows of the table),
calculated the percentage,checked if it'S bigger than 1%,and finally
added it with it's corresponding date to an array called result3.

## * How to run the program :
From the terminal :

`CD <replace this with the path of the loganalysis file which you downloaded>`
Just type **`python3 loganalysis.py`** in the terminal and the results of
the queries should appear.
If an error appears that psycopg2 is not a recognizable module,
try **`python loganalysis.py`**.
If the error still appears try **`pip3 install psycopg2`** (for mac)
and type **`python3 loganalysis.py`** , or **`pip install psycopg2`** and then **`python loganalysis.py`**.

From pycharm :

Open the project and run it.


