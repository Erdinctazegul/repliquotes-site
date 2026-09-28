"""repliquotes-site sayfalarini ortak ust menu + alt bilgi ile uretir.

Destek ve gizlilik metinleri eski GitHub Pages sayfalarindan (eski-site/)
AYNEN alinir; yalnizca yeni tasarima yerlestirilir.
"""
import os, re

S = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(S)
ESKI = os.path.join(S, "eski")
MAIL = "repliquotes.destek@gmail.com"

IK = {
    "destek": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.3 2.4c-.5.2-.8.6-.8 1.1v.5"/><path d="M12 16.5h.01"/></svg>',
    "kalkan": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.7-7 9-4-1.3-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "posta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg>',
    "cop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16"/><path d="M9 7V4h6v3"/><path d="M6 7l1 13h10l1-13"/><path d="M10 11v6M14 11v6"/></svg>',
    "bayrak": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/></svg>',
    "reklamsiz": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/></svg>',
    "ara": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "apple": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.63c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.62-1.7-3.19-1.72-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.74 2.21 1.1-.04 1.51-.71 2.84-.71 1.33 0 1.7.71 2.86.69 1.18-.02 1.93-1.08 2.65-2.14.84-1.23 1.18-2.42 1.2-2.48-.03-.01-2.3-.88-2.32-3.5zM14.2 6.17c.61-.74 1.02-1.76.9-2.78-.88.04-1.94.58-2.57 1.32-.56.65-1.06 1.7-.93 2.7.98.08 1.99-.5 2.6-1.24z"/></svg>',
    "play": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#34A853" d="M3.6 2.3 13.4 12 3.6 21.7c-.4-.2-.6-.6-.6-1.1V3.4c0-.5.2-.9.6-1.1z"/><path fill="#FBBC04" d="M16.8 8.6 13.4 12l3.4 3.4 3.9-2.2c.7-.4.7-1.4 0-1.8z"/><path fill="#4285F4" d="M3.6 2.3c.3-.2.8-.2 1.2 0l12 6.3-3.4 3.4z"/><path fill="#EA4335" d="M13.4 12l3.4 3.4-12 6.3c-.4.2-.9.2-1.2 0z"/></svg>',
}

MAGAZALAR = f'''<div class="magazalar">
        <a class="magaza" href="#indir" aria-label="App Store'da yakında">{IK["apple"]}<span><small>Yakında</small><strong>App Store</strong></span></a>
        <a class="magaza" href="#indir" aria-label="Google Play'de yakında">{IK["play"]}<span><small>Yakında</small><strong>Google Play</strong></span></a>
      </div>'''


def bas(baslik, aciklama, p, aktif=None, og=False):
    """<head> + ust cubuk. p: kok dizine goreli onek ("" ya da "../")."""
    ogm = ""
    if og:
        ogm = f'''<meta property="og:type" content="website">
<meta property="og:title" content="RepliQuotes · Aklındaki repliği anında bul">
<meta property="og:description" content="Film ve dizi repliklerini ara, yapım yapım keşfet, kendi listeni oluştur, oyna ve paylaş.">
<meta property="og:image" content="img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
'''
    def nav(ad, yol, ik, etiket):
        cls = "nav-dugme aktif" if aktif == ad else "nav-dugme"
        cur = ' aria-current="page"' if aktif == ad else ""
        return f'<a class="{cls}" href="{p}{yol}"{cur}>{IK[ik]}{etiket}</a>'
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{baslik}</title>
<meta name="description" content="{aciklama}">
<meta name="theme-color" content="#0B0B0D">
<link rel="icon" type="image/png" href="{p}favicon.png">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
{ogm}<link rel="stylesheet" href="{p}assets/site.css">
</head>
<body>

<header class="ust">
  <div class="kap">
    <a class="logo" href="{p or './'}" aria-label="RepliQuotes ana sayfa">
      <img src="{p}img/ikon.png" alt="">
      <span class="marka">REPLI<span>QUOTES</span></span>
    </a>
    <nav class="menu" aria-label="Ana menü">
      <a class="yazi" href="{p}#ozellikler">Özellikler</a>
      {nav("destek", "destek/", "destek", "Destek")}
      {nav("gizlilik", "gizlilik/", "kalkan", "Gizlilik")}
    </nav>
  </div>
