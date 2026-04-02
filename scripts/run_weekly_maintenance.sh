#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$ROOT_DIR/config/weekly_maintenance.env"
LOG_DIR="$ROOT_DIR/logs"
mkdir -p "$LOG_DIR" "$ROOT_DIR/output" "$ROOT_DIR/config"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Missing config file: $CONFIG_FILE" >&2
  echo "Copy config.weekly_maintenance.env.example to config/weekly_maintenance.env first." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$CONFIG_FILE"
set +a

cd "${REPO_DIR:-$ROOT_DIR}"
TODAY="$(date +%F)"
BRANCH="weekly/arxiv-$TODAY"
PR_TITLE="weekly: arXiv update for $TODAY"

log() {
  echo "[$(date '+%F %T')] $*" | tee -a "$LOG_DIR/weekly.log"
}

log "Starting weekly maintenance"
git checkout "${DEFAULT_BRANCH:-main}"
git pull --ff-only origin "${DEFAULT_BRANCH:-main}"

python3 scripts/weekly_arxiv_update.py 2>&1 | tee -a "$LOG_DIR/weekly.log"
python3 scripts/send_email_digest.py 2>&1 | tee -a "$LOG_DIR/weekly.log"

if git diff --quiet -- README.md output/ docs/ scripts/ .gitignore config.weekly_maintenance.env.example 2>/dev/null; then
  log "No repository changes to commit"
  exit 0
fi

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git branch -D "$BRANCH"
fi

git checkout -b "$BRANCH"
git add README.md output/ docs/ scripts/ .gitignore config.weekly_maintenance.env.example || true
git commit -m "$PR_TITLE"
git push -u origin "$BRANCH"

gh pr create \
  --base "${DEFAULT_BRANCH:-main}" \
  --head "$BRANCH" \
  --title "$PR_TITLE" \
  --body "Automated weekly arXiv update.\n\n- source: arXiv\n- cadence: weekly\n- includes title/link updates in README\n- email digest with abstracts sent separately\n"

log "Weekly maintenance completed"
