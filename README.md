# Max-codes — CBT Lab

A clean, exam-realistic, **multi-course Computer-Based Testing platform**.
Built with **React + Vite**. Timed tests, study mode, shuffled banks,
pause/resume, auto-saved progress and full worked solutions — 100% static,
no backend needed, progress saved in the browser.

> 🎨 **Crimson & Ivory build (`max-codes-cbt-lab-2`)**
> This repository is a full feature-for-feature clone of the original
> `Max-codes` CBT Lab. **Only the colour palette and the typeface changed** —
> every screen, feature and question is identical.
> • Palette: crimson `#C1121F` on ivory `#FDF7EE`, with burnt-amber `#B45309`
> and decorative gold `#C9A227` accents.
> • Typeface: **Inter** (self-hosted variable woff2 in `public/fonts/`, so it
> still works offline — no Google Fonts request at runtime).
> To re-theme: edit the `:root` custom properties at the top of
> `src/styles.css` — nothing else needs to change.

---

## 📚 Courses & content

| Course | Status | Questions | Structure |
|---|---|---|---|
| AEE 202 — Agricultural Engineering | ✅ live | 308 | 3 main categories · 23 topics · 20 diagram questions |
| MTH 202 — Mathematical Methods | ✅ live | 149 | 8 topics |
| EEE 202 — Applied Electricity II | ✅ live | 134 | 9 topics · 66 worked calculations + 68 theory · LaTeX-rendered step-by-step solutions with distractor analysis |
| EEE 252 — Analog Electronics & Circuit Analysis | ✅ live | 75 | 6 topics · 58 solved calculations + 17 theory, all past questions solved step-by-step in LaTeX |
| MEE 206 — Mechanical Eng. Fundamentals | ⏳ soon | — | — |

### EEE 202 — built for a WRITTEN, calculation-heavy exam

EEE 202 is optimised differently from the other courses. Because the paper is
written (not CBT), every 🧮 **Calculation** question carries a full
**Step 1–4 worked solution** (identification → every substitution line →
interpretation → distractor analysis explaining exactly which mistake
produces each wrong option). All mathematics is written in **LaTeX**
($...$ inline, $$...$$ display) and rendered live by KaTeX — no programming
notation anywhere. Every 📖 **Theory** question (including multi-part
(a)(b)(c) stems) has a structured solution with an exam-trap summary. Each
topic carries **summaryNotes** (key abstractions, core mathematical relations,
common pitfalls) shown in Study Mode's topic-notes drawer.

### AEE 202 main categories

AEE questions are organised under **3 main categories** (defined in `categoryMeta`
in `src/data.js`), and each topic belongs to exactly one category:

1. **Questions formed from materials in Shared Drive** — 101 questions across
   12 consolidated topics (welding processes & defects, fasteners, metal
   working, heat treatment, cutting tools, drilling, bench work & fitting,
   machine operations, advanced manufacturing, hand tools, jigs & fixtures,
   workshop safety).
2. **Questions from Actual past questions** — 107 questions across 6 topics
   (Measurement, Precision & Tolerance; Marking Out & Benchwork; Hammers,
   Chisels, Files & Hacksaw; Drilling & Lathe Operations; Materials &
   Engineering Products; Joining, Welding & Workshop Safety). Sourced from the
   AGE 201 Workshop Practice past paper, lecture notes and the compulsory
   objective questions, with AI-authenticated answers and explanations.
3. **Questions formed from First Shared Slide** — 100 questions across 5 topics
   (Centre Lathe & Lathe Operations, Shapers & Planers, Drilling Machines,
   Milling Process, Grinding Process), each with a detailed slide-grounded
   explanation.

In the dashboard you can now start a test on a **whole course**, a **single main
category** or a **single topic**. Empty categories are shown as "Coming soon"
until their content is uploaded.

The question bank lives in **`src/data.js`** and includes diagram-based
questions (images in `public/images/`).

---

## ▶️ Run it

```bash
npm install      # first time only
npm run dev      # http://localhost:5173
```

Build for production: `npm run build` → deploys the `dist/` folder anywhere.

---

## ✨ Features

- **Landing page** with live course/topic overview.
- **Dashboard** to configure each test:
  - Choose **duration** (10–90 min) and **number of questions** (10–50 or all).
  - **Full test** (all topics, shuffled) **or topic-based test**.
  - Topics are **auto-classified from the question bank** — tag a question with a `topicId` and it appears here.
