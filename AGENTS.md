# AGENTS.md

Short, agent-operational guide. See [CLAUDE.md](CLAUDE.md) for project history and fix log.

## What this repo is

An iSamples biology metadata profile. Single SKOS vocabulary (basic taxon classes used as the sampled feature). Pipeline: Turtle → SQLite via `tools/vocab.py` (navocab) → Markdown via `tools/vocab2mdCacheV2.py` → HTML via Quarto. Runs in Docker as a GitHub Action (`action.yml`, `.github/workflows/process_vocab.yml`).

Landing page: <http://isamples.org/metadata_profile_biology/> (intended to be served from `gh-pages/docs` once that branch exists — see **Open setup item** below).

## Open setup item

As of 2026-04-22, origin has only `main`. Workflow now targets `gh-pages`; first successful run creates it. After that, confirm **Settings → Pages** is pointed at `gh-pages` branch, `/docs` folder.

## Vocabularies

| Slug (no ext) | ConceptScheme CURIE |
|---|---|
| `biology_sampledfeature_extension` | `bioe:biologicentityvocabulary` |

## Local verification (Option A — no Docker)

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r tools/requirements.txt

V=biology_sampledfeature_extension
U=bioe:biologicentityvocabulary

mkdir -p testoutput/local_run
rm -f cache/vocabularies.db
.venv/Scripts/python.exe tools/vocab.py --verbosity ERROR -s cache/vocabularies.db load "vocabulary/$V.ttl" "$U"
.venv/Scripts/python.exe tools/vocab2mdCacheV2.py cache/vocabularies.db "$U" > "testoutput/local_run/$V.md"
quarto render "testoutput/local_run/$V.md" -t html
```

## Docker verification (Option B — matches the action)

```bash
docker build -t bio-vocab .
docker run --rm \
  -e INPUT_ACTION=docs \
  -e INPUT_PATH=/app \
  -e INPUT_INPUTTTL='biology_sampledfeature_extension' \
  -e INPUT_INPUTVOCABURI='bioe:biologicentityvocabulary' \
  -v "/$(pwd)/docs://app/docs" \
  bio-vocab
```

The `//` prefix on the volume path is a Git-Bash-on-Windows workaround; drop it on Linux/macOS.

## Do not touch

- `.idea/workspace.xml`, `vocabulary/.project` — JetBrains / Eclipse IDE state.
- Any `*-SMR-Samsung.*` files — owner's local experiments.
- Pre-existing staged or pending deletions you didn't introduce — leave them for the owner to commit separately.

## Common fix pattern (for porting to sibling repos)

This codebase descends from `isamplesorg/vocabularyTemplate`. The 2026-04-22 fix set (see CLAUDE.md for per-file detail):

1. `Dockerfile` — pin `FROM python:3.12-slim`.
2. `tools/requirements.txt` — add `setuptools<81`.
3. Remove any stale `cache/vocabularies-*.db` files.
4. `.github/workflows/process_vocab.yml` — verify every slug in `inputttl` matches an actual `vocabulary/*.ttl`; verify deploy `branch:` target is `gh-pages` (not a stale feature branch — this repo had `Issue17Chromista-kingdom`).
5. `.github/actions/github_action_main.py` — reset cache DB per vocab, process load+md+render in a single per-vocab loop, use `enumerate`.
6. `tools/vocab2mdCacheV2.py` — `getVocabRoot` UNIONs `skos:topConceptOf` + `skos:hasTopConcept`; `getNarrower` falls back to unscoped `skos:broader` when `skos:inScheme` is absent.
7. `tools/navocab/__init__.py::purge_store` — stop referencing undefined `graph`; log + defer to external file deletion.

Applied and verified in: earth_science, archaeology, biology.
