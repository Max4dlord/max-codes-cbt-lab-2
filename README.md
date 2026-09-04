![CI](https://github.com/Max4dlord/max-codes-cbt-lab-2/actions/workflows/ci.yml/badge.svg)
![Vercel](https://img.shields.io/badge/deploy-Vercel%20auto-black?logo=vercel)
![Theme](https://img.shields.io/badge/theme-OAU%20Navy%20%26%20Gold-%23010080)
![Font](https://img.shields.io/badge/font-Inter-0E1436)
![Course](https://img.shields.io/badge/course-EEE%20282%20%C2%B7%2030%20questions-%23C9A227)

# OAU · EEE 282 CBT Lab

A clean, exam-realistic **Computer-Based Testing platform for EEE 282 — Electronic
& Electrical Introductory Practicals II**, built for students of
**Obafemi Awolowo University, Ile-Ife**.

Built with **React + Vite**. Timed tests, study mode, shuffled banks, pause/resume,
auto-saved progress, full worked solutions — plus **typed answers** for the calculation
and short-answer questions, so it mirrors the written bench exam as well as a CBT.
100% static, no backend, progress saved in the browser.

---

## 🎨 Theme — OAU navy & gold

This build is a full feature-for-feature clone of the upstream `Max-codes` CBT Lab.
**Only the colour palette, the typeface and the course content changed** — every screen,
engine and feature is identical.

| Token | Value | Source |
|---|---|---|
| `--navy` | `#010080` | dominant colour of the official OAU crest |
| `--navy-2` | `#000066` | darker navy for hover / pressed states |
| `--navy-mid` | `#3E4095` | crest indigo — gradients |
| `--navy-deep` | `#26145E` | university wordmark |
| `--gold` | `#C9A227` | OAU gold |
| `--gold-2` | `#FECC43` | crest gold (bright accents) |
| `--bg` | `#F5F7FC` | cool ivory page |

Colours were extracted from the official crest and wordmark published on
**oauife.edu.ng**; the logo files ship with the app in `public/`.

- **Typeface:** Inter, self-hosted as a variable woff2 in `public/fonts/` — no Google
  Fonts request at runtime, so it still works offline.
- **Logo:** the OAU crest appears in the navbar, the landing hero, the access gate, the
  footer, the favicon and the Apple touch icon.
- To re-theme, edit the `:root` custom properties at the top of `src/styles.css` —
  nothing else needs to change.

---

## 📚 Course & content

| Course | Status | Questions | Structure |
|---|---|---|---|
| **EEE 282 — Electronic & Electrical Introductory Practicals II** | ✅ live | 30 | 4 topics · 12 diagrams · 17 MCQ + 7 calculations + 6 short answers |

| Topic | Questions | What it covers |
|---|---|---|
| Active & Passive Components | 8 | active vs passive rule, diode, zener, potentiometer divider, NTC, LDR, electrolytic vs ceramic |
| BJT Pin & Type Diagnostics | 10 | multimeter diode-mode identification of base / type / emitter / collector, fault signatures |
| CRO Controls & Functions | 5 | Time/Div, Volts/Div, trigger, position, AC/DC/GND coupling, graticule |
| CRO Waveform Calculations | 7 | Vp-p, Vp, Vrms, period, frequency, DC offset, phase shift, Lissajous |

The other banks from the upstream project (AEE 202, MTH 202, EEE 202, EEE 252, MEE 206)
are **not** part of this build — they remain untouched in the original `Max-codes`
repository. Only EEE 282 ships here.

---

## ✍️ Two ways to answer

Every question carries **four options**, so the app always behaves like a CBT. The
**calculation** and **short-answer** questions *also* show a **typed answer box** —
the way you would actually answer them in the exam.

- A non-empty typed answer **takes precedence** over the picked option.
- Picking an option clears the typed box, so the two never conflict.
- **Numeric grading** (`type: 'calc'`): every value in `num.values` must be matched by
  some number you typed, within `max(0.02, |value| × 2%)`. Order does not matter, so
  `20, 10, 7.07` and `Vrms 7.07 V, Vp-p 20 V, Vp 10 V` both score.
- **Keyword grading** (`type: 'text'`): `match.all` (every keyword), `match.any` (at least
  one) and `match.minAny` (at least *n* of a list).
- Results show exactly what you typed, the model answer, and why it was marked the way it was.

See `src/graders.js` for the whole grading engine.

---

## ▶️ Run it

```bash
npm install      # first time only
npm run dev      # http://localhost:5173
npm run validate # check the question bank
npm run build    # production build -> dist/
```

---

## ✨ Features

- **Landing page** with the OAU crest, university/department identity and a live topic overview.
- **Dashboard** to configure each test: duration (10–90 min), number of questions (10–50 or
  all), full course or single topic. Topics are auto-classified from the question bank.
- **Test engine**: live countdown with Pause / Resume, shuffled order, question palette,
  flagging, **auto-saved progress** (reload or close and resume exactly where you stopped),
  auto-submit on time-out.
- **Typed answers** on calculation / short-answer questions, graded as described above.
- **Study Mode**: same bank, no timer — the correct answer is pre-ticked, the model written
  answer is shown for typed questions, and “See Detailed Explanation” opens a long
  step-by-step breakdown plus a topic deep-dive.
- **Results & review**: score ring, breakdown (correct / wrong / skipped / time used),
  per-question verdict with a one-line explanation, and a **side panel with full worked
  solutions** — no redirect, no lost progress.
- **Diagrams**: **all 44 questions carry a figure** — hand-drawn SVG stored **inline** in
  `src/data.js` and rendered as live, zoomable SVG. Every one is specific to what the question
  asks (active vs passive panels, the two-diode BJT model, DMM probe setups, fault signatures…).
- **Full CRO everywhere**: all 12 CRO questions show the complete instrument — chassis,
  graticule screen, TIME/DIV, VOLTS/DIV, POSITION, TRIGGER, INTENSITY/FOCUS, CH1/CH2 BNC
  inputs and the DC-AC-GND coupling switch — with the control under discussion highlighted in
  OAU gold, and the relevant trace drawn on the screen.
- **Components reference**: a modal table of the 20 most-used active and passive components with
  their circuit symbols and uses, reachable from Study Mode and Review on any
  *Active & Passive Components* question.
- **LaTeX**: every formula is rendered live by KaTeX.

---

## 🖼️ Diagrams & the components table

### Question diagrams live in the data
Each question can carry a `diagram` — a raw, responsive SVG string in `src/data.js`
(replacing the old `image` path). `src/components/Diagram.jsx` injects it and scales it:

```js
{ id: '…', diagram: '<svg class="diagram-svg" viewBox="0 0 400 180">…</svg>',
  diagramCaption: 'PN junction diode: anode and cathode' }
```

Rules the build enforces (`npm run validate`):
- must start with `<svg`, carry a `viewBox`, and no fixed `width`/`height` (so it scales);
- **no `<style>` and no `<script>`** — the figure's internal classes (`.gl`, `.ax`, `.ac`, `.l`,
  `.w`…) are defined in `styles.css` **scoped under `.diagram-svg`**, so they can never leak
  into the rest of the app;
- marker/element ids are **namespaced per question** (`id="ah-eee282_q02"`), so several figures
  can share a page without id collisions.

### Component reference table
`componentSymbols` in `src/data.js` holds 20 entries — 10 passive, 10 active:

```js
{ name: 'Zener diode', category: 'Active', symbol: '<svg class="sym-svg" …>…</svg>',
  uses: 'Operates safely in reverse breakdown at a fixed voltage…' }
```

`src/components/ComponentsTableModal.jsx` renders it in a responsive overlay (search +
Active/Passive filters, sticky header, card layout under 720 px). It is opened by the
**“🔌 View Components Table”** button, which appears **only** on questions whose topic is
*Active & Passive Components*:

| View | Placement | Classes |
|---|---|---|
| Study Mode (`StudyRunner.jsx`) | in the same inline flex row as “See Detailed Explanation”, with `style={{ flex: 1, minWidth: 200 }}` | `.btn .btn-primary` |
| Review (`Results.jsx`) | inside `.ri-actions`, next to “Show full explanation” — the container's flex handles layout, no inline style | `.btn .btn-ghost .btn-sm` |

---

## 🔧 Regenerating the artwork
```bash
node scripts/draw_diagrams.mjs    # redraws all 44 figures into public/images/eee282/
python3 scripts/build_data.py     # inlines them into src/data.js (minified, safe, responsive)
npm run validate                  # checks the bank and every injected SVG
```
Both scripts live in the repo, so the figures are reproducible rather than hand-edited.

## 🚀 Deployment (Vercel)

The project deploys through **Vercel's GitHub integration**: connect the repo once and
**every push to `main` goes live automatically**. Branches and pull requests get their own
preview URLs.

One-time setup (from the Vercel dashboard):

1. **Add New… → Project → Import** `Max4dlord/max-codes-cbt-lab-2`
2. Leave the defaults — `vercel.json` supplies them:

   | Setting | Value |
   |---|---|
   | Framework | Vite |
   | Build Command | `npm run build` |
   | Output Directory | `dist` |
   | Install Command | `npm ci` |
   | Root Directory | `./` (repo root) |

3. **No environment variables** — the app is client-only, with no backend or secrets.
4. **Deploy**

Confirm it is live: **Settings → Git** should read *Connected to GitHub* with production
branch `main`.

Notes:

- `vercel.json` sets an `ignoreCommand`, so pushes that touch nothing under `src/`, `public/`,
  `package*.json`, `vite.config.js` or `index.html` deliberately **skip** the build.
- The app uses a `HashRouter`, so deep links (`/#/dashboard`) need no SPA rewrite rule.
- `.github/workflows/vercel-deploy-hook.yml` is a fallback for a project imported *without*
  the Git integration. It does nothing until a `VERCEL_DEPLOY_HOOK_URL` secret exists, and
  warns instead of passing silently.

## 🔤 Abbreviations

Two rules, enforced in `scripts/build_data.py`:

1. **CRO is always written out in full** — "cathode ray oscilloscope (CRO)" — at every
   place it appears, in questions, options, solutions, captions, topic notes and UI copy.
   Nobody should ever have to guess what "CRO" means.
2. **Every other abbreviation keeps its short form in the prose** (that is how it is
   written in the lab manual and printed on the instrument panel) but is listed in that
   question's **Key terms** drawer — a collapsed list of only the abbreviations that
   question actually uses. 30 of the 44 questions have one; the other 14 use none.
   A term the sentence already spells out in words is left out of the drawer.

To add a term, append it to `TERMS` in `scripts/build_data.py`. To make an abbreviation
behave like CRO (always spelled out), move it into `INLINE`.

## 🗂️ Add questions

Everything lives in **`src/data.js`**. Each question is one object:

```js
{
  id: 'eee282_q31',                 // unique
  topicId: 'cro-calculations',      // must exist in topicMeta.eee282
  kind: 'calc',                     // 'calc' | 'theory'
  type: 'calc',                     // 'mcq' | 'calc' | 'text'  (calc/text show a typed box)
  question: 'A sine wave spans 6 div at 2 V/div. Find Vp-p, Vp and Vrms.',
  options: ['12 V, 6 V, 4.24 V', '6 V, 12 V, 4.24 V', '12 V, 6 V, 8.49 V', '3 V, 6 V, 4.24 V'],
  correct: 0,                        // index of the right option (0-based)
  expected: 'Vp-p = 12 V, Vp = 6 V, Vrms = 4.24 V',   // model typed answer
  num: { values: [12, 6, 4.24], unit: 'V' },          // numeric grader (type: 'calc')
  // match: { all: ['wiper', '1', '3'], any: ['2'] }, // keyword grader (type: 'text')
  short: 'One-line why it is right.',
  solution: '### Steps\n- ...\n$$V_{rms}=0.707V_p$$',
  image: '/images/eee282/q24.svg'    // optional
}
```

> Run the validator before pushing: `npm run validate` (it checks ids, option ranges,
> topics, images, and the typed-answer contract).

---

## 🧱 Project structure

```
  index.html
  vite.config.js
  vercel.json            Vercel build config (framework: vite)
  src/
    main.jsx             app entry
    App.jsx              routes (HashRouter): / /dashboard /test /study /results
    styles.css           full design system — OAU navy & gold, Inter
    data.js              ← course, topics & question bank (single source of truth)
    graders.js           typed-answer grading (numeric + keyword)
    utils.js             shuffle, time format, question-set builder
    progress.js          localStorage save/resume + results
    gateConfig.js        access-gate settings
    components/
      Navbar.jsx         OAU crest + links + "Resume test" indicator
      Landing.jsx        OAU identity band, hero, features, how-it-works, live topics
      Dashboard.jsx      configure + start/resume tests & study mode
      Timer.jsx          countdown + pause/resume
      TestRunner.jsx     test engine: timer, palette, options, typed answers, save, submit
      StudyRunner.jsx    study mode: answers pre-ticked, model answers, deep explanations
      Results.jsx        score + review + show-full-explanation
      SolutionPanel.jsx  side panel with full worked solutions
      Diagram.jsx        renders a raw, responsive inline SVG (tap to zoom)
      ComponentsTableModal.jsx  active/passive components reference overlay
  public/
    oau-crest.png        official OAU crest (from oauife.edu.ng)
    oau-wordmark.png     crest + wordmark lockup
    oau-favicon-180.png  apple-touch-icon
    favicon.svg          navy/gold OAU mark
    fonts/               Inter variable woff2 (self-hosted)
    images/eee282/       30 question diagrams (SVG) — one per question
```

---

## 🚀 Deploy on Vercel (auto-deploy from GitHub)

This repo is **pre-wired for zero-click deploys**. One-time setup:

1. Open **https://vercel.com/new/import?repository-url=https://github.com/Max4dlord/max-codes-cbt-lab-2**
   (or: Add New Project → Import → pick `max-codes-cbt-lab-2`).
2. Leave every setting on the default — `vercel.json` already declares framework `vite`,
   `npm ci`, `npm run build`, output `dist`, SPA rewrites and cache headers. Press **Deploy**.
3. Done. **Every `git push` to `main` rebuilds and updates the live site automatically
   (~30–60 s)**, and every push/PR also gets a build status here.

| File | What it does |
|---|---|
| `.github/workflows/ci.yml` | Runs `npm run validate` + `npm run build` on every push/PR, so a broken bank goes red **before** Vercel ships it. |
| `vercel.json → ignoreCommand` | Skips the deploy when a push only touched docs. |
| `vercel.json → installCommand: npm ci` | Reproducible installs from `package-lock.json`. |
| `.nvmrc` + `engines` | Pins Node 20 for GitHub Actions and Vercel. |
| `.github/workflows/vercel-deploy-hook.yml` | Optional fallback if the project is imported without Vercel's Git integration — add a `VERCEL_DEPLOY_HOOK_URL` secret. |

> Full walkthrough, plus Netlify/GitHub Pages alternatives and maintenance & security
> tips: see **DEPLOYMENT-AND-MAINTENANCE-GUIDE.md**.

---

## 🔐 Access gate (join → unlock)

The app can be locked behind a gate: visitors follow your WhatsApp channel and enter an
**access code** that you post there. Configured in **`src/gateConfig.js`**:

- `enabled` — set to `false` to open the app to everyone instantly.
- `code` — the access code students enter.
- `accessVersion` — bump this number whenever you change the code; every stored unlock
  becomes invalid and users must re-verify.

---

## 🛣️ Possible next steps

- Grow the EEE 282 bank (the source set has room for more topics).
- CSV/JSON bulk importer for past questions.
- Backend + accounts for cross-device progress sync.
- Analytics (weak topics, average time per question).
