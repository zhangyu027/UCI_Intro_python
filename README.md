# UCI 427.62 Python for Data Analysis — Updated Teaching Repo

This package has been refreshed so students can run the course materials from the repository folder without editing old instructor-specific local paths.

## Recommended setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Open notebooks from the repo root or from the `Assignments/` and `In-Class Practice/` folders. Dataset paths now point to `../Data/...`.

## Folder guide

- `Assignments/` — homework notebooks, assignment PDFs, and supporting scripts.
- `In-Class Practice/` — guided practice notebooks by module/week.
- `Data/` — cleaned teaching datasets and `DATASET_INVENTORY.csv`.
- `Slides/` — lecture slides and exported PDFs.
- `Syllabus/` — syllabus and grading reference materials.
- `Other Materials/` — supporting KPI/business reading materials.

## 2026 refresh notes

- Replaced hard-coded local file paths with relative repo paths.
- Added missing sample datasets used by date/groupby/plotting notebooks.
- Added a dataset inventory and homework codebook for easier course management.
- Added `.gitignore` and `requirements.txt` for GitHub readiness.
- Cleaned Mac metadata files from the working package.

## Instructor notes

For an introductory analytics class, keep grading focused on reproducible notebooks, correct use of pandas, clear interpretation, and simple business communication. Avoid making deployment, package management, or advanced ML the center of the course unless those topics are explicitly part of the learning outcomes.
