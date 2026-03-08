#!/usr/bin/env python3
"""
Generate an ATS-safe PDF resume from a resume JSON structure.
Uses ReportLab for clean, parseable PDF output.

This is a fallback when LibreOffice is not available.
Prefer: libreoffice --headless --convert-to pdf resume.docx

Usage:
    python generate_pdf.py --resume-json '<json>' --output-path 'resume.pdf'
    python generate_pdf.py --resume-file resume.json --output-path resume.pdf
"""

import argparse
import json
import os
import sys


def install_and_import():
    try:
        import reportlab
    except ImportError:
        print("Installing reportlab...", file=sys.stderr)
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab", "-q"])


def generate_pdf(resume_data, output_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable
    )
    from reportlab.lib.enums import TA_CENTER, TA_LEFT

    # Page setup
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    name_style = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontSize=18,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica',
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=2,
        textColor=colors.black,
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10.5,
        fontName='Helvetica',
        spaceBefore=1,
        spaceAfter=1,
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10.5,
        fontName='Helvetica',
        leftIndent=15,
        firstLineIndent=-10,
        spaceBefore=1,
        spaceAfter=1,
    )
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        spaceBefore=6,
        spaceAfter=1,
    )
    job_detail_style = ParagraphStyle(
        'JobDetail',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Oblique',
        spaceBefore=0,
        spaceAfter=2,
    )

    candidate = resume_data.get("candidate", {})

    # Name
    story.append(Paragraph(candidate.get("name", "Your Name"), name_style))

    # Contact info
    contact_parts = []
    for field in ["email", "phone", "location", "linkedin", "github"]:
        if candidate.get(field):
            contact_parts.append(candidate[field])
    if contact_parts:
        story.append(Paragraph(" | ".join(contact_parts), contact_style))

    def add_section(title):
        story.append(Paragraph(title.upper(), section_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.black, spaceAfter=3))

    # Summary
    summary = resume_data.get("summary", "")
    if summary:
        add_section("Professional Summary")
        story.append(Paragraph(summary, body_style))
        story.append(Spacer(1, 4))

    # Skills
    skills = resume_data.get("skills", [])
    if skills:
        add_section("Technical Skills")
        for group in skills:
            line = f"<b>{group.get('category', 'Skills')}:</b> {', '.join(group.get('items', []))}"
            story.append(Paragraph(line, body_style))

    # Experience
    experience = resume_data.get("experience", [])
    if experience:
        add_section("Work Experience")
        for job in experience:
            title_line = f"<b>{job.get('title', '')}</b>"
            if job.get("company"):
                title_line += f" — {job['company']}"
            story.append(Paragraph(title_line, job_title_style))

            detail_parts = []
            if job.get("location"):
                detail_parts.append(job["location"])
            dates = job.get("start_date", "")
            if job.get("end_date"):
                dates += f" – {job['end_date']}"
            if dates:
                detail_parts.append(dates)
            if detail_parts:
                story.append(Paragraph(" | ".join(detail_parts), job_detail_style))

            for bullet in job.get("bullets", []):
                story.append(Paragraph(f"• {bullet}", bullet_style))

    # Education
    education = resume_data.get("education", [])
    if education:
        add_section("Education")
        for edu in education:
            degree_line = f"<b>{edu.get('degree', '')}</b>"
            if edu.get("institution"):
                degree_line += f" — {edu['institution']}"
            story.append(Paragraph(degree_line, job_title_style))

            detail_parts = []
            if edu.get("graduation"):
                detail_parts.append(edu["graduation"])
            if edu.get("gpa"):
                detail_parts.append(f"GPA: {edu['gpa']}")
            if edu.get("notes"):
                detail_parts.append(edu["notes"])
            if detail_parts:
                story.append(Paragraph(" | ".join(detail_parts), job_detail_style))

    # Certifications
    certifications = resume_data.get("certifications", [])
    if certifications:
        add_section("Certifications")
        for cert in certifications:
            line = f"<b>{cert.get('name', '')}</b>"
            parts = []
            if cert.get("issuer"):
                parts.append(cert["issuer"])
            if cert.get("date"):
                parts.append(cert["date"])
            if parts:
                line += f" — {' | '.join(parts)}"
            story.append(Paragraph(line, body_style))

    # Projects
    projects = resume_data.get("projects", [])
    if projects:
        add_section("Projects")
        for project in projects:
            title_line = f"<b>{project.get('name', '')}</b>"
            if project.get("tech"):
                title_line += f" ({project['tech']})"
            story.append(Paragraph(title_line, job_title_style))
            for bullet in project.get("bullets", []):
                story.append(Paragraph(f"• {bullet}", bullet_style))

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc.build(story)
    print(f"PDF saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate ATS-safe PDF resume")
    parser.add_argument("--resume-json", help="Resume data as JSON string")
    parser.add_argument("--resume-file", help="Path to resume JSON file")
    parser.add_argument("--output-path", required=True, help="Output .pdf file path")
    args = parser.parse_args()

    if not args.resume_json and not args.resume_file:
        print("Error: provide --resume-json or --resume-file", file=sys.stderr)
        sys.exit(1)

    if args.resume_file:
        with open(args.resume_file) as f:
            resume_data = json.load(f)
    else:
        resume_data = json.loads(args.resume_json)

    install_and_import()
    generate_pdf(resume_data, args.output_path)


if __name__ == "__main__":
    main()
