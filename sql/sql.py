import psycopg2
from config import config

def main():

	conn = psycopg2.connect(
		host="kesavan.db.elephantsql.com",
		database="tayzxcet",
		user="tayzxcet",
		password="t3wVbMM9P_vqK5wL-tm6p2bDPzjFrHLK")
		
	cur = cursor()
	cur.execute("SELECT * FROM projeto")
	row = cur.fetchall()
	
	for i in row:
		print(f"Código: {i[0]} Nome: {i[1]} Localização: {i[2]}")
		
	cur.close()
	conn.close()
	return 0
if __name__ == '__main__': main()
