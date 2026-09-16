from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات التواصل
PHONE_NUMBER = "+491729887745"
WHATSAPP_NUMBER = "491729887745"

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
            --text-light: #f5f5f5;
            --text-muted: #a0a0a0;
        }}
        body {{
            background-color: var(--bg-dark);
            color: var(--text-light);
            font-family: 'Montserrat', sans-serif;
        }}
        h1, h2, h3, h4, .serif-font {{
            font-family: 'Cormorant Garamond', serif;
        }}
        .navbar {{
            background-color: rgba(10, 10, 10, 0.95);
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
        .hero {{
            padding: 70px 20px 50px;
            text-align: center;
            background: linear-gradient(180deg, #111 0%, var(--bg-dark) 100%);
        }}
        .badge-gold {{
            color: var(--accent-gold);
            letter-spacing: 2px;
            font-size: 0.8rem;
            text-transform: uppercase;
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
            color: var(--text-light);
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
            color: var(--text-muted);
            font-size: 1.5rem;
            margin-right: 15px;
        }}
        .new-price {{
            color: var(--accent-gold);
            font-size: 2.8rem;
            font-weight: 700;
        }}
        .info-pill {{
            background: rgba(197, 160, 89, 0.1);
            border: 1px solid rgba(197, 160, 89, 0.3);
            color: var(--accent-gold);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            display: inline-block;
        }}
        .service-card {{
            background-color: var(--card-bg);
            border: 1px solid #222;
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
            color: var(--text-muted);
            font-size: 0.95rem;
        }}
        .service-list li {{
            margin-bottom: 10px;
            position: relative;
            padding-left: 18px;
        }}
        .service-list li::before {{
            content: "•";
            color: var(--accent-gold);
            position: absolute;
            left: 0;
            font-size: 1.2rem;
        }}
        .tag-badge {{
            background: #222;
            color: var(--text-light);
            border: 1px solid #333;
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            display: inline-block;
            margin: 4px;
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
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
        }}
    </style>
</head>
<body>

    <!-- الهيدر واللوجو -->
    <nav class="navbar navbar-dark sticky-top py-3">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center gap-3" href="#">
                <div class="logo-circle">H</div>
                <div>
                    <div class="fw-bold fs-4" style="letter-spacing: 3px;">HEVO</div>
                    <div class="small text-muted" style="font-size: 0.65rem; letter-spacing: 2px;">KOSMETIK AKADEMIE</div>
                </div>
            </a>
        </div>
    </nav>

    <!-- الهيرو الرئيسي -->
    <section class="hero">
        <div class="container">
            <span class="badge-gold d-block mb-2">DAKKS-ZERTIFIZIERTE BEAUTY-AKADEMIE KÖLN</span>
            <h1 class="display-4 my-3">Werde eine starke, <br><i class="serif-font" style="color: var(--accent-gold);">unabhängige Frau.</i></h1>
            <p class="text-muted mx-auto mb-4" style="max-width: 650px;">
                Die erste DAkkS-zertifizierte Kosmetik-Akademie in Köln — Ausbildung und Behandlungen auf Deutsch, Arabisch und Kurdisch, unter ärztlicher Aufsicht.
            </p>
            <div class="d-flex justify-content-center gap-3 flex-wrap">
                <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20einen%20Termin%20vereinbaren" class="btn-gold">BEHANDLUNG BUCHEN</a>
                <a href="#akademie-preis" class="btn-outline-gold">ZUR AKADEMIE</a>
            </div>
        </div>
    </section>

    <!-- قسم الأكاديمية والأسعار الجديدة (من الصور الأخيرة) -->
    <section id="akademie-preis" class="container my-5">
        <div class="text-center mb-4">
            <span class="badge-gold">DIE AKADEMIE</span>
            <h2 class="display-4 serif-font mt-2">Fachkosmetik-Ausbildung</h2>
        </div>

        <!-- بطاقة السعر والتفاصيل -->
        <div class="price-box">
            <div class="row align-items-center text-center text-md-start">
                <div class="col-md-7 mb-4 mb-md-0">
                    <div class="mb-2">
                        <span class="old-price">10.000 €</span>
                        <span class="new-price serif-font">7.000 €</span>
                    </div>
                    <p class="text-warning mb-3"><i class="fas fa-clock me-1"></i> Begrenztes Angebot · Ratenzahlung 500 – 1.000 €/Monat möglich</p>
                    <div class="d-flex flex-wrap gap-2 mb-3">
                        <span class="info-pill"><i class="fas fa-calendar-alt me-1"></i> START: AUGUST 2026</span>
                        <span class="info-pill"><i class="fas fa-clock me-1"></i> DAUER: 6 Monate (Theorie + Praxis) · Intensiv: 2 Monate</span>
                        <span class="info-pill"><i class="fas fa-language me-1"></i> SPRACHEN: Deutsch · Arabisch · Kurdisch</span>
                        <span class="info-pill"><i class="fas fa-user-clock me-1"></i> TERMINE: 2× pro Woche (werktags oder Wochenende)</span>
                    </div>
                    <p class="text-muted mb-0"><strong>ABSCHLUSS:</strong> Mehrere anerkannte Zertifikate</p>
                </div>
                <div class="col-md-5 text-center">
                    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20mich%20für%20die%20Fachkosmetik-Ausbildung%20anmelden" class="btn-gold btn-lg w-100 py-3">JETZT ANMELDEN</a>
                </div>
            </div>
        </div>

        <!-- محاور النظرية والعملي (Theorie & Praxis) -->
        <div class="row g-4">
            <!-- النظرية (Theorie) -->
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

            <!-- العملي (Praxis) -->
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

        <!-- البونص والشهادات الإضافية -->
        <div class="service-card p-4 mt-4">
            <span class="badge-gold">GESCHENK-ZERTIFIKATE</span>
            <p class="text-muted mt-2 mb-3">Diese zusätzlichen Techniken sind als zertifizierte Bonus-Module inklusive:</p>
            <div>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Wimpernlifting</span>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Augenbrauenlaminierung</span>
                <span class="tag-badge"><i class="fas fa-check text-warning me-1"></i> Sauerstoff-Technik</span>
            </div>
        </div>
    </section>

    <!-- باقي الخدمات والفروع -->
    <section class="container my-5 py-4">
        <div class="text-center mb-5">
            <h2 class="display-4 serif-font">Sichtbare Ergebnisse, <br><i style="color: var(--accent-gold);">spürbare Pflege</i></h2>
        </div>
        <div class="row g-4">
            <div class="col-md-6">
                <div class="service-card">
                    <img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=800&q=80" alt="Gesicht">
                    <div class="service-card-body">
                        <h3 class="serif-font fs-2">Gesicht & Haut</h3>
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
                        <h3 class="serif-font fs-2">Laser & Anti-Aging</h3>
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

    <!-- الفوتر والتواصل -->
    <footer class="text-center py-5" style="border-top: 1px solid #222;">
        <div class="container">
            <h3 class="serif-font fs-2 mb-3">HEVO KOSMETIK AKADEMIE</h3>
            <p class="text-muted mb-2"><i class="fas fa-map-marker-alt text-warning me-2"></i>Berliner Str. 368, 51061 Köln</p>
            <p class="text-muted mb-4"><i class="fas fa-phone-alt text-warning me-2"></i>{PHONE_NUMBER}</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="btn-gold mb-4">TERMIN ANFRAGEN</a>
            <p class="small text-muted mb-0">&copy; HEVO Kosmetik Akademie Köln. Alle Rechte vorbehalten.</p>
        </div>
    </footer>

    <!-- زر الواتساب العائم -->
    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo,%20ich%20möchte%20einen%20Termin%20vereinbaren" class="float-whatsapp" target="_blank" title="WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