</header>
'''


def alt(p):
    return f'''
<footer>
  <div class="kap">
    <div>
      <a class="logo" href="{p or './'}"><img src="{p}img/ikon.png" alt=""><span class="marka">REPLI<span>QUOTES</span></span></a>
      <p>Film ve dizi repliklerini bul, biriktir, oyna ve paylaş.</p>
    </div>
    <div>
      <h4>Uygulama</h4>
      <ul>
        <li><a href="{p}#ozellikler">Özellikler</a></li>
        <li><a href="{p}#oyunlar">Oyunlar</a></li>
        <li><a href="{p}#indir">İndir</a></li>
      </ul>
    </div>
    <div>
      <h4>Yardım</h4>
      <ul>
        <li><a href="{p}destek/">Destek</a></li>
        <li><a href="{p}gizlilik/">Gizlilik Politikası</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
      </ul>
    </div>
    <div class="kaynak">
      Bu ürün TMDB API'sini kullanır ancak TMDB tarafından desteklenmemekte veya onaylanmamaktadır. Replikler film ve dizi altyazılarından (OpenSubtitles.com) alınır.<br>
      © 2026 Erdinç Tazegül. App Store, Apple Inc.'in; Google Play, Google LLC'nin ticari markasıdır.
    </div>
  </div>
</footer>
'''


# TR / EN secimi: JS yoksa iki dil de gorunur (hic bir sey saklanmaz).
DIL_JS = '''<script>
(function () {
  var bolumler = document.querySelectorAll('[data-dil]');
  var dugmeler = document.querySelectorAll('.dil-sec button');
  function goster(dil) {
    bolumler.forEach(function (b) { b.hidden = b.getAttribute('data-dil') !== dil; });
    dugmeler.forEach(function (d) { d.setAttribute('aria-pressed', d.value === dil ? 'true' : 'false'); });
    document.documentElement.lang = dil;
  }
  dugmeler.forEach(function (d) {
    d.addEventListener('click', function () {
      goster(d.value);
      history.replaceState(null, '', d.value === 'en' ? '#en' : location.pathname);
    });
  });
  goster(location.hash === '#en' ? 'en' : 'tr');
})();
</script>'''


def dil_sec():
    return '''<div class="dil-sec" role="group" aria-label="Dil">
          <button type="button" value="tr" aria-pressed="true">Türkçe</button>
          <button type="button" value="en" aria-pressed="false">English</button>
        </div>'''


def bolum_al(html, kimlik):
    m = re.search(rf'<section id="{kimlik}"[^>]*>(.*?)</section>', html, re.S)
    return m.group(1)


def temizle_ust(icerik):
    """EN bolumunun basindaki tekrar eden h1 + tarih satirini atar."""
    icerik = re.sub(r'<h1>.*?</h1>\s*', '', icerik, flags=re.S)
    icerik = re.sub(r'<p class="soluk">(Son güncelleme|Last updated)[^<]*</p>\s*', '', icerik)
    return icerik.strip()


# ─── Destek ────────────────────────────────────────────────────────────
def destek():
    eski = open(os.path.join(ESKI, "destek.html"), encoding="utf-8").read()
    eski = eski.replace('href="../"', 'href="../gizlilik/"')

    def cevir(dil):
        ic = temizle_ust(bolum_al(eski, dil))
        kart = re.search(r'<div class="kart">.*?</div>', ic, re.S).group(0)
        span = re.search(r'<span class="soluk">(.*?)</span>', kart, re.S).group(1)
        sorular = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', ic, re.S)
        baslik = "Bize ulaş" if dil == "tr" else "Contact us"
        yaz = "E-posta gönder" if dil == "tr" else "Send email"
        sss = "Sık sorulan sorular" if dil == "tr" else "Frequently asked questions"
        acik = ' open' # ilk soru acik gelsin
        items = []
        for i, (s, c) in enumerate(sorular):
            items.append(f'<details{acik if i == 0 else ""}><summary>{s}</summary><p>{c}</p></details>')
        return f'''<div data-dil="{dil}"{' lang="en"' if dil == "en" else ""}>
        <div class="iletisim">
          <div class="ik">{IK["posta"]}</div>
          <div><b>{baslik}</b><span>{span}</span></div>
          <a class="dugme ana" href="mailto:{MAIL}">{yaz}</a>
        </div>
        <h2 class="sss-baslik">{sss}</h2>
        <div class="sss">
          {chr(10).join(items)}
        </div>
      </div>'''

    govde = f'''
