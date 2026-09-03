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
- **Diagrams**: 12 hand-drawn SVG figures (diode, potentiometer divider, thermistor, LDR,
  capacitor types, zener, DMM probing a TO-92 BJT, CRO traces, Lissajous).
- **LaTeX**: every formula is rendered live by KaTeX.

---

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
  public/
    oau-crest.png        official OAU crest (from oauife.edu.ng)
    oau-wordmark.png     crest + wordmark lockup
    oau-favicon-180.png  apple-touch-icon
    favicon.svg          navy/gold OAU mark
    fonts/               Inter variable woff2 (self-hosted)
    images/eee282/       12 question diagrams (SVG)
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
