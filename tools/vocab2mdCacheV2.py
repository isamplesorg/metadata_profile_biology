"""Script to generate markdown from a SKOS vocabulary.
The generated markdown is intended for rendering with Quarto.

Original python by Dave Vieglais for iSamples project
from https://github.com/isamplesorg/isamplesorg.github.io
Supported by NSF funding: Collaborative Research: Frameworks: 
Internet of Samples: Toward an Interdisciplinary Cyberinfrastructure 
for Material Samples, Award Number:2004815; 

S.M. Richard 2023-02-27 Updated to show some other SKOS properties 
and change formatting

This code reads a skos vocabulary file from a sqlAlchemy database
located at ../cache/vocabularies. Vocabularies are represented using SKOS
RDF vocabulary and Turtle serialization. Vocabularies are identified with
the  URI of the skos:ConceptScheme. The vocabualary representation is transformed
from SKOS/rdf/turtle to stdout as a text Markdown file using Quarto conventions.
The markdown uses some special syntax that is interpreted by 
Quarto for better html rendering

the conversion process fails if there are any non-base ASCII characters 
in the source files. 

license: Apache License 2.0

"""

import sys
import textwrap
import click
import rdflib
import datetime
import logging
import logging.config
import navocab  # this is a local python package with routines for
                # for interacting with skos rdf in an sqlAlchemy database



logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(name)s:%(levelname)s: %(message)s",
            "dateformat": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propogate": False,
        },
    },
}

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.CRITICAL,
    "CRITICAL": logging.CRITICAL,
}

def getLogger():
    return logging.getLogger("voc2md")



NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "obo": "http://purl.obolibrary.org/obo/",
    "dcterm": "http://purl.org/dc/terms/",
    "bioe":"https://w3id.org/isample/biology/biosampledfeature/"
}

PFX = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bioe: <https://w3id.org/isample/biology/biosampledfeature/> 
"""

INDENT = "  "


def skosT(term):
    return rdflib.URIRef(f"{NS['skos']}{term}")


def rdfT(term):
    return rdflib.URIRef(f"{NS['rdf']}{term}")


def rdfsT(term):
    return rdflib.URIRef(f"{NS['rdfs']}{term}")

def dctT(term):
    return rdflib.URIRef(f"{NS['dcterm']}{term}")


def listVocabularies(g):
    """List the vocabularies in the provided graph
    """
    q = PFX + """SELECT ?s
    WHERE {
        ?s rdf:type skos:ConceptScheme.
    }"""
    qres = g.query(q)
    res = []
    for r in qres:
        res.append(r[0])
    return res

def getVocabRoot(g, v):
    """Get top concept of the specific vocabulary
    """
    q = PFX + """SELECT ?s   WHERE { ?s skos:topConceptOf ?vocabulary . }"""
    qres = g.query(q, initBindings={'vocabulary': v})
    res = []
    for row in qres:
        res.append(row[0])
    return res

def getNarrower(g, v, r):
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?s
    WHERE {
        ?s skos:inScheme ?vocabulary .
        ?s skos:broader ?parent .
    }""")
    qres = g.query(q, initBindings={'vocabulary': v, 'parent': r})
    res = []
    for row in qres:
        res.append(row[0])
    return res

