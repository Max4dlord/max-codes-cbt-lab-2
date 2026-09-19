import { useEffect, useState } from 'react'
import { HashRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom'
import { Analytics } from '@vercel/analytics/react'
import Navbar from './components/Navbar.jsx'
import Landing from './components/Landing.jsx'
import Dashboard from './components/Dashboard.jsx'
import TestRunner from './components/TestRunner.jsx'
import StudyRunner from './components/StudyRunner.jsx'
import Results from './components/Results.jsx'
import Gate from './components/Gate.jsx'
import AdminCode from './components/AdminCode.jsx'
import { gateConfig } from './gateConfig.js'
import { verifyAccess } from './gateStore.js'

function Loading() {
  return (
    <div className="gate-shell">
      <div className="gate-card" style={{ textAlign: 'center' }}>
        <div className="gate-brand" style={{ justifyContent: 'center' }}>
          <span className="nav-logo">MC</span>
          <span className="gate-brand-name">
            {gateConfig.brandName} · <em>{gateConfig.brandSub}</em>
          </span>
        </div>
        <p className="gate-sub">Checking your access…</p>
      </div>
    </div>
  )
}

function Shell() {
  const location = useLocation()
  const isAdmin = location.pathname === '/admin-code'

  // 'checking' | 'in' | 'out'  — never a plain boolean the user can flip,
  // because the answer always comes from the server.
  const [state, setState] = useState(gateConfig.enabled ? 'checking' : 'in')
  const [exp, setExp] = useState(null)

  async function check() {
    if (!gateConfig.enabled) { setState('in'); return }
    const r = await verifyAccess()
    if (r.ok) { setExp(r.exp); setState('in') } else setState('out')
  }

  useEffect(() => {
    check()
    const onFocus = () => { if (gateConfig.enabled) check() }
    window.addEventListener('focus', onFocus)
    return () => window.removeEventListener('focus', onFocus)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // Admin console is always reachable and never gated.
  if (isAdmin) {
    return (
      <Routes>
        <Route path="/admin-code" element={<AdminCode />} />
      </Routes>
    )
  }

  if (state === 'checking') return <Loading />
  if (state === 'out') {
    return <Gate onUnlock={(e) => { setExp(e); setState('in') }} />
  }

  return (
    <>
      <Navbar accessExp={exp} />
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/test" element={<TestRunner />} />
          <Route path="/study" element={<StudyRunner />} />
          <Route path="/results" element={<Results />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      <Analytics />
    </>
  )
}

export default function App() {
  return (
    <HashRouter>
      <Shell />
    </HashRouter>
  )
}
