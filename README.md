# Smart Academic Course Recommendation Knowledge Graph

This repository contains a term project for the Knowledge Engineering and Ontologies course. The project models university courses, students, skills, topics, instructors, prerequisites, and recommendations as an ontology-backed knowledge graph.

## Project Objective

The objective is to build a reproducible ontology and knowledge graph that can answer academic advising questions such as:

- Which courses match a student's interests and completed prerequisites?
- Which skills does a course develop?
- Which learning paths prepare a student for a target skill?
- Which recommendations violate prerequisite or credit constraints?

## Dataset Sources

The current repository includes a small reproducible sample dataset in `data/sample/courses.csv`. In the final version, replace or extend it with data from:

- Public university course catalogs
- Department curriculum pages
- Manually curated prerequisite and skill mappings
- Student profile examples created for evaluation

## Repository Structure

- `ontology/` - OWL/Turtle ontology files and namespace definitions
- `data/sample/` - sample CSV and generated RDF data
- `queries/` - SPARQL queries used in the report and presentation
- `shacl/` - SHACL validation shapes
- `src/` - scripts for generating RDF from CSV data
- `docs/` - WIDOCO output target for ontology documentation
- `docs/specification_v2.md` - Phase 2 ontology specification document
- `report/` - project report draft
- `presentation/` - presentation slide draft

## Setup

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate RDF data:

```bash
python3 src/build_graph.py
```

Validate the combined graph with SHACL, if `pyshacl` is installed:

```bash
python3 -m pyshacl -s shacl/course_shapes.ttl -d data/sample/full_kg.ttl -f human
```

## WIDOCO Documentation

Generate ontology documentation with WIDOCO:

```bash
java -jar widoco.jar -ontFile ontology/course-recommendation.ttl -outFolder docs -rewriteAll -webVowl
```

Publish the `docs/` folder with GitHub Pages and add the resulting URL to the report and final presentation.

## Team Members

- Elay Yusifli 210315090
