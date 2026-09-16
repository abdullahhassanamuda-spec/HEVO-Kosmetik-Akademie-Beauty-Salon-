from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# بيانات الاتصال المحدثة
# ==========================================
PHONE_NUMBER = "+491739125695"
WHATSAPP_NUMBER = "491739125695"
INSTAGRAM_HANDLE = "@hevo_kosmatic_akademie_"

HTML_LAYOUT = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEVO KOSMETIK AKADEMIE | KÖLN</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-dark: #0a0a0a;
            --card-bg: #141414;
            --accent-gold: #c5a059;
            --text-white: #ffffff;
            --text-gold-light: #e6ca94;
        }}
        html {{
            scroll-behavior: smooth;
        }}
        body {{
            background-color: var(--bg-dark);
            color: var(--text-white);
            font-family: 'Montserrat', sans-serif;
        }}
        h1, h2, h3, h4, .serif-font {{
            font-family: 'Cormorant Garamond', serif;
            color: var(--text-white);
        }}
        .navbar {{
            background-color: rgba(10, 10, 10, 0.98);
            border-bottom: 1px solid #222;
        }}
        .logo-circle {{
            width: 45px;
            height: 45px;
            border: 1px solid var(--accent-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent-gold);
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.4rem;
        }}
        /* قائمة الموبايل والروابط */
        .offcanvas {{
            background-color: #0d0d0d !important;
            color: #ffffff;
            border-left: 1px solid #222;
        }}
        .nav-link-custom {{
            color: #ffffff;
            font-size: 1.25rem;
            padding: 12px 0;
            text-decoration: none;
            display: block;
            border-bottom: 1px solid #1a1a1a;
            transition: 0.3s;
        }}
        .nav-link-custom:hover {{
            color: var(--accent-gold);
            padding-left: 10px;
        }}
        .hero {{
            padding: 80px 20px 60px;
            text-align: center;
            background: linear-gradient(180deg, #111 0%, var(--bg-dark) 100%);
        }}
        .badge-gold {{
            color: var(--accent-gold);
            letter-spacing: 2px;
            font-size: 0.85rem;
            text-transform: uppercase;
            font-weight: 600;
        }}
        .btn-gold {{
            background-color: var(--accent-gold);
            color: #000;
            font-weight: 600;
            border-radius: 30px;
            padding: 14px 32px;
            letter-spacing: 1px;
            text-transform: uppercase;
            border: none;
            transition: 0.3s;
            text-decoration: none;
            display: inline-block;
        }}
        .btn-gold:hover {{
            background-color: #d4af66;
            color: #000;
            transform: translateY(-2px);
        }}
        .btn-outline-gold {{
            border: 1px solid var(--accent-gold);
            color: var(--text-white);
            font-weight: 500;
            border-radius: 30px;
            padding: 14px 32px;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-decoration: none;
            display: inline-block;
            transition: 0.3s;
        }}
        .btn-outline-gold:hover {{
            background-color: var(--accent-gold);
            color: #000;
        }}
        .price-box {{
            background-color: var(--card-bg);
            border: 1px solid var(--accent-gold);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 40px;
        }}
        .old-price {{
            text-decoration: line-through;
            color: #888888;
            font-size: 1.5rem;
            margin-right: 15px;
        }}
        .new-price {{
            color: var(--accent-gold);
            font-size: 2.8rem;
            font-weight: 700;
        }}
        .info-pill {{
            background: rgba(197, 160, 89, 0.15);
            border: 1px solid rgba(197, 160, 89, 0.4);
            color: var(--text-gold-light);
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.9rem;
            display: inline-block;
        }}
        .service-card {{
            background-color: var(--card-bg);
            border: 1px solid #2a2a2a;
            border-radius: 16px;
            overflow: hidden;
            margin-bottom: 30px;
            height: 100%;
        }}
        .service-card img {{
            width: 100%;
            height: 240px;
            object-fit: cover;
        }}
        .service-card-body {{
            padding: 25px;
        }}
        .service-list {{
            list-style: none;
            padding-left: 0;
            color: var(--text-white);
            font-size: 1rem;
        }}
        .service-list li {{
            margin-bottom: 12px;
            position: relative;
            padding-left: 20px;
            color: #ffffff;
        }}
        .service-list li::before {{
            content: "•";
            color: var(--accent-gold);
            position: absolute;
            left: 0;
            font-size: 1.4rem;
            top: -3px;
        }}
        .tag-badge {{
            background: #222;
            color: var(--text-white);
            border: 1px solid #444;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            display: inline-block;
            margin: 4px;
        }}
        .contact-box {{
            background-color: var(--card-bg);
            border: 1px solid #333;
            border-radius: 20px;
            padding: 35px;
        }}
        .contact-box p, .contact-box span, .contact-box a {{
            color: #ffffff !important;
        }}
        .float-whatsapp {{
            position: fixed;
            width: 60px;
            height: 60px;
            bottom: 30px;
            right: 30px;
            background-color: #25d366;
            color: #FFF;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
        }}
    </style>
</head>
<body>

    <!-- القائمة العلوية مع زر القائمة على اليمين -->
    <nav class="navbar navbar-dark sticky-top py-3">
        <div class="container d-flex justify-content-between align-items-center">
            <!-- الشعار على اليسار -->
            <a class="navbar-brand d-flex align-items-center gap-3" href="#">
                <div class="logo-circle">H</div>
                <div>
                    <div class="fw-bold fs-4" style="letter-spacing: 3px;">HEVO</div>
                    <div class="small" style="font-size: 0.65rem; letter-spacing: 2px; color: var(--accent-gold);">KOSMETIK AKADEMIE</div>
                </div>
            </a>

            <!-- زر فتح القائمة على اليمين -->
            <button class="navbar-toggler border-0 fs-2 text-white" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar">
                <i class="fas fa-bars" style="color: var(--text-white);"></i>
            </button>
        </div>
    </nav>

    <!-- قائمة الهواتف المنسدلة (Offcanvas) -->
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar">
        <div class="offcanvas-header border-bottom border-secondary py-3">
            <div class="d-flex align-items-center gap-2">
                <div class="logo-circle" style="width: 35px; height: 35px; font-size: 1.1rem;">H</div>
                <span class="fw-bold fs-5" style="letter-spacing: 2px; color: #fff;">HEVO</span>
            </div>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body d-flex flex-column justify-content-between py-4">
            <div class="nav flex-column">
                <a href="#behandlungen" class="nav-link-custom" data-bs-dismiss="offcanvas">Behandlungen</a>
                <a href="#akademie" class="nav-link-custom" data-bs-dismiss="offcanvas">Akademie</a>
                <a href="#ueber-uns" class="nav-link-custom" data-bs-dismiss="offcanvas">Über uns</a>
                <a href="#galerie" class="nav-link-custom" data-bs-dismiss="offcanvas">Galerie</a>
                <a href="#kontakt" class="nav-link-custom" data-bs-dismiss="offcanvas">Kontakt</a>
            </div>
            <div class="mt-4">
                <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20eine%20kostenlose%20Beratung%20vereinbaren" class="btn-gold w-100 text-center py-3">BERATUNG BUCHEN</a>
            </div>
        </div>
    </div>

    <!-- الواجهة الرئيسية -->
    <section class="hero">
        <div class="container">
            <span class="badge-gold d-block mb-2">DAKKS-ZERTIFIZIERTE BEAUTY-AKADEMIE KÖLN</span>
            <h1 class="display-4 my-3">Werde eine starke, <br><i class="serif-font" style="color: var(--accent-gold);">unabhängige Frau.</i></h1>
            <p class="mx-auto mb-4" style="max-width: 650px; color: #ffffff; font-size: 1.05rem;">
                Die erste DAkkS-zertifizierte Kosmetik-Akademie in Köln — Ausbildung und Behandlungen auf Deutsch, Arabisch und Kurdisch, unter ärztlicher Aufsicht.
            </p>
            <div class="d-flex justify-content-center gap-3 flex-wrap">
                <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20einen%20Termin%20vereinbaren" class="btn-gold">BEHANDLUNG BUCHEN</a>
                <a href="#akademie" class="btn-outline-gold">ZUR AKADEMIE</a>
            </div>
        </div>
    </section>

    <!-- قسم Über uns -->
    <section id="ueber-uns" class="container my-5 py-3">
        <div class="text-center mb-4">
            <span class="badge-gold">ÜBER UNS</span>
            <h2 class="display-4 serif-font mt-2">Warum HEVO Kosmetik?</h2>
        </div>
        <div class="row g-4 text-center text-md-start">
            <div class="col-md-3 col-6">
                <div class="p-3 border border-secondary rounded-3 h-100">
                    <i class="fas fa-certificate text-warning fs-2 mb-2"></i>
                    <h5 class="serif-font">DAkkS Zertifiziert</h5>
                    <p class="small text-muted mb-0">Höchste Ausbildungsstandards in Deutschland.</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="p-3 border border-secondary rounded-3 h-100">
                    <i class="fas fa-user-md text-warning fs-2 mb-2"></i>
                    <h5 class="serif-font">Ärztliche Aufsicht</h5>
                    <p class="small text-muted mb-0">Fachärztliche Begleitung bei allen Behandlungen.</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="p-3 border border-secondary rounded-3 h-100">
                    <i class="fas fa-language text-warning fs-2 mb-2"></i>
                    <h5 class="serif-font">3 Sprachen</h5>
                    <p class="small text-muted mb-0">Unterricht auf Deutsch, Arabisch & Kurdisch.</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="p-3 border border-secondary rounded-3 h-100">
                    <i class="fas fa-award text-warning fs-2 mb-2"></i>
                    <h5 class="serif-font">FachDozentin</h5>
                    <p class="small text-muted mb-0">Offiziell anerkannte Expertise und Zertifikate.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- قسم الأكاديمية (Akademie) -->
    <section id="akademie" class="container my-5 pt-4">
        <div class="text-center mb-4">
            <span class="badge-gold">DIE AKADEMIE</span>
            <h2 class="display-4 serif-font mt-2">Fachkosmetik-Ausbildung</h2>
        </div>

        <div class="price-box">
            <div class="row align-items-center text-center text-md-start">
                <div class="col-md-7 mb-4 mb-md-0">
                    <div class="mb-2">
                        <span class="old-price">10.000 €</span>
                        <span class="new-price serif-font">7.000 €</span>
                    </div>
                    <p class="text-warning mb-3" style="font-size: 1rem;"><i class="fas fa-clock me-1"></i> Begrenztes Angebot · Ratenzahlung 500 – 1.000 €/Monat möglich</p>
                    <div class="d-flex flex-wrap gap-2 mb-3">
                        <span class="info-pill"><i class="fas fa-calendar-alt me-1"></i> START: AUGUST 2026</span>
                        <span class="info-pill"><i class="fas fa-clock me-1"></i> DAUER: 6 Monate (Theorie + Praxis) · Intensiv: 2 Monate</span>
                        <span class="info-pill"><i class="fas fa-language me-1"></i> SPRACHEN: Deutsch · Arabisch · Kurdisch</span>
                        <span class="info-pill"><i class="fas fa-user-clock me-1"></i> TERMINE: 2× pro Woche</span>
                    </div>
                    <p class="mb-0" style="color: #ffffff;"><strong>ABSCHLUSS:</strong> Mehrere anerkannte Zertifikate</p>
                </div>
                <div class="col-md-5 text-center">
                    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20mich%20für%20die%20Fachkosmetik-Ausbildung%20anmelden" class="btn-gold btn-lg w-100 py-3">JETZT ANMELDEN</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            <div class="col-md-6">
                <div class="service-card p-4">
                    <h3 class="serif-font fs-2 mb-3" style="color: var(--accent-gold);"><i class="fas fa-book me-2"></i>Theorie</h3>
                    <ul class="service-list">
                        <li>Geräte & Hygiene</li>
                        <li>Kundenberatung & Hautanalyse</li>
                        <li>Hautaufbau & Hauttypen</li>
                        <li>Hautkrankheiten</li>
                        <li>Wie du dein eigenes Studio eröffnest</li>
                    </ul>
                </div>
            </div>

            <div class="col-md-6">
                <div class="service-card p-4">
                    <h3 class="serif-font fs-2 mb-3" style="color: var(--accent-gold);"><i class="fas fa-hands me-2"></i>Praxis</h3>
                    <ul class="service-list">
                        <li>Manuelle Reinigung</li>
                        <li>Diamantpeeling & Dermapen</li>
                        <li>Massage</li>
                        <li>Wimpern- & Brauenfärben</li>
                        <li>Make-up & Hautanalyse</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="service-card p-4 mt-4">
            <span class="badge-gold">GESCHENK-ZERTIFIKATE</span>
            <p class="mt-2 mb-3" style="color: #ffffff;">Diese zusätzlichen Techniken sind als zertifizierte Bonus-Module inklusive:</p>
            <div>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Wimpernlifting</span>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Augenbrauenlaminierung</span>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Sauerstoff-Technik</span>
            </div>
        </div>
    </section>

    <!-- قسم Behandlungen & Galerie -->
    <section id="behandlungen" class="container my-5 pt-4">
        <div id="galerie" class="text-center mb-5">
            <span class="badge-gold">BEHANDLUNGEN & GALERIE</span>
            <h2 class="display-4 serif-font mt-2">Sichtbare Ergebnisse, <br><i style="color: var(--accent-gold);">spürbare Pflege</i></h2>
        </div>
        <div class="row g-4">
            <div class="col-md-6">
                <div class="service-card">
                    <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80" alt="Gesicht">
                    <div class="service-card-body">
                        <h3 class="serif-font fs-2" style="color: var(--accent-gold);">Gesicht & Haut</h3>
                        <ul class="service-list mt-3">
                            <li>Tiefenreinigung & Hydrafacial</li>
                            <li>Dermapen / Microneedling & BB Glow</li>
                            <li>Diamantpeeling & Fruchtsäure-Peeling</li>
                            <li>Sauerstoff-Behandlung & GREEN PEEL®</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="service-card">
                    <img src="https://images.unsplash.com/photo-1512290900673-7002012d22b2?auto=format&fit=crop&w=800&q=80" alt="Laser">
                    <div class="service-card-body">
                        <h3 class="serif-font fs-2" style="color: var(--accent-gold);">Laser & Anti-Aging</h3>
                        <ul class="service-list mt-3">
                            <li>CO2-Laser (Hauterneuerung)</li>
                            <li>Plasma Pen (Lifting ohne OP)</li>
                            <li>Dauerhafte Haarentfernung</li>
                            <li>Body Sculpting</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- قسم Kontakt -->
    <section id="kontakt" class="container my-5 pt-4">
        <div class="contact-box">
            <span class="badge-gold d-block mb-2">KONTAKT</span>
            <h2 class="serif-font fs-1 mb-4" style="color: var(--accent-gold);">Besuche uns in Köln</h2>
            <p class="mb-4" style="font-size: 1.05rem;">
                Vereinbare eine kostenlose Beratung — für eine Behandlung oder für die Ausbildung. Wir beraten dich gern auf Deutsch, Arabisch oder Kurdisch.
            </p>

            <div class="row g-4">
                <div class="col-md-6">
                    <div class="d-flex align-items-start gap-3 mb-3">
                        <i class="fas fa-map-marker-alt fs-4 text-warning mt-1"></i>
                        <div>
                            <span class="badge-gold d-block" style="font-size: 0.75rem;">ADRESSE</span>
                            <strong>Berliner Straße 368, 51061 Köln</strong>
                        </div>
                    </div>

                    <div class="d-flex align-items-start gap-3 mb-3">
                        <i class="fas fa-phone-alt fs-4 text-warning mt-1"></i>
                        <div>
                            <span class="badge-gold d-block" style="font-size: 0.75rem;">TELEFON / WHATSAPP</span>
                            <a href="tel:{PHONE_NUMBER}" class="text-decoration-none fw-bold" style="font-size: 1.1rem;">0173 9125695</a>
                        </div>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="d-flex align-items-start gap-3 mb-3">
                        <i class="fas fa-clock fs-4 text-warning mt-1"></i>
                        <div>
                            <span class="badge-gold d-block" style="font-
