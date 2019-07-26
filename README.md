# Log Analysis

## * Views created :

#### helper1:
`Create view helper1 as`                                     
`select authors.id as authors_id,name as author_name,`
`title as articles_title,`
`slug,path,status,log.time::Date as day`

`from authors,articles,log`

`where log.path like concat('%', articles.slug,'%')`

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
1- Install Python version 2 or 3 :

[Click Me :)](https://www.python.org/downloads/)

2-Install VirtualBox 

[Click Me :)](https://www.virtualbox.org/wiki/Downloads)

3-Install Vagrant :

[Click me :)](https://www.vagrantup.com/downloads.html)

4-Set up the files and directory for the database :

Do the following fode blocks

`mkdir <name>` (to make a working directory)

`CD <name of the directory you created>`

`vagrant init hashicorp/precise64`

`vagrant box add hashicorp/precise64`

then follow the **Using a Box** Section in the following link :

[Click me :)](https://www.vagrantup.com/intro/getting-started/boxes.html)


Download all the files in this repository in the vagrant Directory which you've created.

now run these blocks of code : (from the terminal and you should be in the vagrant directory where Vagrant file is located)

`Vagrant up` 

Wait untill it ends, it will take a while depending on the speed of your internet connection..

`Vagrant SSH`

5- Setting up the database :
now (all the files in the repository should be in the vagrant file you've created) .

`cd /vagrant` 

type `psql` 

if postgres is not installed , 

`sudo apt-get update`

`sudo apt-get install postgresql-9.3 postgresql-contrib-9.3`

if any thing goes wromg follow this link here [Click me :)](https://www.postgresql.org/download/linux/ubuntu/)

after yo've typed **psql** type 

`create database news`

then ctrl+D to exit back to the command line

and type this 

`psql -d news -f newsdata.psql`

now type 

`psql news`

you're in Congratulations

6- install psycopg2  and run the code :

`pip install psycopg2` for python 2

`pip3 install psycopg2`

 Run the **loganalysis.py** code from the terminal using the following line 

`python loganalysis.py` for python 2

`python3 loganalysis.py`` for python 3

and finally :

**`python3 loganalysis.py`** to run the code in python 3
**`python loganalysis.py`** to run the code in python 2














