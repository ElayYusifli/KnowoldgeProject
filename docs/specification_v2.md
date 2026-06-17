# Specification Document v2

## Project

Smart Academic Course Recommendation Knowledge Graph

## Version

v2, updated on 2026-06-17

## Objective

The project models university courses, students, prerequisites, topics, skills, instructors, departments, and recommendations as an ontology-backed knowledge graph. Version 2 extends the ontology with research integration, provenance, and student behavior concepts required for Phase 2.

## Changes from v1

- Added `acr:DataSource` for documenting dataset and document provenance.
- Added `acr:ResearchStudy` for connecting architecture and modeling decisions to reviewed research.
- Added `acr:StudentBehaviorSignal` for future behavior-aware recommendation and prediction.
- Added `acr:derivedFromSource` to connect resources to datasets or documents.
- Added `acr:informedByStudy` to indicate research-grounded design decisions.
- Added `acr:hasBehaviorSignal` to connect students to observable signals.
- Added datatype properties `acr:sourceName`, `acr:sourceFormat`, `acr:signalType`, and `acr:signalValue`.
- Expanded the report with Phase 2 research integration and mandatory paper review.
- Increased SPARQL query coverage to ten query files.

## Core Classes

- `acr:Course`
- `acr:Student`
- `acr:Instructor`
- `acr:Department`
- `acr:Topic`
- `acr:Skill`
- `acr:Recommendation`
- `acr:DataSource`
- `acr:ResearchStudy`
- `acr:StudentBehaviorSignal`

## Core Object Properties

- `acr:offeredBy`
- `acr:taughtBy`
- `acr:hasPrerequisite`
- `acr:coversTopic`
- `acr:developsSkill`
- `acr:completedCourse`
- `acr:interestedIn`
- `acr:recommendedCourse`
- `acr:recommendedFor`
- `acr:derivedFromSource`
- `acr:informedByStudy`
- `acr:hasBehaviorSignal`

## Core Data Properties

- `acr:courseCode`
- `acr:courseTitle`
- `acr:credits`
- `acr:level`
- `acr:confidenceScore`
- `acr:explanation`
- `acr:sourceName`
- `acr:sourceFormat`
- `acr:signalType`
- `acr:signalValue`

## Data Acquisition Mapping

- CSV course rows map to `acr:Course`.
- Department labels map to `acr:Department`.
- Instructor labels map to `acr:Instructor`.
- Topic strings map to `acr:Topic`.
- Skill strings map to `acr:Skill`.
- Prerequisite course codes map to `acr:hasPrerequisite`.
- Student profile examples map to `acr:Student`.
- Recommendation records map to `acr:Recommendation`.
- Dataset and document origins map to `acr:DataSource`.

## Validation

The SHACL validation file remains `shacl/course_shapes.ttl`. It validates course code, course title, credit range, course level, recommendation target student, recommendation target course, and confidence score range.

## Documentation

WIDOCO documentation should be regenerated from `ontology/course-recommendation.ttl` after this v2 update.

