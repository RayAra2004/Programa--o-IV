import psycopg2
from config import config

def cursor(a=0):
	if(a == 0):
		conn = None
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

	return cur
	
def main():
	
	cur = cursor()
	cur.execute("SELECT * FROM projeto")
	row = cur.fetchall()
	
	for i in row:
		print(f"Código: {i[0]} Nome: {i[1]} Localização: {i[2]}")
	cur.close()
	return 0
if __name__ == '__main__':main()
