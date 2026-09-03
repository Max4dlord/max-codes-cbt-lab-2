# MTH 202 CBT Lab — Complete Guide

## Deployment, Preview, Long-Term Maintenance & Security

This guide covers everything you need to:
1. Preview the app right now
2. Deploy it free so other students can access it via a link
3. Maintain it long-term (add/edit/remove questions & features)
4. Keep it secure and backed up so you never lose your work

---

# PART 1 — How to Preview Right Now

## Option A: The Live Preview (already running)

The app is already running in this workspace as a live preview. You can click through it
right now — landing page, dashboard, take a test, see solutions. This is the fastest way
to see your work.

## Option B: Run it locally on your own computer

If you want to run it on your own laptop (offline, anytime):

### Step 1: Install Node.js
Download from **https://nodejs.org** (pick the "LTS" version).
This installs both Node and npm. Verify by opening a terminal (Command Prompt / Terminal)
and running:
```
node --version
npm --version
```
You should see version numbers (e.g. v20.x.x and 10.x.x).

### Step 2: Get the project files
You already have the project in this workspace. Download the entire `cbt-platform` folder
to your computer. (If you deploy via GitHub first, you can also `git clone` it — see Part 2.)

### Step 3: Install dependencies and run
Open a terminal in the `cbt-platform` folder and run:
```bash
npm install        # downloads required packages (first time only)
npm run dev        # starts the dev server
```
Then open **http://localhost:5173** in your browser. That is your live preview.

> Every time you save a file (e.g. edit `src/data.js`), the page auto-refreshes.
> This is the fastest way to see changes as you add questions.

### Step 4: Build the production version
When you are ready to deploy:
```bash
npm run build      # creates an optimized "dist/" folder
npm run preview    # previews the built version locally
```
The `dist/` folder is what you upload to a hosting provider.

---

# PART 2 — Free & Open-Source Deployment

Since this app is **100% static** (no backend, no database — all progress is saved in
the browser via localStorage), it can be hosted for FREE on any static hosting platform.
Students just need the link — no login, no setup on their end.

Below are the **four best free options**, ranked easiest to hardest.

---

## ⭐ Option 1: Vercel (RECOMMENDED — easiest, free)

Vercel is built by the same team behind the framework this app uses. It is the simplest
path from "code" to "live link."

