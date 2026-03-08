# ATS Scoring Reference

## How ATS Systems Actually Work

Most companies use one of these major ATS platforms. Each has its own parsing quirks, but the scoring logic is similar:

| ATS System | Used By | Known Quirks |
|---|---|---|
| Workday | Large enterprises, Fortune 500 | Poor at parsing multi-column layouts; strict on section headers |
| Greenhouse | Tech startups, mid-market | Better parser; still penalizes non-standard formatting |
| Lever | Tech companies | Good parser; keyword matching is phrase-sensitive |
| iCIMS | Healthcare, finance, retail | Very strict; tables and graphics cause parse failures |
| Taleo (Oracle) | Government, large enterprises | Oldest parser; most strict; single-column only |
| BambooHR | SMBs | Simpler ATS; less sophisticated keyword scoring |
| LinkedIn Easy Apply | Universal | Pulls from LinkedIn profile, not resume — different optimization rules |
| SmartRecruiters | Mid-market | Good parser; weights skills section heavily |
| Jobvite | Mid-size tech | Good parser; prioritizes job title matching |

**Universal safe formatting**: single-column, standard fonts (Calibri/Arial/Georgia), no tables in experience section, no text boxes, contact info in document body (not headers/footers), PDF or DOCX (not ODT or Pages).

---

## Keyword Scoring Methodology

### How ATS Ranks Candidates

1. **Hard filters** run first: if required keywords are absent, candidate is auto-rejected before scoring
2. **Keyword frequency scoring**: each keyword match earns points; appearing in multiple sections multiplies the score
3. **Proximity scoring**: related keywords appearing near each other score higher than scattered mentions
4. **Recency weighting**: keywords in the most recent job experience weighted 2-3x over older positions
5. **Title matching**: job title match (or near-match) is often a separate high-weight score
6. **Education parsing**: degree level and field extracted separately; often hard-filtered

### Keyword Match Scoring by Section

Different resume sections carry different ATS weight (approximate, varies by system):

| Section | Approximate ATS Weight | Notes |
|---|---|---|
| Job Title (current/most recent) | Very High | Direct title match = major boost |
| Skills Section | High | ATS reads this as explicit capability declaration |
| Experience Bullets (most recent role) | High | Keyword density here matters most |
| Summary / Objective | Medium | Good for context; less weighted than skills/experience |
| Experience Bullets (older roles) | Medium-Low | Recency decay; keywords still count but less |
| Education | Low-Medium | Important when degree is a hard requirement |
| Certifications | Medium-High | Often scanned as hard requirements for regulated roles |

### Exact-Match vs. Semantic Matching

Older ATS (Taleo, iCIMS): **exact string matching only**
- "Machine Learning" ≠ "ML"
- "JavaScript" ≠ "JS"
- "Project Management" ≠ "PM"
- "Amazon Web Services" ≠ "AWS" (unless both appear)

**Fix**: Use the full keyword form from the JD *and* the abbreviation: "Machine Learning (ML)", "Amazon Web Services (AWS)"

Newer ATS (Greenhouse, Lever): partial semantic matching
- Still prefer exact match but can infer synonyms
- Still won't catch major reframings ("coded" vs "developed software")

**Safe rule**: always match the exact strings from the JD. Don't rely on semantic understanding.

---

## ATS Format Rules

### Guaranteed Parse Failures

These cause ATS to either skip the section or garble the text:

- **Tables in experience/skills section**: ATS reads left column, then right column separately — bullets become incoherent fragments
- **Text boxes**: content is invisible to most parsers
- **Graphics/logos/icons**: invisible to all parsers
- **Headers/footers**: contact info here may not be extracted; Taleo/iCIMS skip headers/footers entirely
- **Multi-column layouts**: left column often read last, creating jumbled experience order
- **Unusual fonts**: can cause character encoding issues; stick to system fonts
- **Embedded images of text**: completely invisible
- **Pages format (.pages)**: most ATS can't parse Apple's format; always export to DOCX or PDF

### Safe Formatting Checklist

- [ ] Single-column layout
- [ ] Standard section headers (see list below)
- [ ] Contact info in document body, not header/footer
- [ ] Fonts: Calibri, Arial, Georgia, Times New Roman, Garamond
- [ ] File format: DOCX preferred; PDF acceptable (not scanned PDF)
- [ ] No tables, text boxes, or graphics
- [ ] No color-coded text that carries information (ATS is colorblind)
- [ ] Dates in consistent format: Month YYYY or MM/YYYY

### ATS-Standard Section Headers

ATS systems are trained on these exact strings. Non-standard headers may not be categorized correctly:

