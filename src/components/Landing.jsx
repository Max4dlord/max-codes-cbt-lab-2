import { Link } from 'react-router-dom'
import { courses } from '../data.js'
import { getTopics, getCategories, getQuestionCount } from '../utils.js'

const UNIVERSITY = 'Obafemi Awolowo University'
const CAMPUS = 'Ile-Ife, Osun State · Faculty of Technology'

const FEATURES = [
  { ico: '⏱️', title: 'Timed tests, your way', text: 'Pick a duration and how many questions you want. A live countdown with Pause / Resume keeps you in control.' },
  { ico: '🎯', title: 'Topic-based practice', text: 'Drill a single topic — say, Welding Defects for 25 minutes — or mix the whole syllabus.' },
  { ico: '🔀', title: 'Shuffled question bank', text: 'Every test re-shuffles question order and options from the bank, so no two practice runs feel the same.' },
  { ico: '💾', title: 'Progress auto-saved', text: 'Reload, switch tabs, come back tomorrow — your test resumes exactly where you stopped, timer and all.' },
  { ico: '✅', title: 'Instant verdicts', text: 'After submitting, each question shows right/wrong with a one-line explanation, then a tap for the full solution.' },
  { ico: '📖', title: 'Full worked solutions', text: '“Show full explanation” opens a side panel with complete, step-by-step working — without leaving your results.' }
]

const STEPS = [
  { title: 'Choose your test', text: 'On the dashboard, pick the course, a duration, and the number of questions — or zero in on one topic.' },
  { title: 'Sit the test', text: 'Answer MCQs with a running timer. Pause anytime; your answers and remaining time save automatically.' },
  { title: 'Submit & review', text: 'Get your score instantly. Every question shows a short right/wrong explanation.' },
  { title: 'See full solutions', text: 'Tap “Show full explanation” for a comprehensive, step-by-step worked solution in a side panel.' }
]

