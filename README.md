# Ian Alleyne | Applied AI & Advanced Analytics

**MIT xPRO Professional Certificate in Advanced Analytics with AI, ML, and Data Science**

**100% in all 24 modules · 813 / 813 points · 144 graded activities**

[Explore the portfolio](https://IRATT.github.io/) · [Verify the certificate](https://certificates.emeritus.org/09a749b7-fb41-4777-8b93-559e1039989c) · [Development plan](BUILD_PLAN.md)

This portfolio connects engineering judgment, data science and responsible implementation through 24 module pages and four detailed case studies:

- **Clinical AI:** clinician-reviewed documentation and a governed analytics foundation.
- **Alarm intelligence:** staged, accountable AI support for critical infrastructure.
- **Production optimization:** a modeled weekly contribution of $2,316 in the CSF course case.
- **Network logistics:** a recorded minimum transportation cost of $541,000 in a Gurobipy course model.

The portfolio draws on 19 privately retained submitted files and five text-box responses. Public model evidence comprises four reviewed numerical CSV extracts and one screened notebook. Codio-only assignments are represented by summaries and verified final grades, following the program’s export guidance.

## Evidence and authorship

Grades are final recorded outcomes, including accepted resubmissions, reviewed on 4 November 2026. Course cases, starter code and templates retain their original attribution. This is an independent learner portfolio, not an MIT-operated site. AI assistance was used to organize, edit and build the portfolio.

Course-case results are not realized client outcomes. Clinical and alarm-management applications are proposals or portfolio extensions unless expressly identified otherwise. See `methodology.html` for evidence boundaries and documented corrections.

## Build and maintain

The website is static HTML, CSS and JavaScript, with a Python standard-library generator. No build-time web framework or client-side dependency is required.

```bash
python build.py
python validate_site.py
```

`data/modules.json` contains the 24 module records and final activity scores. Reviewed numerical extracts and the public notebook live in `evidence/`. Full original papers, workbooks and text responses remain private. Generated pages are committed so GitHub Pages can serve the repository root directly.

Optional numerical cross-checks use SciPy:

```bash
python validate_models.py
```

Publishing: GitHub Pages, `main` branch, repository root. No private learner URLs, account identifiers, credentials, patient records or private repository content are included.

## Rights

Portfolio presentation and original commentary © 2026 Ian Alleyne. Embedded educational cases, starter code, templates and third-party material retain their respective ownership. No blanket license is applied to third-party coursework.
