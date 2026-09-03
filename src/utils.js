import { courses, topicMeta, questionBank, categoryMeta } from './data.js'

// Fisher-Yates shuffle (returns a new array).
export function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// seconds -> "MM:SS"
export function formatTime(totalSeconds) {
  const s = Math.max(0, Math.floor(totalSeconds))
  const m = Math.floor(s / 60)
  const r = s % 60
  return `${String(m).padStart(2, '0')}:${String(r).padStart(2, '0')}`
}

export function getCourse(courseId) {
  return courses.find((c) => c.id === courseId) || null
}

// Derive topic list (with live question counts) for a course.
// Topics are "auto-classified" here: anything tagged with a topicId in the
// question bank shows up on the dashboard automatically.
export function getTopics(courseId) {
  const meta = topicMeta[courseId] || []
  const qs = questionBank[courseId] || []
  return meta.map((t) => ({
    ...t,
    count: qs.filter((q) => q.topicId === t.id).length
  }))
}

// Main categories for a course, each carrying its nested topics (with live
// counts). Returns [] for courses that have no category structure.
export function getCategories(courseId) {
  const cats = categoryMeta[courseId] || []
  if (!cats.length) return []
  const qs = questionBank[courseId] || []
  const topics = topicMeta[courseId] || []
  return cats.map((c) => {
    const subs = topics
      .filter((t) => t.categoryId === c.id)
      .map((t) => ({ ...t, count: qs.filter((q) => q.topicId === t.id).length }))
    return {
      ...c,
      topics: subs,
      count: subs.reduce((a, t) => a + t.count, 0)
    }
  })
}

export function getQuestionCount(courseId, topicId = null) {
  const qs = questionBank[courseId] || []
  return topicId ? qs.filter((q) => q.topicId === topicId).length : qs.length
}

// Build the actual ordered question set for a test.
// mode: 'full' (all topics) | 'category' (one main category) | 'topic' (single topic)
// count: number, or 'all'
export function buildQuestionSet(courseId, { mode, topicId, categoryId, count }) {
  let pool = questionBank[courseId] || []
  if (mode === 'topic' && topicId) {
    pool = pool.filter((q) => q.topicId === topicId)
  }
  if (mode === 'category' && categoryId) {
    const ids = new Set(
      (topicMeta[courseId] || [])
        .filter((t) => t.categoryId === categoryId)
        .map((t) => t.id)
    )
    pool = pool.filter((q) => ids.has(q.topicId))
  }
  const shuffled = shuffle(pool)
  const n = !count || count === 'all' ? shuffled.length : Math.min(Number(count), shuffled.length)
  return shuffled.slice(0, n)
}

// Optional Telegram channel/group link. Set this to your real invite link to
// surface a "Discuss in Telegram" button inside the solution panel. The link
// opens in a new tab so the test/progress is never disturbed.
export const TELEGRAM_URL = '' // e.g. 'https://t.me/+YourMTH202Group'
