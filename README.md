# RepliQuotes web sitesi

Statik site: tanitim sayfasi, destek ve gizlilik politikasi. GitHub Pages ile yayinlanir.

| Yol | Icerik |
|-----|--------|
| `/` | Tanitim sayfasi |
| `/destek/` | Destek ve SSS (TR + EN) |
| `/gizlilik/` | Gizlilik politikasi (TR + EN) |
| `/support/`, `/privacy/` | Ingilizce kisayollar, TR sayfalarin `#en` bolumune yonlendirir |

Alan adi baglamak: kok dizine alan adini iceren bir `CNAME` dosyasi eklenir,
alan adi saglayicisinda GitHub Pages DNS kayitlari tanimlanir.

Sayfalar `_kaynak/site_olustur.py` ile uretilir (ust menu ve alt bilgi tek yerde):
`python3 _kaynak/site_olustur.py`. Ana sayfa metni `_kaynak/site_anasayfa_govde.html`,
destek ve gizlilik metinleri `_kaynak/eski/` altindaki dosyalardir.
`_` ile baslayan klasor GitHub Pages'te yayinlanmaz.
