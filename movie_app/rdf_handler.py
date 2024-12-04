from rdflib import Graph

class RDFDataHandler:
    def __init__(self, rdf_file):
        self.graph = Graph()
        self.graph.parse(rdf_file, format='xml')

    def execute_query(self, query):
        return self.graph.query(query)
