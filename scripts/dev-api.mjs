// Local stand-in for Vercel's serverless functions, so `npm run dev` has a
// working /api/* during development. Vercel does NOT use this file.
import http from 'node:http'
import { pathToFileURL } from 'node:url'
import path from 'node:path'

const PORT = process.env.API_PORT || 3001
const routes = ['unlock', 'verify', 'admin-code', 'issue', 'go', 'status']
const mods = {}
for (const r of routes) {
  mods[r] = (await import(pathToFileURL(path.resolve('api', `${r}.js`)).href)).default
}

http.createServer(async (req, res) => {
  const name = req.url.split('?')[0].replace(/^\/api\//, '').replace(/\/$/, '')
  const fn = mods[name]
  if (!fn) { res.statusCode = 404; return res.end('{"ok":false,"error":"no route"}') }
  res.status = (c) => { res.statusCode = c; return res }
  res.send = (b) => res.end(b)
  if (!res.setHeader.__patched) {
    const orig = res.setHeader.bind(res)
    res.setHeader = (k, v) => orig(k, v)
    res.setHeader.__patched = true
  }
  try { await fn(req, res) }
  catch (e) { res.statusCode = 500; res.end(JSON.stringify({ ok: false, error: String(e) })) }
}).listen(PORT, '0.0.0.0', () => console.log('dev api on :' + PORT))
