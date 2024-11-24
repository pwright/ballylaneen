
# MkDocs Automatic Build Repository

This repository is configured to build a MkDocs site automatically every day using GitHub Actions. It also generates a `today.md` file in the `docs/` directory linking to today's "Deaths in YYYY" Wikipedia page.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine.
- Virtual environment tools (`venv`) available.
- Git installed.

### Steps to Run Locally

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set Up Virtual Environment**

   Run the `setup_env.sh` script to create and activate a virtual environment, and install the required dependencies.

   ```bash
   ./setup_env.sh
   pip install -r requirements.txt
   ```

3. **Generate `today.md`**

   Run the `create_today_md.py` script to generate the `today.md` file with a link to today's "Deaths in YYYY" Wikipedia page.

   ```bash
   python create_today_md.py
   ```

4. **Build the MkDocs Site**

   Use MkDocs to build the site.

   ```bash
   mkdocs build
   ```

   The site will be generated in the `site/` directory.

5. **Serve Locally**

   Serve the MkDocs site locally to preview it.

   ```bash
   mkdocs serve
   ```

   Open your browser and navigate to `http://127.0.0.1:8000`.

### GitHub Actions Setup

This repository includes a GitHub Actions workflow that:
- Runs daily at midnight UTC.
- Generates the `today.md` file.
- Builds the MkDocs site.
- Deploys the site to GitHub Pages.

No additional setup is needed for the GitHub Actions workflow; it will run automatically once pushed to a GitHub repository.

## File Overview

- `requirements.txt`: Lists the dependencies for MkDocs.
- `setup_env.sh`: Script to set up the Python virtual environment and install dependencies.
- `create_today_md.py`: Script to generate the `today.md` file.
- `docs/index.md`: The homepage for the MkDocs site.
- `.github/workflows/build.yml`: GitHub Actions workflow to build and deploy the site.

## Notes

- Ensure that the repository is linked to a GitHub Pages deployment for the site to be served publicly.
- Modify the cron schedule in `.github/workflows/build.yml` if needed.

Happy documenting!
