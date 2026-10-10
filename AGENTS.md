# Repository Instructions: Pramaan (Public Curriculum & Textbook)

## Mandatory Dual-Repository Lesson Synchronization Rule ("Pramaan Sync")

This repository is the public production deployment for the **Pramaan** learning platform (hosted on GitHub Pages at `https://ankit1057.github.io/pramaan/`).

### Dual-Repository Structure
1. **Public Production & Deployment Repository (Here):**
   - Path: `/Users/mobile/Desktop/pramaan`
   - Remote: `https://github.com/ankit1057/pramaan.git`
2. **Source & Analysis Workspace:**
   - Path: `/Users/mobile/Desktop/Ankit-AI-Behaviour-Analysis`
   - Remote: `https://github.com/ankit1057/Ankit-AI-Behaviour-Analysis.git`

---

### Mandatory Protocol (Definition of Done)
Whenever any lesson or chapter is modified:
1. Ensure the source files in `/Users/mobile/Desktop/Ankit-AI-Behaviour-Analysis/academy_v2` and `omni_academy` are updated.
2. Validate all modules: `academy_v2/.venv/bin/python academy_v2/tools/validate.py` (135/135 pass).
3. Rebuild the static HTML site: `academy_v2/.venv/bin/python academy_v2/tools/build.py`.
4. Keep `/Users/mobile/Desktop/pramaan` synchronized with the latest built HTML files and 50-chapter textbook.
5. Push changes to BOTH repositories using `env -u GITHUB_TOKEN git push origin main`.
6. Provide raw verification output ("Pramaan") proving the push succeeded.
