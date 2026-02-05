from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
        return """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <title>Will you be my Valentine?</title>
            <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;600&family=Playfair+Display:wght@400;600&display=swap" rel="stylesheet">
            <style>
                :root{
                    --bg-1:#ffdde1;
                    --bg-2:#fceefe;
                    --accent-pink:#ff6b9a;
                    --accent-rose:#ff2e63;
                    --glass: rgba(255,255,255,0.12);
                }
                html,body{height:100%; margin:0; overflow:hidden;}
                body{
                    font-family: Poppins, sans-serif; -webkit-font-smoothing:antialiased;
                    background: radial-gradient( circle at 10% 10%, #fff0f6 0%, var(--bg-1) 10%, var(--bg-2) 60% );
                    display:flex; align-items:center; justify-content:center; overflow:hidden;
                }
                .scene{
                    width:92%; max-width:900px; padding:36px; border-radius:20px; position:relative;
                    box-shadow: 0 20px 60px rgba(255,105,180,0.25), inset 0 1px 0 rgba(255,255,255,0.6);
                    background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(255,255,255,0.3));
                    backdrop-filter: blur(10px);
                    text-align:center;
                    animation: sceneGlow 4s ease-in-out infinite;
                }
                @keyframes sceneGlow{0%,100%{box-shadow: 0 20px 60px rgba(255,105,180,0.25), inset 0 1px 0 rgba(255,255,255,0.6);} 50%{box-shadow: 0 30px 80px rgba(255,105,180,0.35), inset 0 1px 0 rgba(255,255,255,0.6);}}
                h1{
                    margin:8px 0 20px; font-family: 'Dancing Script', cursive; font-size:64px; line-height:1.08; padding-bottom:6px;
                    background: linear-gradient(90deg,#ff007a,#ff2e63,#ff9ac2);
                    -webkit-background-clip:text; background-clip:text; color:transparent;
                    filter: drop-shadow(0 4px 12px rgba(255,90,140,0.3));
                    animation: titleBounce 3s ease-in-out infinite;
                }
                @keyframes titleBounce{0%,100%{transform:translateY(0)} 50%{transform:translateY(-4px)}}
                .flower-row{font-size:30px; margin-bottom:6px; animation: flowerSway 6s ease-in-out infinite;}
                @keyframes flowerSway{0%,100%{transform:scale(1)} 50%{transform:scale(1.08)}}
                .question-wrap{margin-top:18px}

                /* Buttons area */
                #buttons{position:relative; height:140px; margin-top:14px;}
                .btn{
                    position:absolute; top:50%; transform:translate(-50%,-50%); padding:18px 36px; border-radius:40px; border:none;
                    font-size:22px; cursor:pointer; color:white; font-weight:600; box-shadow: 0 8px 24px rgba(0,0,0,0.12);
                    transition: transform .18s ease, box-shadow .18s ease, left 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), top 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
                }
                .btn:hover:not(#no){filter: brightness(1.15); box-shadow: 0 12px 40px rgba(0,0,0,0.2);}
                .btn:active{transform:translate(-50%,-50%) scale(.97)}
                #yes{left:40%; background:linear-gradient(135deg,#ff6b9a,#ff2e63); position:relative;}
                #yes::before{content:''; position:absolute; inset:0; border-radius:40px; background:linear-gradient(135deg,#ff6b9a,#ff2e63); filter:blur(8px); opacity:0; transition:opacity 0.3s; z-index:-1;}
                #yes:hover::before{opacity:0.8;}
                #no{left:60%; background:linear-gradient(135deg,#6b8bff,#8ec5ff);}

                /* modal */
                .overlay{position:fixed; inset:0; display:flex; align-items:center; justify-content:center; background:rgba(0,0,0,0.45); opacity:0; pointer-events:none; transition:opacity .25s ease}
                .overlay.show{opacity:1; pointer-events:auto}
                .modal{background:linear-gradient(135deg, #fff 0%, #ffeef6 100%); padding:36px; border-radius:20px; max-width:640px; text-align:center; box-shadow:0 30px 90px rgba(0,0,0,0.3); animation:modalPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);}
                @keyframes modalPop{from{transform:scale(0.7) translateY(-50px); opacity:0} to{transform:scale(1) translateY(0); opacity:1}}
                .modal h2{font-family:'Dancing Script', cursive; color:#d6005e; margin:0 0 6px; font-size:42px; animation:titleShine 2s ease-in-out infinite;}
                @keyframes titleShine{0%,100%{color:#d6005e} 50%{color:#ff2e63}}
                .modal p{color:#4b2333; font-size:20px; margin:18px 0 0; line-height:1.6; font-weight:500;}
                .close{margin-top:24px; padding:12px 28px; border-radius:12px; border:none; background:linear-gradient(135deg,#ff6b9a,#ff2e63); color:#fff; cursor:pointer; font-weight:600; transition:all 0.3s; box-shadow:0 6px 20px rgba(255,107,154,0.3);}
                .close:hover{transform:translateY(-2px); box-shadow:0 10px 30px rgba(255,107,154,0.4);}

                /* floating hearts/flowers */
                .floating{position:fixed; pointer-events:none; font-size:28px; opacity:.8; animation:floatUp linear infinite; filter:drop-shadow(0 2px 4px rgba(0,0,0,0.1));}
                @keyframes floatUp{from{transform:translateY(0) rotateZ(0) scale(0.8); opacity:0.8} to{transform:translateY(-100vh) rotateZ(360deg) scale(1); opacity:0)}
                .confetti{position:fixed; pointer-events:none; font-size:24px; animation:confettiFall linear;}
                @keyframes confettiFall{to{transform:translateY(100vh) rotateZ(720deg); opacity:0}}
            </style>
        </head>
        <body>
            <div class="scene">
                <div class="flower-row">🌸 🌺 🌷 🌹 💐</div>
                <div class="question-wrap">
                    <h1>Will you be my Valentine? ❤️</h1>       
                </div>

                <div id="buttons" aria-hidden="false">
                    <button id="yes" class="btn">Yes</button>
                    <button id="no" class="btn">No</button>
                </div>
            </div>

            <div id="overlay" class="overlay" role="dialog" aria-modal="true">
                <div class="modal">
                    <h2>You're the best!</h2>
                    <p id="secret">I’m really glad you said yes. Thank you for being my Valentine—I will cherish this forever.</p>
                    <button class="close" id="closeBtn">Close</button>
                </div>
            </div>

            <script>
                const yes = document.getElementById('yes');
                const no = document.getElementById('no');
                const buttonsArea = document.getElementById('buttons');
                const overlay = document.getElementById('overlay');
                const closeBtn = document.getElementById('closeBtn');

                // Ensure initial positions (non-overlapping)
                function initPositions(){
                    yes.style.left = '40%'; yes.style.top = '50%';
                    no.style.left = '60%'; no.style.top = '50%';
                }

                function rectsOverlap(r1, r2){
                    return !(r1.right < r2.left || r1.left > r2.right || r1.bottom < r2.top || r1.top > r2.bottom);
                }

                // Move the No button away when user hovers over it; avoid overlapping the Yes button
                function moveNo(){
                    const areaRect = buttonsArea.getBoundingClientRect();
                    const yesRect = yes.getBoundingClientRect();
                    const nw = no.offsetWidth, nh = no.offsetHeight;
                    let attempts = 0;
                    // Small movement radius: offset by 40-80px in random direction
                    while(attempts < 20){
                        const angle = Math.random() * Math.PI * 2;
                        const distance = 40 + Math.random() * 40;
                        const currentPos = no.getBoundingClientRect();
                        const centerX = currentPos.left + nw/2;
                        const centerY = currentPos.top + nh/2;
                        const newCenterX = centerX + Math.cos(angle) * distance;
                        const newCenterY = centerY + Math.sin(angle) * distance;
                        const left = newCenterX - nw/2;
                        const top = newCenterY - nh/2;
                        const candidate = {left:left, top:top, right:left+nw, bottom:top+nh};
                        // Check bounds and no overlap
                        if(left >= areaRect.left && left + nw <= areaRect.right && 
                           top >= areaRect.top && top + nh <= areaRect.bottom &&
                           !rectsOverlap(candidate, yesRect)){
                            const relLeft = ((left - areaRect.left) + nw/2) / areaRect.width * 100;
                            const relTop = ((top - areaRect.top) + nh/2) / areaRect.height * 100;
                            no.style.left = relLeft + '%';
                            no.style.top = relTop + '%';
                            return;
                        }
                        attempts++;
                    }
                    // fallback: small nudge down
                    no.style.top = (parseFloat(no.style.top) + 15) + '%';
                }

                let mouseX = 0, mouseY = 0;
                document.addEventListener('mousemove', (e) => {
                    mouseX = e.clientX;
                    mouseY = e.clientY;
                });

                function smoothMoveNo() {
                    const noRect = no.getBoundingClientRect();
                    const noCenterX = noRect.left + noRect.width / 2;
                    const noCenterY = noRect.top + noRect.height / 2;
                    const dx = noCenterX - mouseX;
                    const dy = noCenterY - mouseY;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    // If mouse is within 120px, slide away
                    if (distance < 120) {
                        const angle = Math.atan2(dy, dx);
                        const moveDistance = Math.max(0, 120 - distance) * 0.5;
                        const newX = noCenterX + Math.cos(angle) * moveDistance;
                        const newY = noCenterY + Math.sin(angle) * moveDistance;
                        const areaRect = buttonsArea.getBoundingClientRect();
                        const nw = no.offsetWidth, nh = no.offsetHeight;
                        
                        let finalX = newX - nw / 2;
                        let finalY = newY - nh / 2;
                        
                        // Keep within bounds
                        finalX = Math.max(areaRect.left, Math.min(finalX, areaRect.right - nw));
                        finalY = Math.max(areaRect.top, Math.min(finalY, areaRect.bottom - nh));
                        
                        const relLeft = ((finalX - areaRect.left) + nw / 2) / areaRect.width * 100;
                        const relTop = ((finalY - areaRect.top) + nh / 2) / areaRect.height * 100;
                        
                        no.style.left = relLeft + '%';
                        no.style.top = relTop + '%';
                    }
                }
                
                // Continuous smooth animation
                setInterval(smoothMoveNo, 16);
                
                yes.addEventListener('click', ()=>{
                    overlay.classList.add('show');
                    createConfetti();
                });

                closeBtn.addEventListener('click', ()=> overlay.classList.remove('show'));

                // Create some floating hearts/flowers for decoration
                function spawnFloating(){
                    const emojis = ['💖','🌸','🌹','✨','💐','💕','🌷','🌺','💗','💓'];
                    for(let i=0;i<15;i++){
                        const s = document.createElement('div');
                        s.className='floating';
                        s.style.left = (Math.random()*100)+'%';
                        s.style.bottom = '-30px';
                        s.style.fontSize = (16+Math.random()*28)+'px';
                        s.style.opacity = 0.6 + Math.random()*0.4;
                        s.style.animationDuration = (8 + Math.random()*8)+'s';
                        s.style.animationDelay = Math.random()*3 + 's';
                        s.textContent = emojis[Math.floor(Math.random()*emojis.length)];
                        document.body.appendChild(s);
                        // Respawn after animation
                        setTimeout(() => s.remove(), 16000);
                    }
                    setTimeout(spawnFloating, 3000);
                }

                function createConfetti(){
                    const emojis = ['💖','🌸','🌹','✨','💐','💕','🌷','🌺','❤️'];
                    for(let i=0;i<50;i++){
                        const c = document.createElement('div');
                        c.className='confetti';
                        c.style.left = (Math.random()*100)+'%';
                        c.style.top = '-20px';
                        c.style.fontSize = (16+Math.random()*24)+'px';
                        c.textContent = emojis[Math.floor(Math.random()*emojis.length)];
                        c.style.animationDuration = (2.5 + Math.random()*1.5)+'s';
                        c.style.animationDelay = (Math.random()*0.5)+'s';
                        document.body.appendChild(c);
                        setTimeout(() => c.remove(), 4000);
                    }
                }

                initPositions();
                spawnFloating();
            </script>
        </body>
        </html>
        """


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)