<main>
  <section class="sayfa-bas">
    <div class="kap">
      <div class="yol"><a href="../">Ana sayfa</a> / Destek</div>
      <h1>Destek</h1>
      <p class="ozet-yazi">Bir sorun mu var ya da bir önerin mi? Aşağıda en çok sorulan soruların cevapları var; bulamazsan bize yaz, genellikle 2 iş günü içinde dönüyoruz.</p>
      <div class="bas-alt">
        {dil_sec()}
        <span class="tarih">Son güncelleme: 28 Eylül 2026</span>
      </div>
      <div class="hizli">
        <a href="mailto:{MAIL}"><span class="ik">{IK["posta"]}</span><b>Bize yaz</b><span>{MAIL}</span></a>
        <a href="../gizlilik/#tr-6"><span class="ik">{IK["cop"]}</span><b>Hesabımı sil</b><span>Profil → Hesabımı Sil. Kalıcıdır, tüm verilerin silinir.</span></a>
        <a href="../gizlilik/"><span class="ik">{IK["kalkan"]}</span><b>Gizlilik politikası</b><span>Hangi verileri neden topladığımızı oku.</span></a>
      </div>
    </div>
  </section>

  <section class="belge">
    <div class="kap">
      <div class="izgara tek">
      {cevir("tr")}
      {cevir("en")}
      </div>
    </div>
  </section>
</main>
'''
    return bas("Destek · RepliQuotes", "RepliQuotes uygulaması için destek, sık sorulan sorular ve iletişim.", "../", "destek") + govde + alt("../") + DIL_JS + "\n</body>\n</html>\n"


def etiketle(html):
    """Tablo hucrelerine sutun adini yazar; dar ekranda satirlar kart olur."""
    def tablo(m):
        t = m.group(0)
        basliklar = re.findall(r'<th[^>]*>(.*?)</th>', t, re.S)
        def satir(r):
            hucreler = iter(basliklar)
            return re.sub(r'<td>', lambda _: f'<td data-etiket="{next(hucreler, "")}">', r.group(0))
        return re.sub(r'<tr>(?:(?!</tr>).)*<td>.*?</tr>', satir, t, flags=re.S)
    return re.sub(r'<table>.*?</table>', tablo, html, flags=re.S)


# ─── Gizlilik ──────────────────────────────────────────────────────────
def gizlilik():
    eski = open(os.path.join(ESKI, "gizlilik.html"), encoding="utf-8").read()
    eski = eski.replace('href="destek/"', 'href="../destek/"')

    def cevir(dil):
        ic = temizle_ust(bolum_al(eski, dil))
        giris = re.match(r'\s*(<p>.*?</p>)', ic, re.S).group(1)
        ozet = re.search(r'<div class="kart">\s*<strong>[^<]*</strong>\s*<ul>(.*?)</ul>\s*</div>', ic, re.S)
        maddeler = re.findall(r'<li>(.*?)</li>', ozet.group(1), re.S)
        ikonlar = [IK["reklamsiz"], IK["ara"], IK["cop"]]
        kartlar = "".join(f'<div><span class="ik">{ikonlar[i % 3]}</span>{m}</div>' for i, m in enumerate(maddeler))
        # Numarali basliklari kartlara bol.
        parcalar = re.split(r'<h2>(.*?)</h2>', ic[ozet.end():], flags=re.S)
        bolumler, toc = [], []
        for i in range(1, len(parcalar), 2):
            h = parcalar[i].strip()
            m = re.match(r'(\d+)\.\s*(.*)', h)
            no, ad = m.group(1), m.group(2)
            kimlik = f"{dil}-{no}"
            toc.append(f'<li><a href="#{kimlik}">{no}. {ad}</a></li>')
            icerik = parcalar[i + 1].strip()
            icerik = etiketle(icerik)
            bolumler.append(f'<section class="bolum" id="{kimlik}"><h2><span class="n">{no.zfill(2)}</span>{ad}</h2>\n{icerik}\n</section>')
        return f'''<div data-dil="{dil}"{' lang="en"' if dil == "en" else ""}>
        <div class="izgara">
          <aside class="icindekiler"><b>{"İçindekiler" if dil == "tr" else "Contents"}</b><ol>{"".join(toc)}</ol></aside>
          <div class="yazi-alani">
            {giris}
            <div class="ozet-kartlar">{kartlar}</div>
            {chr(10).join(bolumler)}
          </div>
        </div>
      </div>'''

    govde = f'''
