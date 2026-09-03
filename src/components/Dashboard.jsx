import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { courses } from '../data.js'
import { getTopics, getCategories, getQuestionCount, buildQuestionSet } from '../utils.js'
import { loadSession, clearSession, saveSession } from '../progress.js'
import { saveStudySession } from '../progress.js'

const DURATIONS = [10, 15, 20, 25, 30, 45, 60, 90]
const COUNTS = [10, 20, 30, 40, 50, 'all']

export default function Dashboard() {
  const navigate = useNavigate()
  const existing = loadSession()

  const [courseId, setCourseId] = useState(courses.find((c) => c.available)?.id || courses[0].id)
  const [mode, setMode] = useState('full') // 'full' | 'category' | 'topic'
  const [categoryId, setCategoryId] = useState(null)
  const [topicId, setTopicId] = useState(null)
  const [duration, setDuration] = useState(25)
  const [count, setCount] = useState(20)
  const [error, setError] = useState('')

  // --- Study Mode state ---
  const [studyCourseId, setStudyCourseId] = useState(courses.find((c) => c.available)?.id || courses[0].id)
  const [studyMode, setStudyMode] = useState('full')
  const [studyCategoryId, setStudyCategoryId] = useState(null)
  const [studyTopicId, setStudyTopicId] = useState(null)
  const [studyCount, setStudyCount] = useState(20)
  const [studyError, setStudyError] = useState('')

  const course = courses.find((c) => c.id === courseId)
  const topics = getTopics(courseId)
  const categories = getCategories(courseId)
  const hasCats = categories.length > 0
  const selectedTopic = topics.find((t) => t.id === topicId)
  const selectedCategory = categories.find((c) => c.id === categoryId)

  const poolSize =
    mode === 'topic' && topicId
      ? getQuestionCount(courseId, topicId)
      : mode === 'category' && categoryId
      ? selectedCategory?.count ?? 0
      : getQuestionCount(courseId)

  function startTest() {
    setError('')
    if (!course.available) {
      setError('This course is coming soon. Please check back later or choose an available course.')
      return
    }
    if (mode === 'category' && !categoryId) {
      setError('Please pick a main category to start a category-based test.')
      return
    }
    if (mode === 'topic' && !topicId) {
      setError('Please pick a topic to start a topic-based test.')
      return
    }
    if ((mode === 'category' && !categoryId) || (mode === 'topic' && !topicId)) {
      setError('Please pick a selection to start.')
      return
    }
    const set = buildQuestionSet(courseId, {
      mode,
      topicId: mode === 'topic' ? topicId : null,
      categoryId: mode === 'category' ? categoryId : null,
      count
    })
    if (set.length === 0) {
      setError('No questions available for this selection. Please try another topic.')
      return
    }

    const session = {
      v: 1,
      courseId,
      courseCode: course.code,
      courseTitle: course.title,
      topicId: mode === 'topic' ? topicId : null,
      categoryId: mode === 'category' ? categoryId : null,
      topicName:
        mode === 'topic' ? selectedTopic?.name : mode === 'category' ? selectedCategory?.name : null,
      mode,
      durationSec: duration * 60,
      remainingSec: duration * 60,
      index: 0,
      answers: {},
      flagged: [],
      paused: false,
      questionSet: set,
      startedAt: Date.now()
    }
    saveSession(session)
    navigate('/test')
  }

  function startStudy() {
    setStudyError('')
    const sc = courses.find((c) => c.id === studyCourseId)
    if (!sc.available) {
      setStudyError('This course is coming soon. Please check back later.')
      return
    }
    if (studyMode === 'category' && !studyCategoryId) {
      setStudyError('Please pick a main category for study mode.')
      return
    }
    if (studyMode === 'topic' && !studyTopicId) {
      setStudyError('Please pick a topic for study mode.')
      return
    }
    const set = buildQuestionSet(studyCourseId, {
      mode: studyMode,
      topicId: studyMode === 'topic' ? studyTopicId : null,
      categoryId: studyMode === 'category' ? studyCategoryId : null,
      count: studyCount
    })
    if (set.length === 0) {
      setStudyError('No questions available for this selection.')
      return
    }
    const topicsStudy = getTopics(studyCourseId)
    const catsStudy = getCategories(studyCourseId)
    const selTopic = topicsStudy.find((t) => t.id === studyTopicId)
    const selCat = catsStudy.find((c) => c.id === studyCategoryId)
    const studySession = {
      v: 1,
      courseId: studyCourseId,
      courseCode: sc.code,
      courseTitle: sc.title,
      topicId: studyMode === 'topic' ? studyTopicId : null,
      categoryId: studyMode === 'category' ? studyCategoryId : null,
      topicName:
        studyMode === 'topic' ? selTopic?.name : studyMode === 'category' ? selCat?.name : null,
      mode: studyMode,
      index: 0,
      questionSet: set,
      startedAt: Date.now()
    }
    saveStudySession(studySession)
    navigate('/study')
  }

  function resumeExisting() {
    if (existing) navigate('/test')
  }
  function discardExisting() {
    clearSession()
    window.location.reload()
  }

  const testCats = categories
  const studyCats = getCategories(studyCourseId)
  const studyHasCats = studyCats.length > 0

  return (
    <div className="page">
      <div className="page-head">
        <h1>Test Dashboard</h1>
        <p>Configure your CBT practice session — choose a duration, the number of questions, and whether to test a whole course, one main category or a single topic.</p>
      </div>

      {existing && (
        <div className="resume-banner">
          <div className="r-info">
            <span className="r-ico">⏸️</span>
            <div>
              <div className="r-title">You have a test in progress</div>
              <div className="r-sub">
                {existing.courseCode}{existing.topicName ? ` · ${existing.topicName}` : ' · Full course'} ·
                {' '}{existing.questionSet.length} questions · {existing.index + 1} answered ·
                {' '}{Math.floor(existing.remainingSec / 60)} min left{existing.paused ? ' · paused' : ''}
              </div>
            </div>
          </div>
          <div className="flex gap-8">
            <button className="btn btn-primary btn-sm" onClick={resumeExisting}>Resume →</button>
            <button className="btn btn-danger btn-sm" onClick={discardExisting}>Discard</button>
          </div>
        </div>
      )}

      <div className="grid-2">
        {/* ---- Configuration ---- */}
        <div className="card">
          <h2>1 · Configure your test</h2>

          <div className="field">
            <label>Course</label>
            {courses.length > 1 ? (
              <div className="course-select-wrap">
                <select value={courseId} onChange={(e) => { setCourseId(e.target.value); setCategoryId(null); setTopicId(null); setMode('full') }}>
                  {courses.map((c) => (
                    <option key={c.id} value={c.id}>{c.code} — {c.title}{c.available ? '' : ' (soon)'}</option>
                  ))}
                </select>
                <div className="course-pill">
                  <span className="course-dot" style={{ background: course.accent }} />
                  <span className="muted" style={{ fontSize: 13 }}>{course.available ? 'Available' : 'Coming soon'}</span>
                </div>
              </div>
            ) : (
              <div className="course-pill" style={{ padding: '10px 14px', border: '1px solid var(--border)', borderRadius: 10 }}>
                <span className="course-dot" style={{ background: course.accent }} />
                <strong style={{ fontSize: 15 }}>{course.code} — {course.title}</strong>
                <span className="muted" style={{ fontSize: 12, marginLeft: 'auto' }}>
                  {getQuestionCount(course.id)} questions
                </span>
              </div>
            )}
            <p className="info-line">{course.blurb}</p>
          </div>

          <div className="field">
            <label>Test mode</label>
            <div className="tabs">
              <button className={`tab ${mode === 'full' ? 'active' : ''}`} onClick={() => setMode('full')}>Full test (all topics)</button>
              {hasCats && (
                <button className={`tab ${mode === 'category' ? 'active' : ''}`} onClick={() => setMode('category')}>By main category</button>
              )}
              <button className={`tab ${mode === 'topic' ? 'active' : ''}`} onClick={() => setMode('topic')}>Topic-based test</button>
            </div>
          </div>

          {mode === 'category' && hasCats && (
            <div className="field">
              <label>Pick a main category</label>
              <div className="cat-grid">
                {testCats.map((c) => (
                  <button
                    key={c.id}
                    className={`cat-chip ${categoryId === c.id ? 'selected' : ''} ${c.count === 0 ? 'empty' : ''}`}
                    disabled={c.count === 0}
                    onClick={() => setCategoryId(c.id)}
                  >
                    <div className="cat-name">{c.name}</div>
                    <div className="cat-count">{c.count === 0 ? 'Coming soon' : `${c.count} questions · ${c.topics.length} topics`}</div>
                  </button>
                ))}
              </div>
            </div>
          )}

          {mode === 'topic' && (
            <div className="field">
              <label>Pick a topic</label>
              {hasCats ? (
                <div>
                  {categories.map((c) => (
                    <div key={c.id} className="topic-group">
                      {c.topics.length > 0 && (
                        <div className="topic-group-head">{c.name}</div>
                      )}
                      <div className="topic-grid">
                        {c.topics.map((t) => (
                          <button
                            key={t.id}
                            className={`topic-chip ${topicId === t.id ? 'selected' : ''}`}
                            onClick={() => setTopicId(t.id)}
                          >
                            <div className="t-name">{t.name}</div>
                            <div className="t-count">{t.count}</div>
                          </button>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="topic-grid">
                  {topics.map((t) => (
                    <button
                      key={t.id}
                      className={`topic-chip ${topicId === t.id ? 'selected' : ''}`}
                      onClick={() => setTopicId(t.id)}
                    >
                      <div className="t-name">{t.name}</div>
                    </button>
                  ))}
                </div>
              )}
            </div>
          )}

          <div className="row">
            <div className="field">
              <label>Duration (minutes)</label>
              <select value={duration} onChange={(e) => setDuration(Number(e.target.value))}>
                {DURATIONS.map((d) => <option key={d} value={d}>{d} min</option>)}
              </select>
            </div>
            <div className="field">
              <label>Number of questions</label>
              <select value={count} onChange={(e) => {
                const v = e.target.value
                setCount(v === 'all' ? 'all' : Number(v))
              }}>
                {COUNTS.map((c) => <option key={String(c)} value={c}>{c === 'all' ? 'All available' : `${c} questions`}</option>)}
              </select>
            </div>
          </div>

          <p className="info-line">
            {mode === 'topic' && topicId
              ? <>Pool for <strong>{selectedTopic?.name}</strong>: <strong>{poolSize}</strong> question(s) available.</>
              : mode === 'category' && categoryId
              ? <>Pool for <strong>{selectedCategory?.name}</strong>: <strong>{poolSize}</strong> question(s) available.</>
              : <>Full course pool: <strong>{poolSize}</strong> question(s) available.</>}
            {' '}Questions will be shuffled on start.
          </p>

          {error && <p style={{ color: 'var(--red)', fontSize: 14, marginTop: 12 }}>{error}</p>}

          <div style={{ marginTop: 20 }}>
            <button className="btn btn-primary btn-lg" onClick={startTest} style={{ width: '100%' }}>
              Start {mode === 'topic' ? 'topic' : mode === 'category' ? 'category' : 'full'} test →
            </button>
          </div>
          <p className="hint">
            Tip: your test auto-saves as you go. Close the tab or refresh and you'll resume exactly where you stopped.
          </p>
        </div>

        {/* ---- Summary / scaling ---- */}
        <div className="card">
          <h2>Overview</h2>
          <p className="muted" style={{ fontSize: 14 }}>
            {course.code} currently has <strong style={{ color: 'var(--text)' }}>{getQuestionCount(courseId)}</strong> total questions
            across <strong style={{ color: 'var(--text)' }}>{topics.length}</strong> topics{hasCats ? (
              <> in <strong style={{ color: 'var(--text)' }}>{categories.length}</strong> main categories</>
            ) : ''}.
          </p>

          {hasCats ? (
            categories.map((c) => (
              <div key={c.id} style={{ marginTop: 16 }}>
                <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 6 }}>
                  {c.name}
                  <span className="cat-badge">{c.count === 0 ? 'Coming soon' : `${c.count} Qs`}</span>
                </div>
                <div className="topic-grid" style={{ marginTop: 4 }}>
                  {c.topics.length > 0 ? c.topics.map((t) => (
                    <div key={t.id} style={{ padding: 10, borderRadius: 10, background: 'var(--bg-soft)', border: '1px solid var(--border)', fontSize: 13 }}>
                      <span style={{ fontWeight: 600 }}>{t.name}</span>{' '}
                      <span className="muted" style={{ fontSize: 12 }}>· {t.count}</span>
                    </div>
                  )) : (
                    <p className="muted" style={{ fontSize: 13, margin: 0 }}>
                      No questions yet — content will be added soon.
                    </p>
                  )}
                </div>
              </div>
            ))
          ) : (
            <div className="topic-grid" style={{ marginTop: 8 }}>
              {topics.map((t) => (
                <div key={t.id} style={{ padding: 14, borderRadius: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)' }}>
                  <div style={{ fontWeight: 700, fontSize: 14 }}>{t.name}</div>
                </div>
              ))}
            </div>
          )}

          <Link to="/" className="btn btn-ghost btn-sm" style={{ marginTop: 24 }}>← Back to home</Link>
        </div>
      </div>

      {/* -------- STUDY MODE — No timer, immediate explanation, correct pre-ticked, very long explanations -------- */}
      <div className="card" style={{ marginTop: 24, borderLeft: '4px solid var(--primary)', background: 'linear-gradient(135deg, rgba(1,0,128,0.04), rgba(138,106,18,0.02))' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 12, marginBottom: 8 }}>
          <div>
            <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: 10 }}>📖 Study Mode <span style={{ fontSize: 12, background: 'var(--primary)', color: '#fff', padding: '4px 10px', borderRadius: 999 }}>NEW</span></h2>
            <p className="muted" style={{ fontSize: 14, marginTop: 6, maxWidth: 720 }}>
              The same questions as Test Mode, but <strong>no timer</strong>, <strong>correct answer already ticked in green</strong>, and an immediate <strong>“See Detailed Explanation →”</strong> button. Explanations here are <strong>much longer</strong> than in Test Mode — with extra deep dives, common mistakes, and how to approach similar questions.
            </p>
          </div>
        </div>

        <div className="field">
          <label>Course for Study Mode</label>
          <div className="course-select-wrap">
            <select value={studyCourseId} onChange={(e) => { setStudyCourseId(e.target.value); setStudyCategoryId(null); setStudyTopicId(null); setStudyMode('full') }}>
              {courses.map((c) => (
                <option key={c.id} value={c.id}>{c.code} — {c.title}{c.available ? '' : ' (soon)'}</option>
              ))}
            </select>
            <div className="course-pill">
              <span className="course-dot" style={{ background: courses.find(c=>c.id===studyCourseId)?.accent }} />
              <span className="muted" style={{ fontSize: 13 }}>{courses.find(c=>c.id===studyCourseId)?.available ? 'Available' : 'Coming soon'}</span>
            </div>
          </div>
          <p className="info-line">{courses.find(c=>c.id===studyCourseId)?.blurb}</p>
        </div>

        <div className="field">
          <label>Study scope</label>
          <div className="tabs">
            <button className={`tab ${studyMode === 'full' ? 'active' : ''}`} onClick={() => setStudyMode('full')}>All topics (study everything)</button>
            {studyHasCats && (
              <button className={`tab ${studyMode === 'category' ? 'active' : ''}`} onClick={() => setStudyMode('category')}>One main category</button>
            )}
            <button className={`tab ${studyMode === 'topic' ? 'active' : ''}`} onClick={() => setStudyMode('topic')}>One topic only</button>
          </div>
        </div>

        {studyMode === 'category' && studyHasCats && (
          <div className="field">
            <label>Pick a main category to study</label>
            <div className="cat-grid">
              {studyCats.map((c) => (
                <button
                  key={c.id}
                  className={`cat-chip ${studyCategoryId === c.id ? 'selected' : ''} ${c.count === 0 ? 'empty' : ''}`}
                  disabled={c.count === 0}
                  onClick={() => setStudyCategoryId(c.id)}
                >
                  <div className="cat-name">{c.name}</div>
                  <div className="cat-count">{c.count === 0 ? 'Coming soon' : `${c.count} questions · ${c.topics.length} topics`}</div>
                </button>
              ))}
            </div>
          </div>
        )}

        {studyMode === 'topic' && (
          <div className="field">
            <label>Pick a topic to study</label>
            {studyHasCats ? (
              <div>
                {studyCats.map((c) => (
                  <div key={c.id} className="topic-group">
                    {c.topics.length > 0 && <div className="topic-group-head">{c.name}</div>}
                    <div className="topic-grid">
                      {c.topics.map((t) => (
                        <button
                          key={t.id}
                          className={`topic-chip ${studyTopicId === t.id ? 'selected' : ''}`}
                          onClick={() => setStudyTopicId(t.id)}
                        >
                          <div className="t-name">{t.name}</div>
                          <div className="t-count">{t.count}</div>
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="topic-grid">
                {getTopics(studyCourseId).map((t) => (
                  <button
                    key={t.id}
                    className={`topic-chip ${studyTopicId === t.id ? 'selected' : ''}`}
                    onClick={() => setStudyTopicId(t.id)}
                  >
                    <div className="t-name">{t.name}</div>
                  </button>
                ))}
              </div>
            )}
          </div>
        )}

        <div className="field">
          <label>Number of questions to study</label>
          <select value={studyCount} onChange={(e) => {
            const v = e.target.value
            setStudyCount(v === 'all' ? 'all' : Number(v))
          }}>
            {[10,20,30,40,50,'all'].map((c) => <option key={String(c)} value={c}>{c === 'all' ? 'All available' : `${c} questions`}</option>)}
          </select>
          <p className="info-line" style={{ marginTop: 8 }}>
            {studyMode === 'topic' && studyTopicId
              ? <>You’ll study <strong>{getTopics(studyCourseId).find(t=>t.id===studyTopicId)?.name}</strong>: <strong>{getQuestionCount(studyCourseId, studyTopicId)}</strong> available — shown with correct answer pre-ticked.</>
              : studyMode === 'category' && studyCategoryId
              ? <>You’ll study <strong>{studyCats.find(c=>c.id===studyCategoryId)?.name}</strong>: <strong>{studyCats.find(c=>c.id===studyCategoryId)?.count}</strong> available — shown with correct answer pre-ticked.</>
              : <>You’ll study <strong>{getQuestionCount(studyCourseId)}</strong> questions — each shown with correct answer ticked and a detailed explanation button.</>}
          </p>
        </div>

        {studyError && <p style={{ color: 'var(--red)', fontSize: 14, marginTop: 12 }}>{studyError}</p>}

        <div style={{ marginTop: 20 }}>
          <button className="btn btn-primary btn-lg" onClick={startStudy} style={{ width: '100%', background: 'linear-gradient(135deg, var(--primary), #8A6A12)' }}>
            Start Study Mode — No Timer, See Answers Instantly →
          </button>
        </div>
        <p className="hint" style={{ marginTop: 12 }}>
          💡 Study Mode is for learning, not scoring. No timer, no pressure. Tap <strong>See Detailed Explanation</strong> on any question for the very long, step-by-step breakdown — longer than what you see after submitting a Test.
        </p>
      </div>
    </div>
  )
}
