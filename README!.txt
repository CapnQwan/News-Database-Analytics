Requirements for this to run:

	Vagrant installed
	Oracle VM Virtual Box installed
	Git Bash installed 
	the project downloaded and unzipped into a folder

How to run it:
	
	To run this program all you will need to do is open up git bash change directory using cd to where you have the project located (make sure you cd into the folder containing the project) then in git bash run vagrant up
	once that is done you will need to run vagrant ssh once this is done you can then type in "python Project.py" this will then run the program and the outputs will be displayed in the git bash terminal

What is the purpose of this program:

	the purpose of this program is to awnser 3 questions these questions will be awnsered using the database that was given to use by udacity

	1. What are the most popular three articles of all time?
		
		to awnser this question i used the sql query:
			select articles.title, count(log.path) as visits from articles, log where log.path like '%' || articles.slug and log.status = '200 OK' group by articles.title order by visits desc limit 3;

		which gets the title of the articles and then basically counts how many times they have been visited i made sure to make it so only articles with a status 200 OK count as i think 404 errors shouldn't count
		as the articles are not actually being visited

	2. Who are the most popular article authors of all time?
		
		to awnser this question i used the sql query: 
			select authors.name, count(log.path) as visits from authors, log, articles where authors.id = articles.author and log.path like '%' || articles.slug and log.status = '200 OK' group by
			 authors.name order by visits desc;

		which gets the authors names and then counts how many of there articles have been visited in total i made sure to make it so only articles with a status 200 OK count as i think 404 errors shouldn't count
		as the articles are not actually being visited
		
	3. On which days did more than 1% of requests lead to errors?

		this one is a bit different as i used a view which is like another database that we can work off of the sql querys i used were:
		
			create or replace view percentages as select to_char(log.time, 'YYYY-MM-DD') as Date, sum(case when log.status = '404 NOT FOUND' then 1 else 0 end)*100/ count(log.status) as percentage
			 from log group by to_char(log.time, 'YYYY-MM-DD') order by percentage desc;
		
			select * from percentages where percentage>=1;

		as you might be able to tell the first one is what does the bulk of the work it basically groups the dates and then compairs how many visits where made in total to how many where errors making it into a percentage 
		then the second one just takes all the information gathered and gets rid of all the stuff we dont want and desplays the final product

		this view is built into the code so it shouldn't have to be run seperatly 

known errors: 

	pep8 thorws errors about indentations containing tabs but when attempting to fix this and change it over to spaces git bash started thorwing errors and the only solution i could find was swaping it back to tabs

Contact me: 

if there are any errors or any questions feel free to contact me at q.p1453@gmail.com
