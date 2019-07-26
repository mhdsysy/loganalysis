#!/usr/bin/env python3

import psycopg2

db = psycopg2.connect("dbname=news")
cursor = db.cursor()

helper1_view = """create view helper1 as
                 select authors.id as authors_id,name as author_name,
                 title as articles_title,
                 slug,path,status,log.time::Date as day
                 from authors,articles,log
                 where log.path like concat('%', articles.slug,'%')
                 and authors.id = articles.author;"""
# First Question : What are the most popular three articles of all time?

first_question_query = """ select articles_title,count(status)as num
                           from helper1
                           where status='200 OK'
                           GROUP BY articles_title
                           order by num desc
                           limit 3;"""

cursor.execute(helper1_view)
cursor.execute(first_question_query)
print("\n----What are the most popular three articles of all time?-----\n")
result1 = list(cursor.fetchall())
print(result1)

# Second Question : Who are the most popular article authors of all time?

second_question_query = """select author_name,count(*)as num from helper1
                           where status='200 OK'
                           group by author_name
                           order by num desc;"""

cursor.execute(second_question_query)
result2 = list(cursor.fetchall())
print("\n----Who are the most popular article authors of all time?-----\n")
print(result2)

# Third Question : On which days did more than 1% of requests lead to errors?

cursor.execute("""select day,status,count(*) as sum
                  from helper1
                  group by day,status
                  order by day desc;""")

tmp_array = cursor.fetchall()
result3 = []
for i in range(0, len(tmp_array), 2):
    number_of_200 = tmp_array[i][2]
    number_of_404 = tmp_array[i + 1][2]
    tmp_sum = number_of_200 + number_of_404
    percentage = float(number_of_404 * 100) / float(tmp_sum)
    if (percentage) > 1:
        result3.append((str(tmp_array[i][0]), str(percentage) + ' %'))

print("\n--On which days did more than 1% of requests lead to errors?--\n")
print(result3)

db.close()