export default function Landing() {
  // The landing page is COURSE-NEUTRAL by design. Nothing here is driven by a
  // single "selected" course any more, because that made whichever course came
  // first in data.js dominate the whole page. Every live course is rendered in
  // its own equally sized card and syllabus block.
  const availableCourses = courses.filter((c) => c.available)
  const totalQuestions = availableCourses.reduce((n, c) => n + getQuestionCount(c.id), 0)
  function scrollToFeatures() {
    document.getElementById('features')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <>
      <section className="hero">
        <div className="oau-band">
          <img src="/oau-crest.png" alt="Obafemi Awolowo University crest" className="oau-crest" />
          <div>
            <div className="oau-uni">{UNIVERSITY}</div>
            <div className="oau-place">{CAMPUS}</div>
          </div>
        </div>

        <span className="badge"><span className="dot" /> OAU CBT Practice Platform · Live</span>
        <h1>
          Practise for your <span className="grad">OAU</span> papers, one course at a time
        </h1>
        <p className="lead">
          A clean, exam-realistic testing environment. Choose a course below, set your
          duration, and start — with a live timer, auto-saved progress and a full worked
          solution behind every question.
        </p>

        <div className="hero-cta">
          <Link to="/dashboard" className="btn btn-primary btn-lg">Start a test →</Link>
          <button type="button" onClick={scrollToFeatures} className="btn btn-ghost btn-lg">Explore features</button>
        </div>
        <p className="hero-note">No sign-up needed · works offline · your progress is saved on this device</p>

        <div className="hero-card">
          <div className="stat"><div className="num grad">{availableCourses.length}</div><div className="lbl">Courses available</div></div>
          <div className="stat"><div className="num">{totalQuestions}</div><div className="lbl">Questions in total</div></div>
          <div className="stat"><div className="num grad">100%</div><div className="lbl">Free to practice</div></div>
          <div className="stat"><div className="num">∞</div><div className="lbl">Reshuffles per test</div></div>
        </div>
      </section>

      {/* ---------- COURSE PICKER: every course gets equal, distinct space ---------- */}
      <section className="section" id="courses">
        <div className="section-head">
          <h2>Choose your course</h2>
          <p>Each course has its own question bank, topics and worked solutions.</p>
        </div>
        <div className="course-cards">
          {availableCourses.map((c) => {
            const cats = getCategories(c.id).filter((x) => !x.spansAll)
            const tps = getTopics(c.id)
            return (
              <article className="course-card" key={c.id} style={{ '--accent': c.accent }}>
                <div className="course-card-top">
                  <span className="course-card-code">{c.code}</span>
                  <span className="course-card-count">{getQuestionCount(c.id)} questions</span>
                </div>
                <h3 className="course-card-title">{c.title}</h3>
                {c.department && <p className="course-card-dept">{c.department}</p>}
                <p className="course-card-blurb">{c.blurb}</p>

                <div className="course-card-meta">
                  <span>{tps.length} topic{tps.length === 1 ? '' : 's'}</span>
                  {cats.length > 0 && <span>{cats.length + 1} categories</span>}
                </div>

                <div className="course-card-topics">
                  {tps.slice(0, 5).map((t) => (
                    <span className="mini-chip" key={t.id}>{t.name}</span>
                  ))}
                  {tps.length > 5 && <span className="mini-chip more">+{tps.length - 5} more</span>}
                </div>

                <div className="course-card-actions">
                  <Link to="/dashboard" className="btn btn-primary">Take a test →</Link>
                  <Link to="/dashboard" className="btn btn-ghost">Study mode</Link>
                </div>
              </article>
            )
          })}
        </div>
      </section>

      <section className="section" id="features">
        <div className="section-head">
          <h2>Everything a serious student needs</h2>
          <p>Built around how CBT exams actually feel — timing, focus, and instant feedback.</p>
        </div>
        <div className="features">
          {FEATURES.map((f) => (
            <div className="feature" key={f.title}>
              <div className="ico">{f.ico}</div>
              <h3>{f.title}</h3>
              <p>{f.text}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>How it works</h2>
          <p>From choosing a test to reading the full solution — four simple steps.</p>
        </div>
        <div className="steps">
          {STEPS.map((s) => (
            <div className="step" key={s.title}>
              <h3>{s.title}</h3>
              <p>{s.text}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section" id="syllabus">
        <div className="section-head">
          <h2>What each course covers</h2>
          <p>Every topic below is a bank you can drill on its own.</p>
        </div>

        {availableCourses.map((c) => {
          const cats = getCategories(c.id).filter((x) => !x.spansAll)
          return (
            <div className="syllabus-block" key={c.id} style={{ '--accent': c.accent }}>
              <div className="syllabus-head">
                <span className="syllabus-code">{c.code}</span>
                <span className="syllabus-name">{c.title}</span>
                <span className="syllabus-count">{getQuestionCount(c.id)} Qs</span>
              </div>

              {cats.length > 0 ? (
                cats.map((cat) => (
                  <div key={cat.id} className="topic-group">
                    <div className="topic-group-head">
                      {cat.name}
                      <span className="cat-badge">{cat.count === 0 ? 'Coming soon' : `${cat.count} Qs`}</span>
                    </div>
                    {cat.topics.length > 0 ? (
                      <div className="topic-grid">
                        {cat.topics.map((t) => (
                          <Link to="/dashboard" className="topic-chip" key={t.id} style={{ textDecoration: 'none' }}>
                            <div className="t-name">{t.name}</div>
                            <div className="t-count">{t.count}</div>
                          </Link>
                        ))}
                      </div>
                    ) : (
                      <p className="muted" style={{ fontSize: 14 }}>Content coming soon — check back later.</p>
                    )}
                  </div>
                ))
              ) : (
                <div className="topic-grid">
                  {getTopics(c.id).map((t) => (
                    <Link to="/dashboard" className="topic-chip" key={t.id} style={{ textDecoration: 'none' }}>
                      <div className="t-name">{t.name}</div>
                      <div className="t-count">{t.count}</div>
                    </Link>
                  ))}
                </div>
              )}
            </div>
          )
        })}
      </section>

      <div className="cta-band">
        <h2>Ready to test yourself?</h2>
        <p>Pick a duration, choose your topics, and start practising the smart way.</p>
        <Link to="/dashboard" className="btn btn-primary btn-lg">Go to dashboard →</Link>
      </div>

      <footer>
        <img src="/oau-crest.png" alt="OAU crest" className="oau-footer-crest" />
        <div>
          © {new Date().getFullYear()} {UNIVERSITY}, {CAMPUS.split(' · ')[0]} — CBT Lab.
          <br />
          Built for focused, exam-realistic practice. “For Learning and Culture.”
        </div>
      </footer>
    </>
  )
}
