#!/usr/local/bin/python
"""
github_action_main original
depends on makefile to run vocab.py
Driver file for the vocabularies GitHub Action.  Runs inside a Docker container,
with all of the vocabularies tools and dependencies copied into the Docker container.

the github workflow needs to copy output files to the docs directory
in the public github, else they disappear with the docker container when workflow
completes
original code by Dave Vieglais for iSamples project
modified by SM Richard 2023-12-14

input arguments are grabbed from environmental variables
"""

import logging
import os
import subprocess
import sys
import logging
import logging.config

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
    return logging.getLogger("action_main")



def main():
#    logging.debug(f"environment variables are {os.environ}")
#    print(f"environment variables are {os.environ}")

    verbosity = "DEBUG".upper()
    logging_config["loggers"][""]["level"] = verbosity
    logging.config.dictConfig(logging_config)
    L = getLogger()

    command = os.environ["INPUT_ACTION"]
    L.debug(f"github_action_main: INPUT_ACTION: {command}")
    path = os.environ["INPUT_PATH"]
    path = os.path.join(path, "docs")
    input = os.environ["INPUT_INPUTTTL"]
    L.debug(f"inputttl string: {input}")
    inputttl = input.split('|')
    # inputttl is a list of skos rdf vocabulary filenames with Turtle serialization
    # vocab_source_dir is the path to the directory that contains the source files
    for filename in inputttl:
            print(f"files to load: {filename}")

    input = os.environ["INPUT_INPUTVOCABURI"]
    L.debug(f"inputvocaburi string: {input}")
    inputvocaburi = input.split('|')
    for auri in inputvocaburi:
            print(f"vocab URIs: {auri}")

    
    # make sure have cache directory -- this is where the sqlAlchemy db will be         
    cachepath = "cache/vocabularies.db"
    # this is the directory that holds the source SKOS ttl files.
    sourcevocabdir = "vocabulary"


    L.debug(f"github_action_main: target path for output: {path}")
    if path is None:
        L.debug("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        L.debug(f"Created {path} since it didn't exist.")

    # do function of original Makefile here


    theindex = 0
    for inputf in inputttl:
        result=load_cachedb(sourcevocabdir + "/" + inputf + ".ttl", cachepath, inputvocaburi[theindex] )
        if (result == 0):
           L.debug(f"load_cachedb call successful for: {inputf}, {inputvocaburi[theindex]}")
        else:
           L.debug(f"load_cachedb had problem processing: {inputf},{inputvocaburi[theindex]}")
        theindex = theindex + 1


    if command == "uijson":
        L.debug("Generating uijson for inclusion in webUI build")
        index = 0
        while index < len(inputttl):
            _run_uijson_in_container(os.path.join(path, inputttl[index]+".json"), inputvocaburi[index])
            index += 1
    elif command == "docs":
        L.debug("Generating markdown and html docs")
        index = 0
        L.debug(f"input markdown file: {inputttl[index]}, vocab uri: {inputvocaburi[index]}")
        while index < len(inputttl):
            result = _run_docs_in_container(os.path.join(path, inputttl[index]+".md"), inputvocaburi[index])
            if result == 0:
                _quarto_render_html((os.path.join(path, inputttl[index]+".md")),path)
            else:
                L.debug(f"problem with {inputttl[index]}, don't call quarto")
            index += 1
    else:
        L.debug(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)

def load_cachedb(inputf, cachepath, voc_uri):
    # tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@
    L = getLogger()
    L.debug(f"cachdb file to load: {inputf}")
    load_args = ["--verbosity","DEBUG", "-s", cachepath, "load", inputf, voc_uri]
    result = _run_python_in_container("/app/tools/vocab.py", load_args, f="")
    if (result == 0):
        L.debug(f"vocab.py.load call successful for {inputf}")
        return 0
    else:
        L.debug(f"vocab.py.load had problem processing {inputf}")
        return 1
    

def _quarto_render_html(markdown_in:str, output_path:str):
#     print("In githubActionMain: Quarto render: ",markdown_in,  output_path)
#     result = subprocess.run(["/opt/quarto/bin/quarto", "check"])
#     print("Quarto check result ", result.returncode)
#  NOTE update quarto location for your local install...
     result = subprocess.run(["/opt/quarto/bin/quarto", "render", markdown_in, "-t", "html"])
#     print("Quarto call result ", result.returncode)
     L = getLogger()
     if (result.returncode == 0):
         L.debug(f"Quarto call successful for {markdown_in}")
         return 0
     else:
         L.debug(f"Quarto had problem processing {markdown_in}")
         return 1


def _run_make_in_container(target: str):
    L = getLogger()
    L.debug(f"In githubActionMain: make in container, target: {target}")
    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_uijson_in_container(output_path: str, vocab_location: str):
    L = getLogger()
    with open(output_path, "w") as f:
        vocab_args = ["-s", "/app/cache/vocabularies.db", "uijson", vocab_location, "-e"]
        testflag = _run_python_in_container("/app/tools/vocab.py", vocab_args, f)
        if (testflag == 0):
            L.debug(f"Run_uijson: Successfully wrote uijson file to {output_path}")
            return 0
        else:
            L.debug(f"problem processing {vocab_location}")
            return 1

def _run_docs_in_container(output_path: str, vocab_location: str):
    L = getLogger()
    with open(output_path, "w") as f:
        docs_args = ["/app/cache/vocabularies.db", vocab_location]
        testflag = _run_python_in_container("/app/tools/vocab2mdCacheV2.py", docs_args, f)
        if (testflag == 0):
            L.debug(f"Docs in container: Successfully wrote doc file {vocab_location} to {output_path}")
            return 0
        else:
            L.debug(f"vocab2mdCacheV2. problem processing {vocab_location}")
            return 1

def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    L = getLogger()
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    if f=="":
        result = subprocess.run(subprocess_args)
    else:
        result = subprocess.run(subprocess_args, stdout=f)
#    L.debug(f"container call result {result.returncode}")
    return result.returncode




if __name__ == "__main__":
    main()
