# Vercel setup — the one 5-minute job (do it twice, once per project)

You only ever do this **once per project**. After that the gate runs itself.

---

## Why I can't do this part for you

I have no Vercel credentials in this workspace and no way to log into your
account — that's by design, and it's a good thing: it means nobody who gets into
this chat can touch your deployments either.

To automate it I'd need you to create a **Vercel API token** and paste it here.
I'd rather you didn't. You've already had to rotate two GitHub tokens because
they ended up in chat history, and a Vercel token is more dangerous — it can
redeploy, change domains and read every env var on your whole account. Pasting
six short values into a web form is faster and safer than that whole dance.

Everything else **is** automated. This is the only manual step, and it's final.

---

## Project 1 — Max-codes  (max-codes.vercel.app)

1. Open **https://vercel.com/dashboard** → click the **Max-codes** project
2. **Settings** (top tabs) → **Environment Variables** (left sidebar)
3. Add these three. For each one: type the Name, paste the Value, make sure
   **Production**, **Preview** and **Development** are all ticked, click **Save**.

| Name | Value |
|---|---|
| `GATE_SECRET` | `8bcd679195f38ee8d3e30385cd1e6e022574f438ce202c21b4c9b4e2d81fa7d1` |
| `ADMIN_KEY` | `Dafidi1357` |
| `CODE_PREFIX` | `MAX-` |

4. Go to the **Deployments** tab → newest deployment → **⋯** menu → **Redeploy**
   → confirm.

> Env vars only apply to *new* deployments. Skipping the redeploy is the single
> most common reason this appears not to work.

---

## Project 2 — exam-prep-by-max  (EEE 282)

Same steps, on the **max-codes-cbt-lab-2** project. Note the **different**
secret and prefix:

| Name | Value |
|---|---|
| `GATE_SECRET` | `53191c1cfdc793b0066ce5bea949be466795a9c984282489498e543720e05637` |
| `ADMIN_KEY` | `Dafidi1357` |
| `CODE_PREFIX` | `EEE-` |

Then **Redeploy** this project too.

The two secrets are deliberately different so the apps stay independent — a
problem with one can never affect the other.

---

## How to confirm it worked

1. Open your site → scroll to the bottom of the gate → click the small
   **Admin** link
2. Enter `Dafidi1357`
3. Paste any test ID, e.g. `A1B2C3-D4E5F6` → **Generate code**

- ✅ A code like `MAX-XXXXXX` appears → **done, you're live**
- ⚠️ An orange "Setup needed" box → the redeploy hasn't finished or a variable
  is missing/misspelled. Wait a minute, re-check the spelling, redeploy again.

---

## Until you do this

The gate **fails closed** — nobody can unlock, including you. That's intentional.
The alternative (falling back to a default secret) is what left both your sites
briefly mintable by anyone who read the public repo, which I've now removed.

If you want the apps usable *right now* while you sort the env vars, set
`enabled: false` in `src/gateConfig.js` and the gate disappears entirely.
Just say the word and I'll push that.