def getObjects(g, s, p):
    L = getLogger()
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?o
    WHERE {
        ?subject ?predicate ?o .
    }""")

    L.debug(f"getObject prefixes: {PFX}\n")
    L.debug(f"getObject expand subject: {s.toPython()}\n")
    L.debug(f"getObject expand predicate: {p.toPython()}\n")
    # g.expand_curie(s)
    qres = g.query(q, initBindings={'subject': s, 'predicate': p})
    L.debug(f"length of qres: {len(qres)}\n", )
    L.debug(f"qres: {qres}\n")
    res = []
    for row in qres:
        L.debug(f"getObject: {row[0]}\n")
        res.append(row[0])
    return res

def _labelToLink(label):
    if isinstance(label, list):
        label = label[0]
    label = label.split("/")[-1]
    label = label.lower().strip()
    label = label.replace(",", "")
    label = label.replace(" ", "-")
    return label

def termTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))
    L = getLogger()
    L.debug("termTree label: %s",label)
    llabel = _labelToLink(r)
    if not label:
        label = []
        label.insert(0, llabel)
    res = [f"{'    ' * depth}- [{label[0]}](#{llabel})"]
    for term in getNarrower(g, v, r):
        res += termTree(g, v, term, depth=depth + 1)
    return res

def termJsonTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))[0]
    llabel = _labelToLink(r)
    obj = {
        "name": label,
        "target": llabel,
    }
    # res = [f"{'    '*depth}- [{label[0]}](#{llabel})"]
    children = []
    for term in getNarrower(g, v, r):
        children.append(termJsonTree(g, v, term, depth=depth + 1))
    obj["children"] = children
    return obj

def describeTerm(g, t, depth=0, level=1):
    L = getLogger()
    res = []
    labels = getObjects(g, t, skosT('prefLabel'))
    L.debug("describe term: %s", t)
# anchor to link to this term
    _target = t.split("/")[-1]
    res.append("[]{" + f"#{_labelToLink(_target)}" + "}")
    res.append("")
# heading for this term
    hl = f"{'#' * (depth + 1)} "
    if len(labels) < 1:
        res.append(f"{hl} `{t}`")
    else:
        res.append(f"{hl} {labels[0].strip()}")
        for label in labels[1:]:
            res.append(f"* `{label}`")
#        res.append("")

    broader = getObjects(g, t, skosT('broader'))
    if len(broader) > 0:
        res.append("")
        res.append(f"- Child of:")
        for b in broader:
            bt = b.split('/')[-1]
            res.append(f" [`{bt}`](#{bt})")
#    res.append("")
    # The textual description will be present in rdfs:comment or
    # skos:definition. 
    comments = []
    for comment in getObjects(g, t, rdfsT('comment')):
        comments.append(f"- {comment}")
    for comment in getObjects(g, t, skosT('definition')):
        comments.append(f"- {comment}")
    for comment in comments:
        lines = textwrap.wrap(
            comment,
            width=70
        )
        res += lines
    seealsos = getObjects(g, t, rdfsT('seeAlso'))
    if len(seealsos) > 0:
#        res.append("")
        res.append(f"- See Also:")
        for seealso in seealsos:
            res.append(f"  * [{seealso.n3(g.namespace_manager)}]({seealso})")
    altlabels = []
    for altlabel in getObjects(g, t, skosT('altLabel')):
        altlabels.append(altlabel)
    if len(altlabels) > 0:
        delimiter = ""
        if len(altlabels) > 1:
            delimiter = ", "
#        res.append("")
        res.append(f"- **Alternate labels:**")
        for altlabel in altlabels:
            res.append(f"{altlabel}{delimiter}")
#        res.append("")

    sources = []
    for source in getObjects(g, t, dctT('source')):
        sources.append(source)
    if len(sources) > 0:
        delimiter = ""
        if len(sources) > 1:
            delimiter = ", "
#        res.append("")
        res.append(f"- **Source:**")
        for source in sources:
            res.append(f"{source}{delimiter}")
#        res.append("")

    res.append(f"- Concept URI: {t}")
    res.append("")

    return res


def describeNarrowerTerms(g, v, r, depth=0, level=[]):
    res = []
    terms = getNarrower(g, v, r)
    for term in terms:
        res += describeTerm(g, term, depth=depth)
        res.append("")
        res += describeNarrowerTerms(g, v, term, depth=depth + 1)
    return res


def describeVocabulary(G, V):
    res = []
    level = [1, ]
    L = getLogger()
    L.debug(f"vocab2md: {G} graph input")

    # this is the header for Quarto in the markdown output
    res.append("---")
    res.append("comment: | \n  WARNING: This file is generated. Any edits will be lost!")
    res.append("format:")
    res.append("  html:")
    res.append("    ascii: true")
    res.append("    toc: true")
    res.append("    toc-depth: 4")
    res.append("    number-sections: true")
    res.append("    anchor-sections: false")
    res.append("    number-depth: 8")
    res.append("execute:")
    res.append("  echo: false")
#    res.append("categories: [\"vocabulary\"]")
    res.append("---")
    # end of Quarto qmd header

    res.append("")
    gobj = getObjects(G, V, skosT("prefLabel"))
    if len(gobj)>0:
        scheme = gobj[0]
    else:
        L.debug(f"vocab2md: {V} object must have a skos:prefLabel")
        scheme = "ConceptScheme"
    lscheme = scheme.replace(" ","")
    res.append("[]{" + f"#{lscheme}" + "}")
    res.append("")
    # bold heading 1
    res.append(f"# **Concept scheme:** {scheme}")
    res.append("")
    try:
        modified = getObjects(G, V, dctT("modified"))[0]
        res.append(f"Vocabulary last modified:  {modified}")
        res.append("")
    except:
        L.debug("expected a skos:modified date for most recent update to vocabulary")
        res.append("no modified date")
        res.append("")
    res.append("subtitle: ")
    for comment in getObjects(G, V, skosT("definition")) + getObjects(G, V, rdfsT("comment")):
        res.append(f"  {comment.strip()}")
    res.append("")
    res.append("Namespace: ")
    res.append(f"[`{V}`]({V})")
    res.append("")
    res.append("**History**")
    res.append("")
    for history in getObjects(G, V, skosT("historyNote")):
        res.append(f"* {history}")
    res.append("")

    depth = 1
    roots = getVocabRoot(G, V)
#
    for root in roots:
        res += termTree(G, V, root, depth=0)
        res.append("")

    res.append("**Concepts**")
    res.append("")
    for aroot in roots:
        res += describeTerm(G, aroot, depth=depth, level=level)
        res.append("")
        res += describeNarrowerTerms(G, V, aroot, depth=depth + 1, level=level)
        res.append("")
    return res

def conceptschemelist(G):
    vocabs = listVocabularies(G)
    res = []
    res.append("")
    res.append(f"# Concept Schemes in this file")
    res.append("")
    for vocab in vocabs:
        label = getObjects(G, vocab, skosT("prefLabel"))
        llabel = label[0].replace(" ", "")
        res.append(f"[{label[0]}](#{llabel})")
        res.append("")

    res.append("")
    res.append(
        f"This file generated at: \"{datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).isoformat()}\"")

    return res

@click.command()
@click.argument("source")
@click.argument("vocabulary")
# @click.argument("ttl")  #this is from the text file version
#def main(ttl):
def main(source, vocabulary):
    """Generate Pandoc markdown from a SKOS vocabulary in Turtle.
    TTL may be a local file or URL.
    Output to STDOUT.
    """
    # vgraph = rdflib.ConjunctiveGraph()
    # vgraph.parse(ttl, format="text/turtle")
    # for k, v in NS.items():
    #     vgraph.bind(k, v)
    # vocabs = listVocabularies(vgraph)
    # res = []
    # res.append(conceptschemelist(vgraph))

    verbosity = "DEBUG".upper()
    logging_config["loggers"][""]["level"] = verbosity
    logging.config.dictConfig(logging_config)
    L = getLogger()

    source = f"sqlite:///{source}"
    store = navocab.VocabularyStore(storage_uri=source)
    res = []

    L.debug(f"vocab2md source: {source}")
    L.debug(f"vocab2md vocabulary: {vocabulary}")

    test = store._g.namespace_manager.expand_curie(vocabulary)
    L.debug(f"Test: {test}")

    vocabulary = store.expand_name(vocabulary)
    L.debug(f"main: call describeVocabulary for: {vocabulary}")
    theMarkdown = describeVocabulary(store._g, vocabulary)
    res.append(theMarkdown)
    # send the result to stdout via print.
    for doc in res:
        for line in doc:
            print(line)
    return 0
    


if __name__ == "__main__":
    sys.exit(main())
