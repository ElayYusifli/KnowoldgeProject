from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "report" / "project_report.md"
OUTPUT = ROOT / "report" / "Project_Report.pdf"


def clean_inline(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("`", "")
        .replace("**", "")
    )


def build_pdf() -> None:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=26,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#1f2937"),
            spaceBefore=12,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletBody",
            parent=styles["Body"],
            leftIndent=12,
        )
    )

    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Smart Academic Course Recommendation Knowledge Graph",
        author="TODO: Team Name",
    )

    story = []
    bullet_buffer = []

    def flush_bullets() -> None:
        if not bullet_buffer:
            return
        story.append(
            ListFlowable(
                [ListItem(Paragraph(item, styles["BulletBody"])) for item in bullet_buffer],
                bulletType="bullet",
                start="circle",
                leftIndent=18,
            )
        )
        story.append(Spacer(1, 4))
        bullet_buffer.clear()

    for raw_line in SOURCE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            flush_bullets()
            continue

        if line.startswith("- "):
            bullet_buffer.append(clean_inline(line[2:]))
            continue

        flush_bullets()

        if line.startswith("# "):
            story.append(Paragraph(clean_inline(line[2:]), styles["ReportTitle"]))
        elif line.startswith("## "):
            story.append(Paragraph(clean_inline(line[3:]), styles["SectionTitle"]))
        elif line[0:3] in {"1. ", "2. ", "3. ", "4. "}:
            story.append(Paragraph(clean_inline(line), styles["Body"]))
        else:
            story.append(Paragraph(clean_inline(line), styles["Body"]))

    flush_bullets()
    document.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build_pdf()

