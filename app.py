from bottle import *
import sqlite3

@route('/index')
def main():
	return template('search.pyhtml')

@route('/results')
def main():
	conn = sqlite3.connect(r'teste.db')
	cursor = conn.cursor()
	id = request.query.id
	cursor.execute('SELECT * FROM TAB1 WHERE ID = ?', str(id))
	list = []
	for reg in cursor.fetchall():
		list.append(reg)
	conn.close()
	return template('results.pyhtml', list = list)

run(host = 'localhost', port = 1996)