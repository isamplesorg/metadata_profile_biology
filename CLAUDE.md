# CLAUDE.md

## Project overview

This repository contains a SKOS vocabulary (RDF/Turtle) for the iSamples biology metadata profile — basic taxon classes used as the sampled feature for biological material samples. It also functions as a GitHub Action that converts SKOS Turtle files to HTML documentation via a pipeline: Turtle → SQLite (navocab) → Markdown (vocab2mdCacheV2) → HTML (Quarto).

GitHub Pages landing page: <http://isamples.org/metadata_profile_biology/> — generated from `docs/readme.md`. `https://isamplesorg.github.io/metadata_profile_biology/` 301-redirects to the `isamples.org` URL.

### Open setup item: gh-pages branch

As of 2026-04-22, this repo has **only** a `main` branch on origin — no `gh-pages` branch exists. The workflow now targets `gh-pages` (previously targeted the bogus `Issue17Chromista-kingdom`). On the next successful `process_vocab.yml` run, the JamesIves/github-pages-deploy-action step will create the `gh-pages` branch automatically. After that branch exists, confirm that GitHub repo **Settings → Pages** is configured to serve from `gh-pages` branch, `/docs` folder — the currently-live landing page is likely being served from `main/docs` as a fallback, and will need to be repointed once `gh-pages` is populated.

## Repository structure

- `vocabulary/` — Source SKOS Turtle (.ttl) files
- `tools/` — Python processing tools (vocab.py, vocab2mdCacheV2.py, navocab/)
- `docs/` — Generated HTML/Markdown output (deployed to gh-pages)
- `cache/` — SQLite database directory (should be transient)
- `.github/actions/github_action_main.py` — Docker entrypoint for the pipeline
- `.github/workflows/` — GitHub Actions workflow definitions
- `Dockerfile` — Processing container, pinned to `python:3.12-slim`
- `action.yml` — GitHub Action metadata

## Vocabularies

| File | ConceptScheme CURIE |
|------|-------------------|
| `biology_sampledfeature_extension.ttl` | `bioe:biologicentityvocabulary` |

## Pipeline fixes applied 2026-04-22

This repo shares the same codebase as the other `metadata_profile_*` repositories (derived from isamplesorg/vocabularyTemplate). The following fixes were ported from the earth_science repo's 2026-04-22 cleanup:

1. **Dockerfile**: pinned to `python:3.12-slim` so `pkg_resources` remains available (Python 3.14 drops it).
2. **tools/requirements.txt**: added `setuptools<81` (rdflib-sqlalchemy needs `pkg_resources`).
3. **Stale cache DB**: removed `cache/vocabularies-SMR-Samsung.db` (untracked, ~570KB).
4. **Workflow deploy branch**: both `process_vocab.yml` deploy steps now target `gh-pages` (was the bogus `Issue17Chromista-kingdom`). See open setup item above.
5. **github_action_main.py**: resets the cache DB before each vocabulary (fresh DB per vocab, no cross-vocab pollution); processes load + render per vocab in one pass instead of two separate loops.
6. **vocab2mdCacheV2.py**: `getVocabRoot` now UNIONs `skos:topConceptOf` and `skos:hasTopConcept`; `getNarrower` falls back to an unscoped `skos:broader` query when concepts omit `skos:inScheme`.
7. **navocab.purge_store**: no longer crashes on undefined `graph` local; logs a warning and defers to external file deletion.
8. **.gitignore**: expanded to cover `.claude/`, `.venv/`, `/testoutput/local_run/`, and `tools/navocab/__pycache__/`.

## GitHub Actions workflows

- **Process vocabularies** (`process_vocab.yml`) — Manual dispatch. Processes the single biology vocabulary.
- **Test docs** (`testdocs_process_vocab.yml`) — Manual dispatch. Test workflow.
- **Test JSON** (`testjson_process_vocab.yml`) — Manual dispatch. JSON generation test.

## Processing pipeline

Same as the earth_science and archaeology repos:
1. `vocab.py load <file.ttl> <conceptscheme-uri>` — parse Turtle, store in SQLite
2. `vocab2mdCacheV2.py <db> <conceptscheme-uri>` — query DB, generate Markdown
3. `quarto render <file.md> -t html` — render Markdown to HTML
4. Deploy HTML to gh-pages via JamesIves/github-pages-deploy-action