| Standard Header | Avoid These Variants |
|---|---|
| Work Experience / Professional Experience | Career History, My Journey, What I've Done |
| Skills / Technical Skills | What I Know, Toolkit, Capabilities |
| Education | Academic Background, Schooling |
| Certifications | Licenses & Certifications, Credentials |
| Projects | Portfolio, What I've Built |
| Summary / Professional Summary | About Me, Who I Am, Introduction |
| Achievements / Awards | Recognition |

---

## Keyword Categories by Role Type

### Software Engineering / Technical Roles

High-weight keywords ATS looks for:
- **Languages**: exact names (Python, Java, Go, Rust, TypeScript)
- **Frameworks**: React, Node.js, Spring Boot, Django, FastAPI
- **Cloud**: AWS, GCP, Azure — with specific services (S3, Lambda, BigQuery, Kubernetes)
- **Methodologies**: Agile, Scrum, CI/CD, TDD, microservices, distributed systems
- **Scale signals**: numbers of users, requests per second, data volume — ATS doesn't score these but hiring managers do

### Product Management Roles

- **Delivery signals**: launched, shipped, drove, led cross-functional
- **Metrics**: DAU, MAU, retention, NPS, conversion rate, ARR
- **Methodologies**: A/B testing, roadmapping, OKRs, user research
- **Stakeholders**: engineering, design, go-to-market, executive stakeholders

### Data / Analytics Roles

- **Tools**: SQL, Python, R, Tableau, Power BI, Looker, dbt, Spark, Airflow
- **Concepts**: statistical modeling, regression, A/B testing, machine learning, data pipeline
- **Scale**: row counts, query performance, dashboard users

### Operations / Management Roles

- **Leadership signals**: managed team of X, P&L ownership, budget of $X
- **Methodologies**: Lean, Six Sigma, process improvement, OKRs, KPIs
- **Cross-functional**: "worked across", "partnered with", "aligned with"

---

## Seniority Calibration

ATS systems and hiring managers look for different signals at different levels:

### Junior / Early Career (0-3 years)
- Education and certifications carry more weight
- Project work and internships count as experience
- Skills section keyword density matters most
- Metrics less critical; focus on scope and technologies

### Mid-level (4-8 years)
- Recent experience keywords dominate
- Metrics expected on at least 50% of bullets
- Progression visible (IC → lead → manager of scope)
- Certifications relevant but not primary signal

### Senior / Lead (8-15 years)
- Leadership signals required: "Led team of X", "Architected", "Defined strategy for"
- Business impact metrics expected: revenue, cost, user scale
- Cross-functional signals: "aligned with VP-level stakeholders", "drove organizational change"
- Breadth + depth balance

### Executive (15+ years)
- P&L language, budget ownership, headcount
- Board, investor, or C-suite interaction signals
- Strategic framing: "defined 3-year roadmap", "built organization from 0 to X"
- Less technical depth, more organizational impact

---

## ATS Pass Probability Estimation

Use this heuristic to estimate ATS pass probability:

| Condition | Impact |
|---|---|
| All Tier 1 keywords present | +40% base |
| Each additional Tier 1 keyword present (up to 5) | +5% each |
| Tier 2 keyword match ≥ 70% | +20% |
| Job title match (exact or near) | +15% |
| Format: single column, standard headers | +10% |
| Quantified metrics in ≥ 60% of bullets | +5% |
| Missing 1 Tier 1 keyword | -20% |
| Missing 2+ Tier 1 keywords | -40% |
| Non-standard format (tables, multi-column) | -15% |
| Missing skills section | -10% |

Cap at 95% (no resume is guaranteed to pass every ATS configuration). Express as a range: "Estimated 55-65% ATS pass probability."

---

## Common Honest Reframing Examples

These are legitimate reframes (not fabrications):

| What resume says | What JD requires | Honest reframe |
|---|---|---|
| "Built dashboards in Tableau" | "Data visualization and reporting" | "Designed and delivered data visualizations and executive reporting dashboards using Tableau" |
| "Managed a project with 3 developers" | "Cross-functional team leadership" | "Led cross-functional delivery team of engineers, product, and design stakeholders" |
| "Reduced bug count" | "Improved system reliability" | "Improved system reliability by reducing production bug rate by 40%" |
| "Used Python for data tasks" | "Python programming" | "Python (data processing pipelines, automation scripts, API integrations)" |
| "Worked with AWS" | "Cloud infrastructure (AWS)" | "Cloud infrastructure management on AWS (EC2, S3, Lambda, CloudFormation)" |

What is never acceptable: Adding tools the candidate hasn't used, claiming leadership of projects they contributed to, inventing metrics.
