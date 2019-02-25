import psycopg2

DBNAME = "news"


def Top_Articles():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select articles.title, count(log.path) as visits from articles,"
				" log where log.path like '%' || articles.slug and log.status = "
				"'200 OK' group by articles.title order by visits desc limit 3;")
	print("top 3 articles of all time")
	Article = c.fetchone()
	while Article is not None:
		print(str(Article[0]) + " - " + str(Article[1]) + " Views")
		Article = c.fetchone()
	print("")
	db.close()


def Top_Authors():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select authors.name, count(log.path) as visits from authors, "
				"log, articles where authors.id = articles.author and log.path"
				" like '%' || articles.slug and log.status = '200 OK' group by"
				" authors.name order by visits desc;")
	print("Top authors of all time")
	author = c.fetchone()
	while author is not None:
		print(str(author[0]) + " - " + str(author[1]) + " Views")
		author = c.fetchone()
	print("")
	db.close()


def Error_percentile():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("create or replace view percentages as select to_char(log.time,"
				" 'YYYY-MM-DD') as Date, sum(case when log.status = '404 NOT "
				"FOUND' then 1 else 0 end)*100/ count(log.status) as percentage"
				" from log group by to_char(log.time, 'YYYY-MM-DD') order by "
				"percentage desc;")
	c.execute("select * from percentages where percentage>=1;")
	print("Days where more then 1% of requests lead to errors")
	errors = c.fetchone()
	while errors is not None:
		print(str(errors[0]) + " - " + str(errors[1]) + "%")
		errors = c.fetchone()
	db.close()


Top_Authors()
Top_Articles()
Error_percentile()
