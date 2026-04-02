# Cron Setup (Local Machine)

## Goal
Run the weekly maintenance job every Monday at 09:00 Asia/Shanghai on the local machine.

## 1. Create local config

```bash
cd /root/.openclaw/workspace-scholar/Awesome-Personalized-LLMs
mkdir -p config
cp config.weekly_maintenance.env.example config/weekly_maintenance.env
```

Then edit `config/weekly_maintenance.env` and make sure these are correct:
- `DIGEST_EMAIL_TO`
- `SMTP_HOST=smtp.qq.com`
- `SMTP_PORT=465`
- `SMTP_USER`
- `SMTP_FROM`
- `SMTP_PASS`

## 2. Make the runner executable

```bash
chmod +x /root/.openclaw/workspace-scholar/Awesome-Personalized-LLMs/scripts/run_weekly_maintenance.sh
```

## 3. Test manually

```bash
cd /root/.openclaw/workspace-scholar/Awesome-Personalized-LLMs
bash scripts/run_weekly_maintenance.sh
```

## 4. Install cron job

Open crontab:

```bash
crontab -e
```

Add:

```cron
CRON_TZ=Asia/Shanghai
0 9 * * 1 /bin/bash /root/.openclaw/workspace-scholar/Awesome-Personalized-LLMs/scripts/run_weekly_maintenance.sh >> /root/.openclaw/workspace-scholar/Awesome-Personalized-LLMs/logs/cron.log 2>&1
```

## 5. Verify

```bash
crontab -l
```

## Current scaffold limitation
The current scaffold already supports:
- local config loading
- SMTP email sending
- log writing
- scheduled execution entrypoint

The next implementation step is to replace placeholder candidate generation with real arXiv retrieval, filtering, deduplication, README mutation, branch creation, push, and PR creation.
