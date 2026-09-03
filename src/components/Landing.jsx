import { Link } from 'react-router-dom'
import { courses } from '../data.js'
import { getTopics, getCategories } from '../utils.js'

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
  const availableCourses = courses.filter((c) => c.available)
  const course = availableCourses[0] || courses[0]
  const topics = getTopics(course.id)
  function scrollToFeatures() {
    document.getElementById('features')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <>
      <section className="hero">
        <span className="badge"><span className="dot" /> CBT Practice Platform · Live</span>
        <h1>
          Master your exams with <span className="grad">Max-codes CBT Lab</span>
        </h1>
        <p className="lead">
          A clean, exam-realistic testing environment for past questions. Configure your test,
          shuffle the question bank, pause when you need to, and review every answer with
          full worked solutions.
        </p>
        <div className="hero-cta">
          <Link to="/dashboard" className="btn btn-primary btn-lg">Start a test →</Link>
          <button type="button" onClick={scrollToFeatures} className="btn btn-ghost btn-lg">Explore features</button>
        </div>
        <p className="hero-note">No sign-up needed · works offline · your progress is saved on this device</p>

        <div className="hero-card">
          <div className="stat"><div className="num grad">{availableCourses.length}</div><div className="lbl">Courses live now</div></div>
          <div className="stat"><div className="num">{getTopics(course.id).length}</div><div className="lbl">Topic categories</div></div>
          <div className="stat"><div className="num grad">100%</div><div className="lbl">Free to practice</div></div>
          <div className="stat"><div className="num">∞</div><div className="lbl">Reshuffles per test</div></div>
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

      <section className="section">
        <div className="section-head">
          <h2>Topics covered in {course.code}</h2>
          <p>Comprehensive coverage across all core areas you need to master.</p>
        </div>
        {getCategories(course.id).length > 0 ? (
          <div>
            {getCategories(course.id).map((c) => (
              <div key={c.id} className="topic-group">
                <div className="topic-group-head">
                  {c.name}
                  <span className="cat-badge">{c.count === 0 ? 'Coming soon' : `${c.count} Qs`}</span>
                </div>
                {c.topics.length > 0 ? (
                  <div className="topic-grid">
                    {c.topics.map((t) => (
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
            ))}
          </div>
        ) : (
          <div className="topic-grid">
            {topics.map((t) => (
              <Link to="/dashboard" className="topic-chip" key={t.id} style={{ textDecoration: 'none' }}>
                <div className="t-name">{t.name}</div>
              </Link>
            ))}
          </div>
        )}
      </section>

      <div className="cta-band">
        <h2>Ready to test yourself?</h2>
        <p>Pick a duration, choose your topics, and start practising the smart way.</p>
        <Link to="/dashboard" className="btn btn-primary btn-lg">Go to dashboard →</Link>
      </div>

      <footer>
        © 2026 Max-codes CBT Lab — Built for focused, exam-realistic practice.
      </footer>
    </>
  )
}
