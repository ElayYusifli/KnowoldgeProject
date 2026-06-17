from __future__ import annotations

import csv
from pathlib import Path
from urllib.parse import quote

from rdflib import Graph, Literal, Namespace, RDF, RDFS, XSD


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "sample" / "courses.csv"
STUDENTS_PATH = ROOT / "data" / "sample" / "students.ttl"
OUT_PATH = ROOT / "data" / "sample" / "course_kg.ttl"
FULL_OUT_PATH = ROOT / "data" / "sample" / "full_kg.ttl"

ACR = Namespace("https://example.org/acr#")
EX = Namespace("https://example.org/acr/resource/")


def resource(prefix: str, value: str):
    slug = quote(value.strip().replace(" ", "_"), safe="_")
    return EX[f"{prefix}_{slug}"]


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def main() -> None:
    graph = Graph()
    graph.bind("acr", ACR)
    graph.bind("ex", EX)

    courses_by_code = {}

    with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    for row in rows:
        course = resource("course", row["code"])
        department = resource("department", row["department"])
        instructor = resource("instructor", row["instructor"])
        courses_by_code[row["code"]] = course

        graph.add((course, RDF.type, ACR.Course))
        graph.add((course, ACR.courseCode, Literal(row["code"])))
        graph.add((course, ACR.courseTitle, Literal(row["title"])))
        graph.add((course, ACR.credits, Literal(int(row["credits"]), datatype=XSD.integer)))
        graph.add((course, ACR.level, Literal(int(row["level"]), datatype=XSD.integer)))
        graph.add((course, ACR.offeredBy, department))
        graph.add((course, ACR.taughtBy, instructor))

        graph.add((department, RDF.type, ACR.Department))
        graph.add((department, RDFS.label, Literal(row["department"])))
        graph.add((instructor, RDF.type, ACR.Instructor))
        graph.add((instructor, RDFS.label, Literal(row["instructor"])))

        for topic_name in split_values(row["topics"]):
            topic = resource("topic", topic_name)
            graph.add((topic, RDF.type, ACR.Topic))
            graph.add((topic, RDFS.label, Literal(topic_name)))
            graph.add((course, ACR.coversTopic, topic))

        for skill_name in split_values(row["skills"]):
            skill = resource("skill", skill_name)
            graph.add((skill, RDF.type, ACR.Skill))
            graph.add((skill, RDFS.label, Literal(skill_name)))
            graph.add((course, ACR.developsSkill, skill))

    for row in rows:
        course = courses_by_code[row["code"]]
        for prerequisite_code in split_values(row["prerequisites"]):
            graph.add((course, ACR.hasPrerequisite, courses_by_code[prerequisite_code]))

    graph.serialize(destination=OUT_PATH, format="turtle")

    full_graph = Graph()
    full_graph.bind("acr", ACR)
    full_graph.bind("ex", EX)
    full_graph.parse(OUT_PATH, format="turtle")
    full_graph.parse(STUDENTS_PATH, format="turtle")
    full_graph.serialize(destination=FULL_OUT_PATH, format="turtle")

    print(f"Wrote {OUT_PATH}")
    print(f"Wrote {FULL_OUT_PATH}")


if __name__ == "__main__":
    main()
