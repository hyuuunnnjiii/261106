import streamlit as st

st.set_page_config(
    page_title="최현지 | 나를 소개합니다",
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

    .idol-feature {
        display: grid;
        grid-template-columns: minmax(0, 320px) 1fr;
        gap: 2rem;
        align-items: center;
        margin-top: 2rem;
    }
    .anton-photo {
        display: block;
        width: 100%;
        aspect-ratio: 4 / 5;
        object-fit: cover;
        object-position: center;
    }
    .idol-feature h3 {
        margin: 0;
        color: var(--forest);
        font-family: 'Gowun Batang', serif;
        font-size: 2rem;
    }
    .image-credit { margin-top: 1rem; color: var(--muted); font-size: 0.75rem; line-height: 1.8; }
    .image-credit a { color: var(--leaf) !important; }

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
        .idol-feature { grid-template-columns: 1fr; }
        .anton-photo { max-width: 360px; }
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
            <h1>안녕하세요,<br><span>최현지</span>입니다.</h1>
            <a class="hero-link" href="#about">나를 더 알아보기 &nbsp; ↓</a>
        </div>
    </header>

    <nav class="site-nav">
        <div class="nav-label">최현지의 기록</div>
        <div class="nav-links">
            <a href="#about">소개</a>
            <a href="#affiliation">소속</a>
            <a href="#dream">꿈</a>
        </div>
    </nav>

    <section class="section" id="about">
        <div class="section-kicker">01 / ABOUT ME</div>
        <h2>관심 분야와 요즘의 일상</h2>
        <p class="about-copy section-intro">
            관심 분야는 책 읽기와 음악입니다.<br>
            요즘은 과제를 하며 시간을 보내고 있습니다.
        </p>
    </section>

    <section class="section" id="affiliation">
        <div class="section-kicker">02 / WHERE I BELONG</div>
        <h2>함께 배우고 있는 곳</h2>
        <div class="affiliation-band">
            <h3>청주교대 컴퓨터교육과</h3>
        </div>
    </section>

    <section class="section" id="dream">
        <div class="section-kicker">03 / A DREAM IN PROGRESS</div>
        <h2>마음에 품고 있는 방향</h2>
        <div class="dream-band">
            <p>앞으로 좋은 교사가 되고 싶습니다.</p>
        </div>
    </section>

    <section class="section" id="favorite-idol">
        <div class="section-kicker">04 / MY FAVORITE IDOL</div>
        <h2>좋아하는 아이돌</h2>
        <div class="idol-feature">
            <img
                class="anton-photo"
                src="https://upload.wikimedia.org/wikipedia/commons/8/87/20231124_Anton_Lee_%28Riize%29.jpg"
                alt="라이즈 앤톤"
                loading="lazy"
            >
            <div>
                <h3>라이즈 앤톤</h3>
                <p class="image-credit">
                    사진: <a href="https://www.youtube.com/channel/UCY9QGuU9mBLBp_OCRNKeVSw" target="_blank" rel="noopener noreferrer">K-POPIT</a>
                    · <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener noreferrer">CC BY 3.0</a>
                    · <a href="https://commons.wikimedia.org/wiki/File:20231124_Anton_Lee_(Riize).jpg" target="_blank" rel="noopener noreferrer">원본</a>
                </p>
            </div>
        </div>
    </section>

    <footer class="footer">최현지의 작은 기록들 · Made with care</footer>
    """,
    unsafe_allow_html=True,
)
