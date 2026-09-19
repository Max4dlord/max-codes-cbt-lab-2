import { Link, NavLink, useLocation } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { loadSession } from '../progress.js'
import { timeLeftLabel } from '../gateStore.js'

export default function Navbar({ accessExp }) {
  const loc = useLocation()
  const [hasSession, setHasSession] = useState(() => !!loadSession())

  useEffect(() => {
    setHasSession(!!loadSession())
  }, [loc.pathname])

  return (
    <header className="nav">
      <Link to="/" className="nav-brand">
        <img src="/oau-crest.png" alt="Obafemi Awolowo University crest" className="nav-crest" />
        <span className="nav-title">
          OAU <em>· CBT Lab</em>
        </span>
      </Link>
      <nav className="nav-links">
        <NavLink to="/" end>Home</NavLink>
        <NavLink to="/dashboard">Dashboard</NavLink>
        {hasSession && (
          <NavLink to="/test" className="nav-resume">Resume test →</NavLink>
        )}
        {accessExp && (
          <span className="nav-access" title="Time left on your access. Your progress is never affected.">
            {timeLeftLabel(accessExp)} left
          </span>
        )}
      </nav>
    </header>
  )
}