### Prerequisites
- A **GitHub** account (free at https://github.com)
- Your project pushed to a GitHub repository (see "How to put your project on GitHub" below)

### Steps
1. Go to **https://vercel.com** and sign up (use "Continue with GitHub").
2. Click **"Add New Project"** → **"Import"** your GitHub repository.
3. Vercel auto-detects Vite. Just click **"Deploy."**
4. Wait ~30 seconds. You get a live link like:
   `https://mth202-cbt-lab.vercel.app`
5. **Done.** Share that link with students.

### Why Vercel is best here
- **Free forever** for personal projects (generous limits: 100GB bandwidth/month).
- **Automatic redeploy**: every time you push a change to GitHub, Vercel rebuilds and
  updates the live site within ~30 seconds. You edit `data.js`, push, and students see
  new questions automatically.
- **Custom domain**: free `*.vercel.app` subdomain, or connect your own domain free.
- **HTTPS** is automatic (secure padlock in browser).
- **No credit card required** for the free tier.

---

## Option 2: Netlify (also excellent, free)

Very similar to Vercel. Slightly different interface but equally free and reliable.

### Steps
1. Go to **https://netlify.com** and sign up (GitHub login).
2. Click **"Add new site"** → **"Import an existing project"**.
3. Connect your GitHub repo.
4. Build settings: Netlify auto-detects Vite. Build command = `npm run build`,
   publish directory = `dist`.
5. Click **"Deploy."** You get a link like:
   `https://mth202-cbt-lab.netlify.app`

### Netlify bonus features
- **Drag-and-drop deploy**: you can literally drag your `dist/` folder onto the Netlify
  dashboard to deploy without GitHub. Great for quick updates.
- **Form handling** (free) — if you later add a "contact us" form.
- **Free 100GB bandwidth/month**.

---

## Option 3: GitHub Pages (completely free, forever)

GitHub Pages hosts directly from your GitHub repository. No third-party account needed.

### Steps
1. Push your project to GitHub (see below).
2. Add a deploy workflow file (GitHub Actions does the build automatically).
3. In your repo: **Settings → Pages → Source: GitHub Actions**.
4. Every push to `main` triggers a build and deploys to:
   `https://yourusername.github.io/cbt-platform`

### Pros & cons
- ✅ Completely free, no bandwidth limits, no account elsewhere.
- ✅ Lives entirely in your GitHub repo (single source of truth).
- ⚠️ Slightly more setup (one workflow file).
- ⚠️ The site is public (your repo must be public on the free tier, or you need GitHub Pro
  for private-repo Pages).

A ready-made workflow file is included below in Part 3, section "GitHub Actions file."

---

## Option 4: Cloudflare Pages (free, fastest CDN)

Cloudflare has one of the fastest global content delivery networks.

### Steps
1. Go to **https://pages.cloudflare.com** and sign up.
2. **Create a project** → connect your GitHub repo.
3. Build command: `npm run build`. Output directory: `dist`.
4. Deploy. You get: `https://cbt-platform.pages.dev`

### Pros
- ✅ Free, unlimited bandwidth, unlimited requests.
- ✅ Fastest global CDN of all the options.
- ⚠️ Slightly more technical setup.

---

## How to put your project on GitHub (needed for Options 1-4)

GitHub is the central place where your code lives. All the hosting platforms above pull
from it. Here is how to get your code there:

### Step 1: Create a GitHub account
Go to **https://github.com** → Sign up (free).

### Step 2: Create a new repository
1. Click the **"+"** icon (top right) → **"New repository."**
2. Name it `mth202-cbt-lab` (or whatever you like).
3. Set it to **Public** (required for free GitHub Pages; fine for Vercel/Netlify either way).
4. **Do NOT** check "Add a README" or ".gitignore" (we already have files).
5. Click **"Create repository."**

### Step 3: Install Git on your computer
Download from **https://git-scm.com/downloads**. Verify:
```
git --version
```

### Step 4: Push your project to GitHub
Open a terminal in your `cbt-platform` folder and run:
```bash
git init
git add .
git commit -m "MTH 202 CBT Lab - initial version with 99 questions"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/mth202-cbt-lab.git
git push -u origin main
```
(Replace `YOURUSERNAME` with your actual GitHub username.)

GitHub will ask for your username and a **Personal Access Token** (not your password).
To create a token: GitHub → Settings → Developer settings → Personal access tokens →
Generate new token → check "repo" scope → copy the token → paste it as your password.

### Step 5: Your code is now on GitHub
From now on, whenever you make changes (add questions, edit files), you push them:
```bash
git add .
git commit -m "Added 20 new Linear Algebra questions"
git push
```
And Vercel/Netlify/Cloudflare will automatically rebuild and update the live site.

---

## Quick comparison — which should you pick?

| Feature | Vercel | Netlify | GitHub Pages | Cloudflare |
|---|---|---|---|---|
| Ease of setup | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Free bandwidth | 100GB/mo | 100GB/mo | Unlimited | Unlimited |
| Auto-deploy on push | ✅ | ✅ | ✅ (via Actions) | ✅ |
| Custom domain (free) | ✅ | ✅ | ✅ | ✅ |
| HTTPS automatic | ✅ | ✅ | ✅ | ✅ |
| No account beyond GitHub | ❌ | ❌ | ✅ | ❌ |
| Speed | Fast | Fast | Medium | Fastest |

**My recommendation: Vercel.** It is the easiest, auto-deploys on every push, and the
free tier is more than enough for a class of students. If you want zero third-party
accounts, use GitHub Pages.

---

# PART 3 — Long-Term Maintenance

This is how you keep the CBT running for years without losing your setup, with simple
editing and no risk of breaking things.

---

## 3.1 — Adding, Modifying & Removing Questions

All questions live in one file: **`src/data.js`**. You only ever touch this file for
content changes. The structure is:

```js
{
  id: 'cn_27',                          // unique ID (topic_prefix_number)
  topicId: 'complex-numbers',           // must match a topic in topicMeta
  question: 'Your question text here?',
  options: ['Option A', 'Option B', 'Option C', 'Option D'],  // 2-6 options
  correct: 2,                           // index of correct answer (0-based: A=0, B=1, C=2, D=3)
  short: 'One-line explanation of why the answer is correct.',
  solution: 'Full step-by-step worked solution shown in the side panel.'
}
```

### To ADD a question
Paste a new object into the `questionBank.mth202` array, inside the appropriate topic
section (or anywhere — order does not matter, since tests shuffle). Make sure:
- `id` is unique (e.g. `cn_27`, `la_35`, `va_22`).
- `topicId` matches a topic that exists in `topicMeta.mth202`.

### To MODIFY a question
Find it by its `id`, edit the text, save the file. Done.

### To REMOVE a question
Delete its entire object (from `{` to `}`). Make sure not to leave a dangling comma
that breaks the file. Example — removing one question from a list:
```js
// BEFORE:
{ id: 'cn_05', ... },
{ id: 'cn_06', ... },     // ← delete this whole block
{ id: 'cn_07', ... },

// AFTER (no leftover comma issues):
{ id: 'cn_05', ... },
{ id: 'cn_07', ... },
```

### To ADD a new topic
1. Add it to `topicMeta.mth202`:
   ```js
   { id: 'calculus-of-variations', name: 'Calculus of Variations' }
   ```
2. Tag questions with `topicId: 'calculus-of-variations'`.
3. The topic automatically appears on the dashboard with its question count.

### To ADD a new course (e.g. MTH 301)
1. Add a course object to the `courses` array (set `available: true`).
2. Add a `topicMeta.mth301` array with that course's topics.
3. Add a `questionBank.mth301` array with that course's questions.
4. The course appears in the course selector on the dashboard automatically.

### Editing workflow (safest approach)
1. Run `npm run dev` locally so you see changes live.
2. Edit `src/data.js`.
3. Save → the page auto-refreshes → verify your new question shows up.
4. Take a quick test to confirm the answer/solution is correct.
5. Commit and push (see section 3.4).

> **Pro tip**: If you accidentally break the file (syntax error), the dev server shows a
> red error overlay telling you exactly which line has the problem. Fix it and the page
> recovers automatically. You cannot permanently break anything — just undo your last
> edit and try again.

---

## 3.2 — Updating Features

The app is organized into clean, separate files so you can change one thing without
affecting others:

| File | What it controls |
|---|---|
| `src/data.js` | Questions, topics, courses (content) |
| `src/utils.js` | Shuffling, time formatting, test builder, Telegram link |
| `src/progress.js` | Save/resume logic (localStorage) |
| `src/styles.css` | All colors, spacing, layout (design) |
| `src/components/Landing.jsx` | The landing page text & layout |
| `src/components/Dashboard.jsx` | The test configuration screen |
| `src/components/TestRunner.jsx` | The test engine (timer, palette, submit) |
| `src/components/Results.jsx` | The results & review screen |
| `src/components/SolutionPanel.jsx` | The side panel with full solutions |
| `src/components/Navbar.jsx` | The top navigation bar |
| `src/components/Timer.jsx` | The countdown timer display |

### Common feature changes

**Change the app's colors:**
Edit the variables at the top of `src/styles.css`:
```css
:root {
  --primary: #6366f1;    /* main brand color — change this one line */
  --accent: #22d3ee;     /* secondary accent color */
  --bg: #0f1117;         /* page background */
}
```

**Change the course name or landing page text:**
Edit `src/components/Landing.jsx` and the `courses` array in `src/data.js`.

**Change the timer durations available:**
In `src/components/Dashboard.jsx`, edit the `DURATIONS` array:
```js
const DURATIONS = [10, 15, 20, 25, 30, 45, 60, 90]  // add/remove values
```

**Change the question counts available:**
In `src/components/Dashboard.jsx`, edit the `COUNTS` array:
```js
const COUNTS = [10, 20, 30, 40, 50, 'all']
```

**Enable the Telegram discussion button:**
In `src/utils.js`, set:
```js
export const TELEGRAM_URL = 'https://t.me/+YourMTH202Group'
```
A "Discuss in Telegram" button then appears inside the solution panel.

**Add a new page/route:**
Add a route in `src/App.jsx` and create a new component in `src/components/`.

---

## 3.3 — Backing Up (Never Lose Your Work)

### Method 1: GitHub (automatic backup — best)
Every `git push` saves a snapshot to GitHub. You can go back to ANY previous version at
any time. This is your primary backup.

To see history: `git log --oneline`
To restore an old version of a file: `git checkout <commit-hash> -- src/data.js`

### Method 2: Manual copies (simple backup)
Once a week (or after big updates), copy the entire `cbt-platform` folder to:
- A USB drive, OR
- Google Drive / Dropbox / OneDrive, OR
- A second folder on your computer

The most important file to back up is **`src/data.js`** — that is all your questions
and solutions. If you lose everything else, you can rebuild the app, but losing
`data.js` means losing all your typed questions.

### Method 3: Tagged releases (milestone backup)
When you reach a milestone (e.g. "all MTH 202 questions loaded"), tag it:
```bash
git tag v1.0-all-questions
git push origin v1.0-all-questions
```
This creates a permanent named checkpoint you can always return to.

---

## 3.4 — The Daily Editing Workflow (Version Control with Git)

This is the professional way to make changes without fear. Git lets you experiment freely
— if something breaks, you undo with one command.

### Before you start editing
```bash
git status              # see what is clean/dirty
```

### After making changes (add questions, edit features)
```bash
git add .                                         # stage all changes
git commit -m "Added 15 new Complex Numbers Qs"   # save a snapshot
git push                                          # upload to GitHub + auto-deploy
```

### If you broke something and want to undo
```bash
# Undo changes that you have NOT committed yet:
git checkout -- src/data.js          # restore data.js to last committed version

# Undo your most recent commit (but keep the changes in your files):
git reset HEAD~1

# Completely undo the last commit (discard the changes too — careful!):
git reset --hard HEAD~1
```

### Best practice: small, frequent commits
Instead of making 50 changes then committing, commit after every 5-10 questions. This way
if something goes wrong, you only lose a small amount. Each commit is a restore point.

### Best practice: use a branch for big experiments
```bash
git checkout -b experiment-new-feature     # create a safe branch
# ...make changes, test...
# If good:
git checkout main && git merge experiment-new-feature
# If bad:
git checkout main && git branch -D experiment-new-feature   # discard the branch
```

---

## 3.5 — Security (Preventing Hacks & Tampering)

Since this is a static site with no backend, the security picture is simpler than most
web apps. Here are the real risks and how to handle them:

### Risk 1: Someone edits your GitHub repo
**Prevention:**
- Use a **strong, unique password** for GitHub.
- Enable **Two-Factor Authentication (2FA)** on GitHub (Settings → Password and
  authentication → Enable 2FA via authenticator app). This is the single most important
  security step.
- Never share your GitHub password or Personal Access Token with anyone.
- If you add collaborators, give them "read" or "pull" access only, not "admin."

### Risk 2: Students cheat by looking at answers in the source code
Since this is a client-side app, a technically savvy student *could* open browser dev
tools (F12) and see the question bank with answers. This is a limitation of any
front-end-only quiz app.

**Mitigations:**
- For **practice tests** (which this is), this is acceptable — students are practising,
  not being graded. The value is in the timed, shuffled experience.
- If you later need **true exam security** (answers hidden server-side), you would need a
  backend (e.g. a small Node/Express or serverless API that serves questions one at a time
  and only returns the answer after submit). That is a Phase 2 upgrade — I can help you
  build it when you are ready.
- You can minify the build (`npm run build` already does this) so the code is harder to
  read, though not impossible.

### Risk 3: Malicious dependency packages
**Prevention:**
- Only run `npm install` with packages you trust. The current `package.json` uses only
  well-known, safe packages (React, Vite, React Router).
- Run `npm audit` periodically to check for known vulnerabilities:
  ```bash
  npm audit
  npm audit fix       # auto-fixes what it can
  ```
- Do not install random packages you find online without checking them.

### Risk 4: Someone claims your free domain
Free subdomains (like `mth202-cbt-lab.vercel.app`) are tied to your account, so nobody
can take them. If you want a permanent, professional URL, buy a custom domain
(~$10-15/year from Namecheap, Google Domains, or Cloudflare Registrar) and connect it.
Then your link becomes something like `https://mth202.university.edu` or
`https://mth202cbt.com`.

### Risk 5: Losing access to your hosting account
**Prevention:**
- Use 2FA on Vercel/Netlify/GitHub.
- Keep your GitHub account as the single source of truth — even if a hosting account has
  issues, your code is safe on GitHub and can be redeployed to any other platform in
  minutes.

### General security checklist (do these once, then forget)
- [ ] GitHub: strong password + 2FA enabled
- [ ] Hosting account (Vercel/Netlify): strong password + 2FA
- [ ] `npm audit` run once a month
- [ ] Back up `src/data.js` to cloud storage weekly
- [ ] Never commit secrets (passwords, API keys) to Git — this app has none, so you are fine

---

## 3.6 — GitHub Actions file (for GitHub Pages deployment)

If you choose GitHub Pages (Option 3), create this file at
`.github/workflows/deploy.yml` in your repo:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist
      - uses: actions/deploy-pages@v4
```

Also add this to `vite.config.js` (so asset paths work on GitHub Pages):
```js
export default defineConfig({
  base: '/cbt-platform/',   // your repo name with slashes
  plugins: [react()],
  // ...rest of config
})
```

Then: repo Settings → Pages → Source = "GitHub Actions". Every push to `main` auto-deploys.

---

# PART 4 — Summary Checklist

### To deploy today (30 minutes):
1. [ ] Create a GitHub account and push your project (Part 2, "How to put your project on GitHub")
2. [ ] Sign up at Vercel.com with GitHub
3. [ ] Import your repo → click Deploy
4. [ ] Copy your live link (e.g. `https://mth202-cbt-lab.vercel.app`)
5. [ ] Share the link with students

### To maintain long-term:
1. [ ] Edit `src/data.js` to add/modify questions
2. [ ] `git add . && git commit -m "description" && git push` to save + auto-deploy
3. [ ] Run `npm run dev` locally to preview before pushing
4. [ ] Enable 2FA on GitHub and Vercel
5. [ ] Back up `src/data.js` to cloud storage weekly

### To scale later:
1. [ ] Add more courses (MTH 301, MTH 304) in `src/data.js`
2. [ ] Add a backend for true exam security (Phase 2)
3. [ ] Buy a custom domain (~$10/year)
4. [ ] Add analytics to track popular topics

---

*This app is 100% yours — open source, no subscriptions, no vendor lock-in. You can
host it anywhere, move it anytime, and it will keep working.*
