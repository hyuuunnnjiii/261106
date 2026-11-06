import streamlit as st

st.set_page_config(
    page_title="[이름] | 나를 소개합니다",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    :root {
        --forest: #173d32;
        --leaf: #377c5a;
        --moss: #78977b;
        --mint: #e7f0e5;
        --paper: #f7f8f2;
        --ink: #20362e;
        --muted: #64766c;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 12% 18%, rgba(201, 222, 194, 0.34), transparent 30%),
            repeating-linear-gradient(135deg, rgba(55, 124, 90, 0.025) 0 1px, transparent 1px 9px),
            var(--paper);
        color: var(--ink);
        font-family: 'Noto Sans KR', sans-serif;
    }

    .block-container {
        max-width: 1120px;
        padding: 2rem 2rem 4rem;
    }

    h1, h2, h3, p, a { letter-spacing: 0; }
    .hero {
        min-height: 430px;
        display: flex;
        align-items: flex-end;
        padding: clamp(2rem, 6vw, 5rem);
        color: #fff;
        background-image:
            linear-gradient(90deg, rgba(15, 43, 34, 0.84), rgba(15, 43, 34, 0.24)),
            url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=2000&q=85');
        background-size: cover;
        background-position: center 54%;
    }

    .hero-copy { max-width: 680px; }
    .eyebrow, .section-kicker, .nav-label, .card-index {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }
    .hero .eyebrow { color: #c9e2c5; }
    .hero h1 {
        margin: 0.8rem 0 1rem;
        font-family: 'Gowun Batang', serif;
        font-size: clamp(2.5rem, 7vw, 5rem);
        font-weight: 700;
        line-height: 1.2;
    }
    .hero h1 span { color: #cbe4bf; }
    .hero p {
        margin: 0;
        color: rgba(255,255,255,0.88);
        font-size: 1rem;
        line-height: 1.8;
    }
    .hero-link {
        display: inline-block;
        margin-top: 1.7rem;
        padding-bottom: 0.35rem;
        border-bottom: 1px solid rgba(255,255,255,0.7);
        color: #fff !important;
        font-size: 0.9rem;
        text-decoration: none;
    }

    .site-nav {
        position: sticky;
        top: 0;
        z-index: 20;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid #dfe7dc;
        background: rgba(247, 248, 242, 0.94);
        backdrop-filter: blur(12px);
    }
    .nav-label { color: var(--forest); white-space: nowrap; }
    .nav-links { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 0.45rem 1.25rem; }
    .nav-links a { color: var(--muted) !important; font-size: 0.83rem; text-decoration: none; }
    .nav-links a:hover { color: var(--leaf) !important; }

    .section { padding: 5rem 0 1rem; scroll-margin-top: 5rem; }
    .section-kicker { margin-bottom: 0.8rem; color: var(--leaf); }
    .section h2 {
        margin: 0 0 1rem;
        color: var(--forest);
        font-family: 'Gowun Batang', serif;
        font-size: 2.2rem;
        line-height: 1.4;
    }
    .section-intro { max-width: 700px; color: var(--muted); line-height: 1.9; }
    .about-copy { max-width: 790px; font-size: 1.08rem; line-height: 2.05; }

    .affiliation-band {
        display: grid;
        grid-template-columns: 1fr 1.35fr;
        gap: 2rem;
        align-items: center;
        margin-top: 2rem;
        padding: 2.4rem;
        background: var(--mint);
    }
    .affiliation-band h3 { margin: 0; color: var(--forest); font-family: 'Gowun Batang', serif; font-size: 1.5rem; }
    .affiliation-band p { margin: 0; color: #4c6757; line-height: 1.9; }

    .dream-band {
        margin-top: 2rem;
        padding: 2.5rem 0 2.5rem 2rem;
        border-left: 3px solid #92b78b;
    }
    .dream-band p { max-width: 760px; margin: 0; color: var(--forest); font-family: 'Gowun Batang', serif; font-size: 1.5rem; line-height: 1.8; }

    .item-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 2rem; }
    .item-card { min-height: 190px; padding: 1.5rem; border: 1px solid #dfe7dc; background: rgba(255,255,255,0.56); }
    .card-index { color: var(--moss); }
    .item-card h3 { margin: 1.2rem 0 0.6rem; color: var(--forest); font-family: 'Gowun Batang', serif; font-size: 1.25rem; }
    .item-card p { margin: 0; color: var(--muted); font-size: 0.9rem; line-height: 1.8; }

    .research-list { margin-top: 2rem; border-top: 1px solid #dfe7dc; }
    .research-row { display: grid; grid-template-columns: 150px 1fr; gap: 1rem; padding: 1.4rem 0; border-bottom: 1px solid #dfe7dc; }
    .research-row strong { color: var(--leaf); font-size: 0.9rem; }
    .research-row p { margin: 0; color: var(--muted); line-height: 1.8; }

    .travel-card { min-height: 160px; background: linear-gradient(145deg, #e5eee1, #f8f7ed); }
    .travel-card h3 { margin-top: 2rem; }
    .footer {
        margin-top: 6rem;
        padding-top: 1.4rem;
        border-top: 1px solid #dfe7dc;
        color: var(--muted);
        font-size: 0.82rem;
    }

    @media (max-width: 720px) {
        .block-container { padding: 1rem 1.1rem 3rem; }
        .hero { min-height: 390px; padding: 2rem 1.5rem; }
        .site-nav { align-items: flex-start; flex-direction: column; }
        .nav-links { justify-content: flex-start; gap: 0.7rem 1rem; }
        .section { padding-top: 3.8rem; }
        .section h2 { font-size: 1.8rem; }
        .affiliation-band { grid-template-columns: 1fr; padding: 1.6rem; }
        .item-grid { grid-template-columns: 1fr; }
        .research-row { grid-template-columns: 1fr; gap: 0.35rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="hero">
        <div class="hero-copy">
            <div class="eyebrow">A LITTLE FIELD GUIDE TO ME</div>
            <h1>안녕하세요,<br><span>[이름]</span>입니다.</h1>
            <p>[나를 가장 잘 보여주는 한 문장을 적어보세요.]</p>
            <a class="hero-link" href="#about">나를 더 알아보기 &nbsp; ↓</a>
        </div>
    </header>

    <nav class="site-nav">
        <div class="nav-label">[이름]의 기록</div>
        <div class="nav-links">
            <a href="#about">소개</a>
            <a href="#affiliation">소속</a>
            <a href="#dream">꿈</a>
            <a href="#classes">수업</a>
            <a href="#research">연구</a>
            <a href="#travels">여행</a>
        </div>
    </nav>

    <section class="section" id="about">
        <div class="section-kicker">01 / ABOUT ME</div>
        <h2>천천히, 단단하게 자라는 사람</h2>
        <p class="about-copy section-intro">
            저는 [관심 분야]를 좋아하고, [요즘 시간을 가장 많이 쓰는 일]을 하며 지냅니다.<br>
            새로운 것을 배우고 주변의 작은 변화를 발견하는 순간을 소중히 여깁니다.<br>
            [나를 소개하는 문장이나 나만의 이야기를 더 적어보세요.]
        </p>
    </section>

    <section class="section" id="affiliation">
        <div class="section-kicker">02 / WHERE I BELONG</div>
        <h2>함께 배우고 있는 곳</h2>
        <div class="affiliation-band">
            <h3>[학교 · 기관 · 팀 이름]</h3>
            <p>[소속에서 맡은 역할, 함께하는 사람들, 이곳에서 배우고 있는 것을 적어보세요.]</p>
        </div>
    </section>

    <section class="section" id="dream">
        <div class="section-kicker">03 / A DREAM IN PROGRESS</div>
        <h2>마음에 품고 있는 방향</h2>
        <div class="dream-band">
            <p>“[앞으로 이루고 싶은 꿈과 그 꿈을 꾸게 된 이유를 적어보세요.]”</p>
        </div>
    </section>

    <section class="section" id="classes">
        <div class="section-kicker">04 / THINGS I LEARNED</div>
        <h2>기억에 남는 수업</h2>
        <p class="section-intro">배움의 순간과 그 안에서 발견한 생각을 모았습니다.</p>
        <div class="item-grid">
            <article class="item-card">
                <div class="card-index">CLASS 01</div>
                <h3>[수업 이름]</h3>
                <p>[배운 내용이나 기억에 남는 점을 적어보세요.]</p>
            </article>
            <article class="item-card">
                <div class="card-index">CLASS 02</div>
                <h3>[수업 이름]</h3>
                <p>[배운 내용이나 기억에 남는 점을 적어보세요.]</p>
            </article>
            <article class="item-card">
                <div class="card-index">CLASS 03</div>
                <h3>[수업 이름]</h3>
                <p>[배운 내용이나 기억에 남는 점을 적어보세요.]</p>
            </article>
        </div>
    </section>

    <section class="section" id="research">
        <div class="section-kicker">05 / QUESTIONS I FOLLOW</div>
        <h2>오래 들여다보고 싶은 질문</h2>
        <p class="section-intro">관심 있는 주제와 지금까지의 연구 경험을 기록합니다.</p>
        <div class="research-list">
            <div class="research-row">
                <strong>[연구 주제 또는 연도]</strong>
                <p>[연구에서 궁금했던 점, 맡은 역할, 새롭게 알게 된 점을 적어보세요.]</p>
            </div>
            <div class="research-row">
                <strong>[연구 주제 또는 연도]</strong>
                <p>[진행 중인 연구나 앞으로 더 탐구하고 싶은 내용을 적어보세요.]</p>
            </div>
        </div>
    </section>

    <section class="section" id="travels">
        <div class="section-kicker">06 / PLACES I HAVE SEEN</div>
        <h2>마음에 남은 여행지</h2>
        <p class="section-intro">풍경과 사람, 그곳에서 만난 작은 장면들을 기억합니다.</p>
        <div class="item-grid">
            <article class="item-card travel-card">
                <div class="card-index">PLACE 01</div>
                <h3>[도시 · 나라]</h3>
                <p>[가장 선명하게 기억나는 순간을 적어보세요.]</p>
            </article>
            <article class="item-card travel-card">
                <div class="card-index">PLACE 02</div>
                <h3>[도시 · 나라]</h3>
                <p>[그곳에서 보고 느낀 것을 적어보세요.]</p>
            </article>
            <article class="item-card travel-card">
                <div class="card-index">PLACE 03</div>
                <h3>[도시 · 나라]</h3>
                <p>[다시 가고 싶은 이유를 적어보세요.]</p>
            </article>
        </div>
    </section>

    <footer class="footer">[이름]의 작은 기록들 · Made with care</footer>
    """,
    unsafe_allow_html=True,
)
