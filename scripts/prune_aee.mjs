// AEE 202 hygiene pass: merge overlapping topics, trim bank to ~100 questions,
// keep ALL diagram questions. Emits JSON for the data.js splice script.
import { questionBank } from '../src/data.js'
import { writeFileSync } from 'fs'

const MERGE = {
  'welding-processes-defects': ['welding-defects', 'welding-classification', 'mig-welding', 'tig-welding', 'gas-welding', 'arc-welding', 'gas-arc-welding', 'production-welding', 'metal-joining', 'joining-metals'],
  'fasteners': ['fasteners'],
  'metal-working': ['hot-metal-working', 'metal-shapes'],
  'heat-treatment': ['heat-treatment'],
  'cutting-tools': ['cutting-tools'],
  'drilling': ['drilling'],
  'bench-work-fitting': ['bench-work', 'bench-work-fitting'],
  'machine-operations': ['machine-operations', 'workshop-machines'],
  'advanced-manufacturing': ['advanced-manufacturing'],
  'hand-tools': ['hand-tools'],
  'jigs-fixtures': ['jigs-fixtures', 'jig-fixture-design'],
  'workshop-safety': ['workshop-safety', 'workshop-hazards', 'cold-metal-safety'],
}

const TOPIC_NAMES = {
  'welding-processes-defects': 'Welding Processes & Defects',
  'fasteners': 'Fasteners',
  'metal-working': 'Metal Working (Hot & Cold)',
  'heat-treatment': 'Heat Treatment of Steel',
  'cutting-tools': 'Cutting Tools & Hacksaws',
  'drilling': 'Drilling & Drill Press',
  'bench-work-fitting': 'Bench Work & Fitting',
  'machine-operations': 'Machine Operations & Workshop Machines',
  'advanced-manufacturing': 'Advanced Manufacturing Processes',
  'hand-tools': 'Hand & Power Tools',
  'jigs-fixtures': 'Jigs & Fixtures',
  'workshop-safety': 'Workshop Safety & Hazards',
}

// ~100 total (101 with cutting-tools carrying 4 diagrams)
const QUOTA = {
  'welding-processes-defects': 32,
  'fasteners': 9,
  'metal-working': 4,
  'heat-treatment': 4,
  'cutting-tools': 4,
  'drilling': 3,
  'bench-work-fitting': 7,
  'machine-operations': 4,
  'advanced-manufacturing': 12,
  'hand-tools': 1,
  'jigs-fixtures': 8,
  'workshop-safety': 13,
}

const CATEGORIES = [
  { id: 'shared-drive', name: 'Questions formed from materials in Shared Drive' },
  { id: 'past-questions', name: 'Questions from Actual past questions' },
  { id: 'first-slides', name: 'Questions formed from First Shared Slide' },
]

const bank = questionBank.aee202 || []

// group by original topic
const byTopic = {}
for (const q of bank) (byTopic[q.topicId] ??= []).push(q)

// deterministic even-spread ordering so sampling covers the whole pool
function spread(arr) {
  const n = arr.length
  const G = 3
  return arr
    .map((q, i) => ({ q, k: (i * G) % n }))
    .sort((a, b) => a.k - b.k)
    .map((x) => x.q)
}

const selected = []
const report = []

for (const [merged, originals] of Object.entries(MERGE)) {
  const all = originals.flatMap((id) => byTopic[id] || [])
  const diagrams = all.filter((q) => q.image)
  const kept = [...diagrams]
  let rem = Math.max(0, (QUOTA[merged] ?? 10) - diagrams.length)

  const pools = originals
    .map((id) => (byTopic[id] || []).filter((q) => !q.image))
    .filter((a) => a.length > 0)
    .map(spread)

  let guard = 0
  while (rem > 0 && pools.length && guard++ < 2000) {
    let took = false
    for (const pool of pools) {
      if (rem <= 0) break
      if (!pool.length) continue
      kept.push(pool.shift())
      rem--
      took = true
    }
    if (!took) break
  }

  for (const q of kept) selected.push({ ...q, topicId: merged })
  report.push(`${merged}: kept ${kept.length} (${diagrams.length} diagram) from ${all.length}`)
}

const topics = Object.keys(MERGE).map((id) => ({
  id,
  name: TOPIC_NAMES[id],
  categoryId: 'shared-drive',
}))

writeFileSync('.prune_out_questions.json', JSON.stringify(selected, null, 2))
writeFileSync('.prune_out_topics.json', JSON.stringify(topics, null, 2))
writeFileSync('.prune_out_categories.json', JSON.stringify(CATEGORIES, null, 2))

console.log(report.join('\n'))
console.log('TOTAL KEPT:', selected.length, '| diagram questions kept:', selected.filter((q) => q.image).length)
