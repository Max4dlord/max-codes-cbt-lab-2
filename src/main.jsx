import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)

// Remove the loading screen once React has mounted
requestAnimationFrame(() => {
  const ls = document.getElementById('loading-screen')
  if (ls) ls.remove()
})
