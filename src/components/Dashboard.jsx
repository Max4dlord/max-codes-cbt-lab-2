import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { courses } from '../data.js'
import { getTopics, getCategories, getLectures, buildQuestionSet } from '../utils.js'
import { loadSession, clearSession, saveSession } from '../progress.js'
import { saveStudySession } from '../progress.js'

const DURATIONS = [10, 15, 20, 25, 30, 45, 60, 90]
const COUNTS = [10, 20, 30, 40, 50, 'all']

export default function Dashboard() {
  const navigate = useNavigate()
  const existing = loadSession()

  const [courseId, setCourseId] = useState(courses.find((c) => c.available)?.id || courses[0].id)
  const [mode, setMode] = useState('full') // 'full' | 'topic' (SWEP day) | 'lecture'
  const [topicId, setTopicId] = useState(null)
  const [lectureId, setLectureId] = useState(null)
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
  const lectures = getLectures(courseId)
  const selectedTopic = topics.find((t) => t.id === topicId)
  const selectedLecture = lectures.find((l) => l.id === lectureId)

  function startTest() {
    setError('')
    if (!course.available) {
      setError('This course is coming soon. Please check back later or choose an available course.')
      return
    }
    if (mode === 'topic' && !topicId) {
      setError('Please pick a SWEP day to start.')
      return
    }
    if (mode === 'lecture' && !lectureId) {
      setError('Please pick a lecture to start.')
      return
    }
    const set = buildQuestionSet(courseId, {
      mode,
      topicId: mode === 'topic' ? topicId : null,
      lectureId: mode === 'lecture' ? lectureId : null,
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
      lectureId: mode === 'lecture' ? lectureId : null,
      topicName:
        mode === 'topic' ? selectedTopic?.name : mode === 'lecture' ? selectedLecture?.name : null,
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
                {' '}{existing.index + 1} answered ·
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

      {/* ================= TEST MODE ================= */}
      <div className="mode-band mode-band-test">
        <div className="mode-band-icon">⏱️</div>
        <div>
          <h2 className="mode-band-title">Test Mode</h2>
          <p className="mode-band-sub">
            Timed and scored, just like the real CBT. A countdown runs, answers stay
            hidden until you submit, then you get your score with explanations.
          </p>
        </div>
      </div>

      <div className="grid-2">
        {/* ---- Configuration ---- */}
        <div className="card">
          <h2>1 · Configure your test</h2>

          <div className="field">
            <label>Course</label>
            {courses.length > 1 ? (
              <div className="course-select-wrap">
                <select value={courseId} onChange={(e) => { setCourseId(e.target.value); setTopicId(null); setLectureId(null); setMode('full') }}>
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
              </div>
            )}
            <p className="info-line">{course.blurb}</p>
          </div>

          <div className="field">
            <label>Test mode</label>
            <div className="tabs">
              <button className={`tab ${mode === 'full' ? 'active' : ''}`} onClick={() => setMode('full')}>Full test (all topics)</button>
              <button className={`tab ${mode === 'topic' ? 'active' : ''}`} onClick={() => setMode('topic')}>Test across SWEP Days</button>
              {lectures.length > 0 && (
                <button className={`tab ${mode === 'lecture' ? 'active' : ''}`} onClick={() => setMode('lecture')}>Test per Lecture/Presentation/Slide</button>
              )}
            </div>
          </div>

          {mode === 'lecture' && (
            <div className="field">
              <label>Pick a lecture / presentation</label>
              {Array.from(new Set(lectures.map((l) => l.dayId))).map((dayId) => {
                const day = topics.find((t) => t.id === dayId)
                const dayLectures = lectures.filter((l) => l.dayId === dayId)
                return (
                  <div key={dayId} className="topic-group">
                    {dayLectures.length > 0 && (
                      <div className="topic-group-head">{day?.name || dayId}</div>
                    )}
                    <div className="lecture-grid">
                      {dayLectures.map((l) => (
                        <button
                          key={l.id}
                          className={`lecture-chip ${lectureId === l.id ? 'selected' : ''}`}
                          onClick={() => setLectureId(l.id)}
                        >
                          <div className="lecture-name">{l.name}</div>
                          <div className="lecture-meta">{l.speaker}</div>
                        </button>
                      ))}
                    </div>
                  </div>
                )
              })}
            </div>
          )}

          {mode === 'topic' && (
            <div className="field">
              <label>Pick a SWEP day</label>
              {hasCats ? (
                <div>
                  {categories.filter((c) => !c.spansAll).map((c) => (
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
              ? <>Ready for <strong>{selectedTopic?.name}</strong> — questions will be shuffled on start.</>
              : mode === 'lecture' && lectureId
              ? <>Ready for <strong>{selectedLecture?.name}</strong> — questions will be shuffled on start.</>
              : <>Full course pool ready — questions will be shuffled on start.</>}
          </p>

          {error && <p style={{ color: 'var(--red)', fontSize: 14, marginTop: 12 }}>{error}</p>}

          <div style={{ marginTop: 20 }}>
            <button className="btn btn-primary btn-lg" onClick={startTest} style={{ width: '100%' }}>
              Start {mode === 'topic' ? 'SWEP day' : mode === 'lecture' ? 'lecture' : 'full'} test →
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
            {course.code} covers <strong style={{ color: 'var(--text)' }}>{topics.length}</strong> topic{topics.length===1?'':'s'} in tertiary-standard depth. Select a mode on the left to begin.
          </p>

          {hasCats ? (
            categories.filter(c=>!c.spansAll).map((c) => (
              <div key={c.id} style={{ marginTop: 16 }}>
                <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 6 }}>
                  {c.name}
                </div>
                <div className="topic-grid" style={{ marginTop: 4 }}>
                  {c.topics.length > 0 ? c.topics.map((t) => (
                    <div key={t.id} style={{ padding: 10, borderRadius: 10, background: 'var(--bg-soft)', border: '1px solid var(--border)', fontSize: 13 }}>
                      <span style={{ fontWeight: 600 }}>{t.name}</span>
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

      {/* ================= STUDY MODE ================= */}
      <div className="mode-divider"><span>or learn without pressure</span></div>

      <div className="mode-band mode-band-study">
        <div className="mode-band-icon">📖</div>
        <div>
          <h2 className="mode-band-title">
            Study Mode <span className="mode-band-tag">NO TIMER</span>
          </h2>
          <p className="mode-band-sub">
            The same questions, but nothing is timed and the correct answer is already
            ticked in green. Explanations here are much longer than in Test Mode — deep
            dives, common mistakes, and how to approach similar questions.
          </p>
        </div>
      </div>

      <div className="card study-card">

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
                  <div className="cat-count">
                    {c.count === 0
                      ? 'Coming soon'
                      : c.spansAll
                      ? `Everything, shuffled`
                      : `${c.topics.length} topics`}
                  </div>
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
                {studyCats.filter((c) => !c.spansAll).map((c) => (
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
              ? <>You’ll study <strong>{getTopics(studyCourseId).find(t=>t.id===studyTopicId)?.name}</strong> — shown with correct answer pre-ticked.</>
              : studyMode === 'category' && studyCategoryId
              ? <>You’ll study <strong>{studyCats.find(c=>c.id===studyCategoryId)?.name}</strong> — shown with correct answer pre-ticked.</>
              : <>You’ll study with correct answer ticked and a detailed explanation button.</>}
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
