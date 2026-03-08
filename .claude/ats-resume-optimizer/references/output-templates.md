# Output Templates and Schemas

## Keyword Injection — Internal Reasoning Template

When injecting missing keywords into existing resume content, reason through this structure internally before writing any output. This ensures every keyword addition is grounded in what the candidate actually did, not invented.

```
KEYWORDS TO INJECT: [list from JD gap analysis]
MASTER RESUME (source of truth): [original resume content]
JOB DESCRIPTION CONTEXT: [relevant JD excerpts]

RULES:
1. Only add keywords where the master resume provides supporting evidence
2. Do NOT add skills, technologies, or certifications not present in the master resume
3. Rephrase existing bullet points to include keywords — do not invent new content
4. Maintain factual accuracy — if unsure whether candidate has a skill, flag it as a gap, do not inject
5. Do not use em-dashes or AI buzzwords (see Word Choice blacklist in SKILL.md)

FOR EACH KEYWORD:
- Does the master resume contain evidence that supports this keyword? (Yes/No)
- If Yes: which bullet or section supports it? How can I rephrase to include it naturally?
- If No: mark as genuine gap, do not inject
```

This is not shown to the user — it is your internal check before writing rewritten bullets.

## Gap Analysis Table — Full Example

```
## ATS Gap Analysis

### Stripe — Senior Software Engineer
Estimated ATS Pass Probability: 40-55% | Tier 1 Match: 3/6 | Tier 2 Match: 8/14 | Format Score: Good

| Gap | Severity | Current State | Suggestion | Update Section |
|-----|----------|--------------|------------|----------------|
| "Distributed systems" keyword missing | Critical | No mention of distributed systems | Add "Distributed Systems" to Skills section; reframe the payment processing work: "Engineered distributed payment processing system handling 50K TPS" | Skills, Experience |
| "Go" or "Golang" not present | Critical | Resume only lists Python, Java | If candidate knows Go, add to Skills. If not, note as genuine gap | Skills |
| "API design" not mentioned | Critical | Has REST API experience but not named | Add "API Design & Development (REST, GraphQL)" to Skills; add "Designed RESTful APIs consumed by 12 internal teams" to most recent role | Skills, Experience |
| "Payment processing" mentioned only once | Moderate | One bullet in 2020 role | Move payment context into summary; add at least one more bullet in recent role mentioning fintech/payment domain | Summary, Experience |
| No quantified scale metrics | Moderate | Generic "improved performance" | Add scale: "Improved API response time by 35%, reducing p99 latency from 800ms to 180ms at 10K RPS" | Experience |
| "Kubernetes" / "K8s" missing | Moderate | Has Docker but not orchestration | Add if used; add "containerization (Docker, Kubernetes)" to Skills | Skills |
| "Code review" / "mentoring" not present | Nice-to-have | No mention of team development | Add "led weekly code reviews for team of 5 engineers" if accurate | Experience |

**Your biggest universal wins across all target companies:**
1. Add a dedicated Skills section with exact tool names (Python, AWS, SQL etc.) — this single change improves ATS score for every JD
2. Add scale metrics to your 3 most recent roles (even approximate ones like "~1M daily active users" are better than none)
3. Update your Summary to mirror each company's job title — takes 2 minutes and adds 15% to ATS score
```

---

## Rewritten Bullet Examples

### Before / After Pattern

**Original bullet:**
> Worked on the backend system for customer payments and improved performance

