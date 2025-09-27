import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="¿Me amás?", page_icon="❤️", layout="centered")
st.title("💌 Pregunta importante")
st.subheader("¿Me amás?")

custom_html = """
<div id="wrap">
  <div class="question">¿Me amás?</div>
  <div class="buttons">
    <button id="muchote">Muchote 💖</button>
    <button id="poquito">Poquito 😅</button>
  </div>
  <div id="msg"></div>
</div>

<style>
  :root { --w: 720px; --h: 420px; }
  #wrap{
    width: var(--w); max-width: 95vw; height: var(--h); max-height: 70vh;
    border-radius: 18px; border: 1px solid #eee; padding: 24px;
    position: relative; overflow: hidden; background: #fff;
    box-shadow: 0 10px 24px rgba(0,0,0,.07);
    display: grid; grid-template-rows: auto 1fr auto; place-items: center;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }
  .question{ font-size: 28px; font-weight: 700; margin: 4px 0 18px; }
  .buttons{ position: relative; width: 100%; height: 100%; }
  #muchote{
    position: absolute; left: 50%; top: 55%; transform: translate(-50%, -50%);
    padding: 12px 18px; border-radius: 999px; border: 0; font-size: 16px; cursor: pointer;
    background: #ff4b4b; color: #fff; box-shadow: 0 6px 14px rgba(255,75,75,.35);
  }
  #poquito{
    position: absolute; left: 20%; top: 30%;
    padding: 12px 18px; border-radius: 999px; border: 0; font-size: 16px; cursor: pointer;
    background: #f1f1f1; color: #444; box-shadow: 0 6px 14px rgba(0,0,0,.07);
    transition: transform .08s ease;
  }
  #msg{
    position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%);
    font-size: 18px; color: #ff4b4b; font-weight: 600; text-align: center;
  }
</style>

<script>
(function(){
  const wrap = document.getElementById('wrap');
  const poco = document.getElementById('poquito');
  const mucho = document.getElementById('muchote');
  const msg  = document.getElementById('msg');

  function bounds(){
    const r = wrap.getBoundingClientRect();
    return { w: r.width, h: r.height };
  }

  function movePoquito(nx, ny){
    const b = poco.getBoundingClientRect();
    const pad = 8;
    const { w, h } = bounds();
    const maxX = w - b.width - pad;
    const maxY = h - b.height - pad;
    nx = Math.max(pad, Math.min(nx, maxX));
    ny = Math.max(pad, Math.min(ny, maxY));
    poco.style.left = nx + "px";
    poco.style.top  = ny + "px";
  }

  function randomMove(){
    const b = poco.getBoundingClientRect();
    const { w, h } = bounds();
    const nx = Math.random() * (w - b.width - 16) + 8;
    const ny = Math.random() * (h - b.height - 16) + 8;
    movePoquito(nx, ny);
  }

  wrap.addEventListener('mousemove', (e) => {
    const br = poco.getBoundingClientRect();
    const wr = wrap.getBoundingClientRect();
    const mx = e.clientX - wr.left;
    const my = e.clientY - wr.top;
    const cx = br.left - wr.left + br.width/2;
    const cy = br.top  - wr.top  + br.height/2;
    const dx = mx - cx;
    const dy = my - cy;
    const dist = Math.hypot(dx, dy);

    const zonaPeligro = 110;
    if (dist < zonaPeligro){
      const k = 1.2;
      const nx = (cx - dx * k) - br.width/2;
      const ny = (cy - dy * k) - br.height/2;
      movePoquito(nx, ny);
      poco.style.transform = "scale(0.98)";
      setTimeout(()=> poco.style.transform = "scale(1)", 80);
    }
  });

  poco.addEventListener('click', (e) => {
    e.preventDefault();
    msg.textContent = "¡Ese botón se escapa! 😆 Intentá con 'Muchote'.";
    randomMove();
  });

  mucho.addEventListener('click', () => {
    msg.style.color = "#2e7d32";
    msg.textContent = "¡Yo también te amo MU-CHO-TE! 💖🎉";
  });

  randomMove();
})();
</script>
"""

# incrustamos el HTML/JS
html(custom_html, height=520, scrolling=False)
