# Smart Academic Course Recommendation Knowledge Graph

---

## Problem and Objective

- Course selection requires prerequisite, interest, and skill reasoning
- Catalog text is not machine-interpretable
- Objective: build an ontology-backed course recommendation knowledge graph

---

## Competency Questions

- Which courses match a student's interests?
- Which prerequisites are missing?
- Which skills does a course develop?
- Which courses support a target learning path?

---

## Ontology Scope

- Courses
- Students
- Instructors
- Departments
- Topics
- Skills
- Recommendations

---

## Core Classes

- `acr:Course`
- `acr:Student`
- `acr:Instructor`
- `acr:Department`
- `acr:Topic`
- `acr:Skill`
- `acr:Recommendation`

---

## Main Properties

- `acr:hasPrerequisite`
- `acr:coversTopic`
- `acr:developsSkill`
- `acr:completedCourse`
- `acr:interestedIn`
- `acr:recommendedCourse`

---

## Data Acquisition

- Sample CSV course catalog
- Course code, title, credits, level
- Department and instructor
- Curated topic and skill annotations
- Prerequisite mappings

---

## Knowledge Graph Construction

- CSV input is transformed into RDF/Turtle
- Courses become RDF resources
- Topics, skills, instructors, and departments are reused
- Prerequisite links are added between courses

---

## Example SPARQL Query

Find courses matching a student's interests while excluding courses with unmet prerequisites.

File: `queries/recommend_courses.rq`

---

## SHACL Validation

- Course code is required
- Course title is required
- Credits must be between 1 and 10
- Level must be between 1 and 4
- Recommendations must point to a student and course

---

## LLM Integration

- Student asks a natural-language question
- LLM maps request to topics or skills
- System runs SPARQL query
- LLM explains only graph-grounded results

---

## Findings

- Ontology improves explainability
- SHACL catches incomplete catalog data
- SPARQL supports transparent recommendations
- Modeling recommendations as resources enables confidence and explanation metadata

---

## Limitations and Future Work

- Current dataset is small
- Skill annotation is manually curated
- Future work: larger catalog, prerequisite path reasoning, user evaluation

---

## Repository and Documentation

- GitHub Repository URL: TODO
- WIDOCO Documentation URL: TODO

