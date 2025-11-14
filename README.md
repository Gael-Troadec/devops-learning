# DevOps Learning Journey

**Objectif** : DevOps Junior en 18 mois (reconversion ex-militaire, opérateur nucléaire)

---

## Current Status
**Jour 10** - Flask consolidation, Permissions avancées, Docker integration

---

## Project Structure

### Scripts Foundation (Jour 1-8)
- `list_files_sorted.py` - Lister et trier fichiers
- `backup.py` - Sauvegarde automatique + error handling
- `sysinfo_disk.py` - Info système et espace disque
- `data_analyzer.py` - Analyser données CSV
- `log_analyzer.py` - Parser logs serveur
- `analyze_employees.sh` - Bash CSV analysis
- `system_monitor.py` - Real-time monitoring (CPU/memory/disk)

### Flask Consolidation (Jour 9-10)
`flask_consolidation/` - 3 variations consolidation:
- `meteo/` - Routes + JSON endpoint (météo)
- `todo/` - TODO list app
- `warhammer/` - Warhammer 40K theme (Omnissiah)

**Pattern acquis:** Routes, decorators, jsonify, debug mode

### Docker Integration (Jour 10)
`flask_docker_day10/` - Flask app containerisée:
- `app.py` - Flask minimal
- `Dockerfile` - Image build

**Pattern acquis:** FROM, WORKDIR, COPY, RUN, EXPOSE, CMD

### Permissions & Linux (Jour 10)
`app_structure/` - DevOps-realistic structure:
- `src/` (700) - Code app, owner only
- `config/` (700) - Secrets/passwords, owner only
- `logs/` (755) - Logs partagés, others read
- `data/` (755) - Data, others read
- `deploy.sh` (700) - Deployment script

**Concepts maîtrisés:**
- umask (default permissions)
- setuid (execute as owner)
- sticky bit (shared directories)
- Dossier vs fichier permissions
- Bash validation scripts

---

## Tech Stack
- **Languages:** Python 3, Bash, YAML
- **Tools:** Git/GitHub, Docker, VS Code
- **Platforms:** WSL2 Ubuntu, MacBook Pro + Linux Mint, Android + Termux
- **Documentation:** Obsidian (cloud synced)

---

## Learning Approach
✅ Hand-typed all code (no copy-paste)
✅ Error handling + logging in every script
✅ Cross-platform testing
✅ Git workflow (clean commits, rebasing)
✅ Real projects over tutorials
✅ Consolidation via variations (Flask x3, Permissions x2)

---

## Roadmap (18-24 months)

### Phase 1: Foundations (Mois 1-2) ✅ DONE
- Linux fundamentals
- Python basics
- Bash scripting
- Git workflow

### Phase 2: DevOps Exploration (Semaine 3-4)
- GitHub Actions CI/CD
- Flask + Docker advanced
- Testing automation

### Phase 3: Specialization Test (Décembre)
- DevOps track (pipelines, deployment)
- SRE track (monitoring, Prometheus/Grafana)
- Linux Admin track (hardening, Ansible)

### Phase 4: Specialization Deep-dive (Jan-Mar)
- Docker mastery
- Kubernetes intro
- CI/CD pipelines (Jenkins/GitHub Actions)

### Phase 5: Cloud (Avr-Juin)
- AWS fundamentals
- AWS certification prep
- Cloud-native patterns

### Phase 6: Job Preparation (Juillet-Sept)
- Portfolio final push
- Interview prep
- Real job search

---

## Key Learnings

### Consolidation Pattern
**Problem:** Copy-paste → understand moment → forget 24h later
**Solution:** Feynman Method + variations
- Learn concept
- Explain aloud
- Refaire de mémoire (timer strict)
- Document in Obsidian
- Repeat with variations

### Mindset Shifts
- "Obey instructions" → "Solve problems autonomously"
- "Copy-paste" → "Hand-retype for understanding"
- "Theory first" → "Hands-on projects first"
- "One environment" → "Cross-platform"
- "Happy path" → "Error handling everywhere"

### Core Competencies Built
✅ Error handling + logging (4+ contexts)
✅ Pipeline operations (grep | cut | sort | uniq)
✅ Python-Linux integration
✅ Flask web apps (routes, JSON)
✅ Docker containerization
✅ Git workflow mastery
✅ Bash automation
✅ Linux permissions (basic + advanced)

---

## Next Steps (Jour 11+)
- [ ] Permissions test solo (refaire de mémoire)
- [ ] GitHub Actions CI/CD pipeline
- [ ] Raspberry Pi server setup (DevOps-only)
- [ ] Monitoring stack (Prometheus/Grafana intro)
- [ ] Specialization decision (DevOps/SRE/Admin)

---

## Personal Context
- Age: 39, ex-militaire (7 ans, opérateur nucléaire)
- Discipline: 20-25h/week learning, rotating schedule
- Motivation: Scientific contribution (space/oceanography/defense), family security
- Timeline: 18 months target, 24 months acceptable
- Mindset: Direct, no-bullshit, detail-oriented

---

**Status** : Portfolio public ✅ | En progression Jour 10/540