**Problems:**
- No action verb specificity (ATS doesn't weight "worked on" highly)
- No keywords from JD (distributed systems, API, Go, payment processing)
- No metrics

**Rewritten:**
> Engineered distributed payment processing microservice in Python (migrating to Go) handling 50K daily transactions, reducing checkout latency by 35% through async queue optimization

**Why this works:**
- "Distributed" + "payment processing" + "microservice" hit three Tier 1 keywords
- "(migrating to Go)" acknowledges learning without fabricating proficiency
- Metric (35%) + scale (50K daily) signals seniority

---

**Original bullet:**
> Helped design APIs for mobile app

**Problems:**
- "Helped" undersells — ATS and humans both weight this as junior
- No API type (REST? GraphQL?)
- No scale or impact

**Rewritten:**
> Designed and documented RESTful APIs for iOS/Android mobile client, serving 200K monthly active users with 99.9% uptime SLA

**Why this works:**
- Verb upgrade: "Designed and documented" vs "helped"
- Keyword injection: "RESTful APIs", "iOS/Android"
- Scale (200K MAU) + reliability signal (99.9% SLA)

---

## Summary Section — Before / After

**Original:**
> Experienced software developer with 6 years in backend development. Passionate about building great products.

**Problems:**
- Generic opener (ATS sees this 10,000 times)
- "Software developer" doesn't match target title "Senior Software Engineer"
- Zero keywords

**Rewritten for Stripe:**
> Senior Software Engineer with 6 years building distributed backend systems in Python and Java. Specialized in high-throughput API design, payment processing infrastructure, and microservices architecture. Brings a track record of shipping reliable systems at scale (10K-50K RPS) with a focus on measurable performance improvement.

**Why this works:**
- Title match: "Senior Software Engineer" in first line
- 5 Tier 1/2 keywords: distributed, API design, payment processing, microservices, performance
- Scale signal (10K-50K RPS) for hiring manager

---

## Resume JSON Schema

When generating DOCX/PDF with the bundled script, structure the resume as this JSON:

```json
{
  "font_family": "sans-serif",
  "candidate": {
    "name": "Jane Smith",
    "target_title": "Senior Software Engineer",
    "email": "jane@example.com",
    "phone": "+1-555-0100",
    "location": "San Francisco, CA",
    "linkedin": "linkedin.com/in/janesmith",
    "github": "github.com/janesmith"
  },
  "summary": "Senior Software Engineer with 6 years...",
  "skills": [
    {
      "category": "Languages",
      "items": ["Python", "Java", "Go", "TypeScript"]
    },
    {
      "category": "Frameworks",
      "items": ["FastAPI", "Spring Boot", "React"]
    },
    {
      "category": "Cloud & Infrastructure",
      "items": ["AWS (EC2, S3, Lambda, RDS)", "Docker", "Kubernetes"]
    },
    {
      "category": "Methodologies",
      "items": ["Distributed Systems", "Microservices", "REST API Design", "Agile/Scrum", "CI/CD"]
    }
  ],
  "experience": [
    {
      "title": "Senior Backend Engineer",
      "company": "Acme Corp",
      "location": "San Francisco, CA",
      "start_date": "January 2021",
      "end_date": "Present",
      "bullets": [
        "Engineered distributed payment processing microservice in Python handling 50K daily transactions, reducing checkout latency by 35%",
        "Designed RESTful APIs for iOS/Android mobile client serving 200K monthly active users with 99.9% uptime SLA",
        "Led weekly code reviews for team of 5 engineers; mentored 2 junior engineers to mid-level promotion within 18 months"
      ]
    },
    {
      "title": "Software Engineer",
      "company": "Beta Startup",
      "location": "Remote",
      "start_date": "June 2018",
      "end_date": "December 2020",
      "bullets": [
        "Built data pipeline in Python + AWS Lambda processing 2M daily events with p99 latency under 200ms",
        "Migrated monolithic application to microservices architecture, reducing deployment time from 2 hours to 8 minutes"
      ]
    }
  ],
  "education": [
    {
      "degree": "B.S. Computer Science",
      "institution": "University of California, Berkeley",
      "graduation": "May 2018",
      "gpa": null,
      "notes": "Dean's List 2016-2018"
    }
  ],
  "certifications": [
    {
      "name": "AWS Solutions Architect — Associate",
      "issuer": "Amazon Web Services",
      "date": "March 2022"
    }
  ],
  "projects": []
}
```

---

## Hiring Manager Quick Take — Format

After the ATS optimization, always close with this section:

```
### Hiring Manager Quick Take (6-second read)

**Passes the skim test**: [Yes / Partially / No] — [one sentence on why]

**Would follow up on**: [1-2 things a hiring manager would want to know more about — framed as curiosity, not red flags]

**Potential red flags to address in interview**: [1-2 honest observations — short tenure, gaps, title inflation risk, etc.]
```

Example:
```
### Hiring Manager Quick Take (6-second read)

**Passes the skim test**: Partially — the Summary now leads with the right title and keywords, but the most recent role's bullets bury the lead. Move the distributed systems bullet to position 1 in that role.

**Would follow up on**: The payment processing work at Acme — the scale numbers are strong but I'd want to know if they owned the system end-to-end or were a contributor

**Potential red flags to address in interview**: Gap between Beta Startup (Dec 2020) and Acme Corp (Jan 2021) is 1 month — no action needed. If asked, this was a standard transition.
```