<main>
  <section class="sayfa-bas">
    <div class="kap">
      <div class="yol"><a href="../">Ana sayfa</a> / Gizlilik</div>
      <h1>Gizlilik Politikası</h1>
      <p class="ozet-yazi">Hangi verileri topladığımızı, neden topladığımızı, kimlerle paylaştığımızı ve verilerini nasıl silebileceğini açıkça anlatıyoruz.</p>
      <div class="bas-alt">
        {dil_sec()}
        <span class="tarih">Son güncelleme: 28 Eylül 2026</span>
      </div>
    </div>
  </section>

  <section class="belge">
    <div class="kap">
      {cevir("tr")}
      {cevir("en")}
    </div>
  </section>
</main>
'''
    return bas("Gizlilik Politikası · RepliQuotes", "RepliQuotes gizlilik politikası: toplanan veriler, kullanım amaçları, paylaşılan hizmetler ve hesap silme.", "../", "gizlilik") + govde + alt("../") + DIL_JS + "\n</body>\n</html>\n"


if __name__ == "__main__":
    for ad, fn in (("destek", destek), ("gizlilik", gizlilik)):
        os.makedirs(os.path.join(W, ad), exist_ok=True)
        open(os.path.join(W, ad, "index.html"), "w", encoding="utf-8").write(fn())
    # Ana sayfa: govde ayri dosyada, bas/alt buradan.
    govde = open(os.path.join(S, "site_anasayfa_govde.html"), encoding="utf-8").read()
    govde = govde.replace("{{MAGAZALAR}}", MAGAZALAR)

    # Ekran goruntuleri: 720 px + 1080 px (@2x). Retina/3x ekranda tarayici
    # buyugunu secer; boylece telefonlarda bulaniklik olmaz. Genislik/yukseklik
    # yazilir ki gorsel yuklenirken sayfa kaymasin.
    from PIL import Image
    ilk = {"kesfet", "arama"}  # giris bolumundekiler hemen yuklenir
    goruldu = set()
    def img(m):
        ad, alt_ = m.group(1), m.group(2)
        w, h = Image.open(os.path.join(W, "img", ad + ".webp")).size
        tembel = "" if (ad in ilk and ad not in goruldu) else ' loading="lazy"'
        goruldu.add(ad)
        return (f'<img src="img/{ad}.webp" srcset="img/{ad}.webp 720w, img/{ad}@2x.webp 1080w" '
                f'sizes="(max-width: 560px) 46vw, 300px" alt="{alt_}" width="{w}" height="{h}" decoding="async"{tembel}>')
    govde = re.sub(r'\{\{IMG (\w+) "([^"]*)"\}\}', img, govde)
    ana = bas("RepliQuotes · Film ve dizi repliklerini bul, oyna, paylaş",
              "Aklındaki repliği saniyeler içinde bul. Film ve dizilerden yüz binlerce replik, yapım sayfaları, kendi replik listelerin, 4 oyun ve Makara ile anında rakip.",
              "", None, og=True) + govde + alt("") + "\n</body>\n</html>\n"
    open(os.path.join(W, "index.html"), "w", encoding="utf-8").write(ana)
    print("tamam")
