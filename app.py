from flask import Flask, render_template_string

app = Flask(__name__)

# رقم الواتساب المباشر بالأكاديمية (491729887745)
WHATSAPP_NUMBER = "491729887745"

HTML_LAYOUT = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEVO Kosmetik - Akademie & Beauty Salon</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #faf5f6; color: #333; }}
        .hero {{ background: linear-gradient(135deg, #f8cdda 0%, #1d2671 100%); color: white; padding: 70px 20px; border-bottom-left-radius: 40px; border-bottom-right-radius: 40px; text-align: center; }}
        .btn-whatsapp {{ background-color: #25D366; color: white; border-radius: 30px; font-weight: bold; padding: 12px 30px; transition: 0.3s; text-decoration: none; display: inline-block; }}
        .btn-whatsapp:hover {{ background-color: #1ebc57; color: white; transform: scale(1.05); }}
        .card {{ border: none; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: 0.3s; background: white; }}
        .card:hover {{ transform: translateY(-5px); }}
        .float-whatsapp {{ position: fixed; width: 60px; height: 60px; bottom: 30px; right: 30px; background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center; font-size: 30px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); z-index: 1000; display: flex; align-items: center; justify-content: center; text-decoration: none; }}
        .float-whatsapp:hover {{ color: #FFF; background-color: #20ba5a; }}
        .info-box {{ background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #1d2671; margin-top: 30px; }}
    </style>
</head>
<body>

    <header class="hero">
        <div class="container">
            <h1 class="display-4 fw-bold">HEVO Kosmetik</h1>
            <p class="lead fs-4">Akademie & Beauty Salon · Köln</p>
            <p class="mb-4">Ihre Experten für Ästhetik, Schönheit & professionelle Schulungen</p>
            <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo%20HEVO%20Kosmetik,%20ich%20möchte%20einen%20Termin%20vereinbaren." target="_blank" class="btn btn-whatsapp btn-lg">
                <i class="fab fa-whatsapp me-2"></i>Jetzt per WhatsApp buchen
            </a>
        </div>
    </header>

    <section class="container my-5">
        <div class="row text-center mb-4">
            <div class="col-md-6 mb-4">
                <div class="card p-4 h-100">
                    <i class="fas fa-graduation-cap fa-3x text-danger mb-3"></i>
                    <h3 class="h4">Kosmetik Akademie</h3>
                    <p class="text-muted">Professionelle Ausbildungen und Zertifikatskurse im Bereich Kosmetik & Ästhetik in Köln.</p>
                </div>
            </div>
            <div class="col-md-6 mb-4">
                <div class="card p-4 h-100">
                    <i class="fas fa-sparkles fa-3x text-danger mb-3"></i>
                    <h3 class="h4">Beauty Salon</h3>
                    <p class="text-muted">Erstklassige Gesichtsbehandlungen, Permanent Make-up und ästhetische Pflege.</p>
                </div>
            </div>
        </div>

        <div class="info-box">
            <h4 class="fw-bold"><i class="fas fa-map-marker-alt text-danger me-2"></i>Adresse & Kontakt</h4>
            <p class="mb-1"><strong>Adresse:</strong> Berliner Str. 368, 51061 Köln</p>
            <p class="mb-0"><strong>Telefon / WhatsApp:</strong> +49 172 9887745</p>
        </div>
    </section>

    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hallo%20HEVO%20Kosmetik,%20ich%20möchte%20einen%20Termin%20vereinbaren." class="float-whatsapp" target="_blank" title="WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

    <footer class="bg-dark text-white text-center py-3 mt-5">
        <p class="mb-0">&copy; HEVO Kosmetik Akademie & Beauty Salon Köln</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