- **Test engine**: live countdown with **Pause / Resume**, shuffled order, question palette, flagging, **auto-saved progress** (reload/close/resume exactly where you stopped), auto-submit on time-out.
- **Study Mode**: same bank, no timer — the correct answer is pre-ticked and a "See Detailed Explanation" button shows a long, step-by-step breakdown. Topic deep-dives included.
- **Results & review**: score ring, breakdown (correct / wrong / skipped / time used), per-question verdict + one-line explanation, and a **side panel with full worked solutions** — no redirect, no progress lost.
- **Diagram support**: questions can carry an `image` (welding defects, flame zones, anvil, hacksaw TPI, jig vs fixture, taper pin…).
- **Multi-course ready** — add courses/topics/questions in one file.

---

## 🗂️ Add questions

Everything lives in **`src/data.js`**. Each question is one object:

```js
{
  id: 'aee_wd_01',                          // unique
  topicId: 'welding-processes-defects',     // must exist in topicMeta.aee202
  question: 'What is slag in welding and what is its primary cause?',
  options: ['A', 'B', 'C', 'D'],            // 2–6 options
  correct: 0,                               // index of the right option (0-based)
  short: 'One-line why it is right/wrong.',
  solution: 'Full step-by-step worked solution shown in the side panel.',
  image: '/images/optional-diagram.png'     // optional
}
```

**To add a topic:** add `{ id, name, categoryId }` to `topicMeta[<id>]` (use
`categoryId: 'shared-drive'`, `'past-questions'` or `'first-slides'` for AEE).
**To add a course:** add it to `courses`, plus `topicMeta[<id>]` and
`questionBank[<id>]` arrays.

> 💡 Tip: run the data validator before pushing —
> see `npm run validate` below.

---

## 🧱 Project structure

```
  index.html
  vite.config.js
  vercel.json            Vercel build config (framework: vite)
  src/
    main.jsx             app entry
    App.jsx              routes (HashRouter): / /dashboard /test /study /results
    styles.css           full design system
    data.js              ← courses, topics & question bank (single source of truth)
    utils.js             shuffle, time format, question-set builder
    progress.js          localStorage save/resume + results
    components/
      Navbar.jsx         brand + links + "Resume test" indicator
      Landing.jsx        hero, features, how-it-works, live topics
      Dashboard.jsx      configure + start/resume tests & study mode
      Timer.jsx          countdown + pause/resume
      TestRunner.jsx     test engine: timer, palette, save, submit
      StudyRunner.jsx    study mode: answers pre-ticked + deep explanations
      Results.jsx        score + review + show-full-explanation
      SolutionPanel.jsx  side panel with full worked solutions
```

---

## 🚀 Deploy on Vercel (auto-deploy from GitHub)

1. Push this repo to GitHub.
2. On [vercel.com](https://vercel.com) → **Add New Project → Import** the repo.
3. Vercel auto-detects Vite (`vercel.json` is already in the repo) → **Deploy**.
4. Every `git push` to `main` rebuilds and updates the live site automatically (~30 s).

> Full walkthrough, plus Netlify/GitHub Pages alternatives and
> maintenance & security tips: see **DEPLOYMENT-AND-MAINTENANCE-GUIDE.md**.

---

## 🔐 Access gate (join → unlock)

The app is normally locked behind a gate: visitors follow your WhatsApp
channel (and any other tasks you add) and enter an **access code** that you
post in the channel. Everything is configured in **`src/gateConfig.js`**:

- `enabled` — set to `false` to open the app to everyone instantly.
- `code` — the access code students must enter (currently `Maxprep3060`).
- `accessVersion` — bump this number whenever you change the code; every
  stored unlock becomes invalid and users must re-verify.
- `tasks` — the list of steps users must complete. Adding a task is just
  adding one object (examples are included in the file).

An unlock is saved in the visitor's browser and stays valid until you bump
`accessVersion` — no expiry by default.

> For a hard lock (e.g. during maintenance or exams), enable **Vercel
> Deployment Protection → Password Protection** in the Vercel dashboard.

---

## 🛣️ Possible next steps

- CSV/JSON bulk importer for past questions.
- Backend + accounts for cross-device progress sync (swap `progress.js` for an API).
- Access gate (join-group → unlock) in front of the app.
- Analytics (weak topics, average time per question).
