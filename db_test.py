import psycopg2
import sys
 
def main():
	#Define our connection string
	conn = None
	try:
		conn = psycopg2.connect(host="localhost", database="political_api", user="postgres", password="jstopen")
		cur=conn.cursor()
		lst = cur.execute("SELECT * FROM users")
		part_id = cur.fetchone()
		print(part_id)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == "__main__":
	main()