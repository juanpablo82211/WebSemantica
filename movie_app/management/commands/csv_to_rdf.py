import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

# Define una URI base
BASE_URI = "http://example.org/movies/"
MOVIE = Namespace(BASE_URI)

# Crear un grafo RDF
g = Graph()

# Leer el archivo CSV
csv_file_path = "movie_app\management\commands\movie_app_movie.csv"  # Reemplaza con la ruta a tu archivo
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_id = row['id']
        movie_uri = URIRef(f"{BASE_URI}{movie_id}")
        
        # Añadir triples al grafo
        g.add((movie_uri, RDF.type, MOVIE.Movie))
        g.add((movie_uri, MOVIE.movie_id, Literal(row['movie_id'], datatype=XSD.integer)))
        g.add((movie_uri, MOVIE.title, Literal(row['title'], datatype=XSD.string)))
        g.add((movie_uri, MOVIE.overview, Literal(row['overview'], datatype=XSD.string)))
        g.add((movie_uri, MOVIE.popularity, Literal(row['popularity'], datatype=XSD.float)))
        g.add((movie_uri, MOVIE.poster, Literal(row['poster'], datatype=XSD.anyURI)))
        g.add((movie_uri, MOVIE.video, Literal(row['video'], datatype=XSD.string)))
        g.add((movie_uri, MOVIE.release_date, Literal(row['release_date'], datatype=XSD.date)))
        g.add((movie_uri, MOVIE.language, Literal(row['language'], datatype=XSD.string)))
        g.add((movie_uri, MOVIE.vote_average, Literal(row['vote_average'], datatype=XSD.float)))
        g.add((movie_uri, MOVIE.is_active, Literal(row['is_active'], datatype=XSD.boolean)))
        g.add((movie_uri, MOVIE.slug, Literal(row['slug'], datatype=XSD.string)))
        g.add((movie_uri, MOVIE.viewed, Literal(row['viewed'], datatype=XSD.integer)))

# Guardar el grafo en un archivo Turtle
output_file = "movies.rdf"
g.serialize(destination=output_file, format="turtle")
print(f"Grafo RDF exportado a {output_file}")
