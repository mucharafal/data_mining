import pandas

def reader(fileName):
	df = pandas.read_json(fileName, lines=True)
	authors_ids = df["authors"].apply(lambda x: map(lambda y: y["index"], x)).apply(lambda x: list(x))
	return authors_ids
