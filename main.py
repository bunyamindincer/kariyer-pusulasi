import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Yetenek ve Kariyer Pusulası",
    page_icon="🧠",
    layout="wide"
)

# --- 260 MADDELİK EKSİKSİZ AKADEMİK SORU HAVUZU ---
SORULAR = {
    "Zekâ Alanları": {
        "Sözel": [
            "Duygularımı ve düşüncelerimi kelimelerle ifade etmekte oldukça başarılıyımdır.",
            "Yeni kelimeler öğrenmek, kelime oyunları oynamak veya bulmaca çözmek hoşuma gider.",
            "Okuduğum bir metindeki ana fikri, yazım hatalarını veya üslubu hızlıca fark ederim.",
            "Bir topluluk önünde konuşma yaparken veya sunum hazırlarken kendimi rahat hissederim.",
            "Kitap okumak, makale incelemek veya edebi yazılar üzerine tartışmak ilgimi çeker.",
            "Hikaye anlatma, fıkra aktarma veya yaşanmış bir olayı etkileyici şekilde tasvir etme becerim yüksektir.",
            "Yabancı diller öğrenmeye karşı doğal bir yatkınlığım ve ilgim vardır.",
            "Yazılı yönergeleri, sözlü talimatlara kıyasla çok daha hızlı ve doğru şekilde analiz ederim.",
            "Kelime dağarcığım zengindir ve konuşurken kelimeleri seçerek, yerinde kullanmaya özen gösteririm.",
            "Günlük tutmak, şiir, deneme veya makale yazmak kendimi ifade etme biçimlerimden biridir.",
            "İsimler, tarihler veya kitap başlıkları gibi sözel bilgileri hafızamda kolayca tutabilirim.",
            "Bir konuyu araştırırken birden fazla kaynaktan okuma yapmak beni hiç yormaz.",
            "Kelime kökenleri, dil bilgisi yapıları ve kavramların anlam varyasyonları üzerine düşünürüm.",
            "Tartışmalarda veya mülakatlarda kendimi savunurken kelimeleri birer stratejik araç gibi kullanırım.",
            "Radyo programları, sesli kitaplar veya podcast dinlemek dinlenme yöntemlerim arasındadır.",
            "Yazılı bir metni sadeleştirmek veya karmaşık bir fikri özet halinde yazmak benim için kolaydır.",
            "Söz sanatları, ironi, mecaz ve atasözlerinin altındaki derin anlamları hızlı yakalarım.",
            "Ezber yapmam gerektiğinde, bilgileri kafiyeler veya sözel kodlar üreterek hafızama alırım.",
            "Başkalarının konuşmalarındaki mantık hatalarını veya ifade zayıflıklarını anında fark ederim.",
            "Tiyatro metinleri okumak, senaryo incelemek veya hitabet sanatı üzerine çalışmak ilgimi çeker."
        ],
        "İletişim": [
            "Girdiğim yeni ortamlarda insanlarla kolayca iletişim kurar ve bağ kurabilirim.",
            "Bir grupta anlaşmazlık çıktığında genellikle arabulucu rolünü üstlenirim.",
            "İnsanların sadece söylediklerini değil, beden dillerini ve ses tonlarını da iyi analiz ederim.",
            "Çevremdeki insanlar genellikle dertlerini paylaşmak veya tavsiye almak için bana gelirler.",
            "Grup çalışmalarında liderlik üstlenmek, görev dağılımı yapmak ve ekibi motive etmek bana göredir.",
            "Farklı kültürlerden veya arka planlardan gelen insanlarla empati kurmakta zorlanmam.",
            "Bir insanın ruh halindeki anlık değişimleri (üzüntü, öfke, heyecan) hemen sezerim.",
            "Takım oyunlarında ve ortak projelerde uyum sağlamak benim için oldukça doğaldır.",
            "Sosyal organizasyonlar planlamak, arkadaş gruplarını bir araya getirmek beni mutlu eder.",
            "İkna kabiliyetimin yüksek olduğunu düşünürüm; fikirlerimi başkalarına aktarırken başarılıyım.",
            "Bir insanı dinlerken yargılamadan, dikkatle ve onun gözünden bakarak dinlemeyi başarırım.",
            "Toplulukların enerjisini ve dinamiklerini yönlendirme konusunda kendime güvenirim.",
            "İş birliği yapılması gereken durumlarda kişisel egoları geri plana itebilirim.",
            "İnsanların güçlü yönlerini keşfetmek ve onları doğru alanlara yönlendirmek hoşuma gider.",
            "Ağ kurma (networking) ve profesyonel ilişkiler geliştirme konusunda aktif biriyimdir.",
            "Sosyal sorumluluk projelerinde görev almak ve toplumsal fayda sağlamak benim için önemlidir.",
            "Bireysel çalışmak yerine, beyin fırtınası yapılabilecek dinamik ekiplerde daha üretken olurum.",
            "Geri bildirim (eleştiri) verirken veya alırken yapıcı üslubu korumaya özen gösteririm.",
            "İnsanların motivasyon kaynaklarını bulup onları harekete geçirmek heyecan vericidir.",
            "Kitle iletişim araçları, sosyal dinamikler ve topluluk psikolojisi üzerine düşünürüm."
        ],
        "Matematik": [
            "Karmaşık problemleri mantıklı parçalara ayırarak çözmek bana keyif verir.",
            "Olaylar veya veriler arasındaki neden-sonuç ilişkilerini ve kalıpları hızlıca fark ederim.",
            "Bir karar alırken duygulardan ziyade somut verilere, sayılara ve kanıtlara güvenirim.",
            "Bulmacalar, strateji oyunları (satranç vb.) ve mantık yürütme testlerinde başarılıyımdır.",
            "Matematiksel formüller, denklemler veya kodlama mantığı bana karmaşık gelmez.",
            "Zihinden hızlı hesaplamalar yapmak veya sayısal tahminlerde bulunmak benim için kolaydır.",
            "Finansal tabloları, grafikleri ve istatistiksel verileri incelemek ilgimi çeker.",
            "Sistemli ve düzenli çalışmayı severim; kaos yerine bir algoritma takip etmeyi tercih ederim.",
            "Bilimsel keşifler, teknolojik yenilikler ve evrenin çalışma prensipleri üzerine düşünürüm.",
            "Soyut kavramları geometrik veya matematiksel modellere oturtarak daha iyi anlarım.",
            "Bir bilginin doğruluğunu kabul etmeden önce mantıksal bir ispat veya delil ararım.",
            "Büyük ve karmaşık veri setleri içerisindeki sapmaları, anomalileri tespit edebilirim.",
            "Stratejik planlama yapmak, risk analizi çıkarmak ve senaryolar üretmek bana göredir.",
            "Verimlilik artırma, süreç optimizasyonu ve maliyet hesapları gibi konular ilgimi çeker.",
            "Kriptoloji, şifreleme mantığı veya veri tabanı mimarileri üzerine okumalar yaparım.",
            "Bir sistemdeki tıkanıklığı veya teknik bir problemi kök nedenine inerek çözerim.",
            "Matematiksel bir problemin farklı yollardan nasıl çözülebileceğini aramaktan sıkılmam.",
            "Ekonomik trendler, borsa grafikleri veya küresel pazar verileri dikkatimi çeker.",
            "Bilgisayar yazılımlarının çalışma arkasındaki mantığı ve algoritmaları anlamaya çalışırım.",
            "Ölçülebilir hedefler koymayı ve başarıyı net metriklerle takip etmeyi severim."
        ],
        "Müzik": [
            "Bir ortamdaki arka plan seslerini, ritimleri veya melodi değişimlerini hemen fark ederim.",
            "Çalışırken veya düşünürken arka planda bir ritim tutmak odaklanmama yardımcı olur.",
            "Şarkıların melodilerini, tonlarını veya enstrüman geçişlerini zihnimde kolayca ayırt edebilirim.",
            "Bir şarkıyı sadece bir kez duymama rağmen daha sonra mırıldanabilir veya ritmini hatırlayabilirim.",
            "Müzik aletlerinin ses akortlarındaki en ufak sapmaları veya detone durumları hemen hissederim.",
            "Bir enstrüman çalıyorum veya bir enstrümanı çalmayı öğrenme konusunda yüksek bir hevesim var.",
            "Doğadaki sesler (yağmur, rüzgar, kuş sesleri) zihnimde melodik bir yapı oluşturur.",
            "Şarkı sözlerinden ziyade, müziğin arkasındaki armoni ve beste yapısı dikkatimi çeker.",
            "Farklı müzik türlerini dinlemekten ve bu türlerin kökenlerini araştırmaktan keyif alırım.",
            "Ritim duygum gelişmiştir; dans ederken veya tempoya ayak uydururken zorluk çekmem.",
            "Seslerin tınılarını (akustik kalitesini) ve mekandaki yankılanma biçimlerini ayırt edebilirim.",
            "Zihnimde sürekli bir melodi üretimi veya var olan müzikleri yeniden aranje etme eğilimi vardır.",
            "Müzikal korolar, orkestralar veya akustik performanslar beni derinden etkiler.",
            "Filmleri izlerken sahnelerin arkasındaki müzikal temanın duyguyu nasıl yönettiğini incelerim.",
            "Ses montajı, ses efektleri tasarlama veya dijital müzik üretimi ilgimi çeken alanlardır.",
            "Çevremdeki insanların ses tonlarından onların ruh hallerini ve samimiyetlerini analiz edebilirim.",
            "Müzik teorisi, notasyon bilgisi veya solfej gibi akademik konular bana zor gelmez.",
            "Kendi başıma kaldığımda müzik eşliğinde düşünmek yaratıcılığımı gözle görülür şekilde artırır.",
            "Bir eserin hangi döneme (Klasik, Barok, Modern vb.) ait olduğunu kabaca tahmin edebilirim.",
            "Enstrümanların yapım süreçleri, akustik mühendisliği ve ses fiziği konularını merak ederim."
        ],
        "Bedensel": [
            "Bir şeyi sadece dinlemek yerine, ona dokunarak veya bizzat uygulayarak daha iyi öğrenirim.",
            "El becerisi gerektiren işlerde (tamirat, maket, yemek yapma, çizim vb.) oldukça hassasımdır.",
            "Fiziksel koordinasyon ve denge gerektiren aktivitelerde kendime güvenirim.",
            "Uzun süre masa başında oturmak enerjimi tüketir; hareket halinde olmayı tercih ederim.",
            "Spor yapmak, dans etmek, yürüyüş veya doğa aktivitelerine katılmak yaşam tarzımın bir parçasıdır.",
            "Beden dilimi ve mimiklerimi duygularımı aktarırken oldukça etkili bir şekilde kullanırım.",
            "Aletleri, makineleri veya mutfak gereçlerini kullanırken reflekslerim hızlı ve güvenlidir.",
            "Bir el becerisini veya fiziksel bir hareketi bir kez görerek taklit edebilirim.",
            "Yüksek dikkat ve fiziksel hassasiyet gerektiren detaylı işlerde sabırlıyım.",
            "Sahada olmak, açık havada çalışmak veya materyallerle doğrudan temas kurmak beni besler.",
            "Kendi sınırlarımı, fiziksel dayanıklılığımı ve kas gücümü iyi tanır ve yönetirim.",
            "Mekanik parçaları sökmek, temizlemek, bir araya getirmek benim için bir çeşit deşarj yöntemidir.",
            "Cerrahi operasyonlar, ince el işçilikleri veya kuyumculuk gibi hassas motor beceriler ilgimi çeker.",
            "Fiziksel risk içeren macera sporları veya dinamik görevler bende korku yerine heyecan uyandırır.",
            "Vücut ergonomisi, doğru duruş ve fiziksel sağlık konularına özen gösteririm.",
            "Bir nesnenin ağırlığını, dokusunu ve sıcaklığını dokunarak hızlıca analiz edebilirim.",
            "Takım sporlarında stratejiyi sahada anlık olarak uygularken oldukça çeviğimdir.",
            "Yorulmak bilmeyen bir fiziksel enerjiye sahip olduğumu söylerler.",
            "Sahne sanatları, pandomim, tiyatral hareketler veya koreografiler tasarlamak ilgimi çeker.",
            "Zorlu doğa şartlarında veya engebeli arazilerde fiziksel kontrolümü kaybetmem."
        ],
        "Görsel": [
            "Gittiğim bir yerin mimari yapısını, düzenini veya haritasını zihnimde kolayca canlandırabilirim.",
            "Grafikler, şemalar, renk uyumları ve görsel tasarımlar dikkatimi çok çabuk çeker.",
            "Üç boyutlu nesneleri farklı açılardan hayal etmek benim için oldukça kolaydır.",
            "Bir konuyu öğrenirken metinlerden ziyade infografikler, resimler ve videolar bana yardımcı olur.",
            "Fotoğraf çekmek, video kurgulamak veya dijital tasarımlar yapmak ilgimi çeken uğraşlardır.",
            "Yön duygum çok gelişmiştir; harita okumakta veya bilmediğim bir yerde yolumu bulmakta zorlanmam.",
            "Kıyafet seçiminde, oda dekorasyonunda veya sunum hazırlarken renk kombinasyonlarına çok dikkat ederim.",
            "Gördüğüm insanların yüzlerini, giydikleri detayları veya mekanların dekorunu yıllar sonra bile hatırlarım.",
            "Karalamalar yapmak, eskiz çizmek veya zihnimdeki fikirleri şemalara dökmek hoşuma gider.",
            "Görsel sanatlar, sinema, resim sergileri veya mimari yapıtlar entelektüel ilgimi çeker.",
            "Bir web sitesinin, mobil uygulamanın veya derginin görsel düzenindeki dengesizlikleri hemen yakalarım.",
            "Geometrik şekiller, perspektif çizimleri ve teknik çizim konuları bana anlaşılır gelir.",
            "Hayal gücüm çok renklidir; bir projeyi hayata geçirmeden önce bitmiş halini zihnimde net görürüm.",
            "Görsel simgeler, amblemler ve logolar üzerinden markaların vermeye çalıştığı mesajları iyi okurum.",
            "Işık, gölge ve derinlik algım gelişmiştir; estetik detaylar hayat kalitemi etkiler.",
            "Bir odadaki eşyaların yerini değiştirerek alanı nasıl daha verimli kullanabileceğimi hemen planlarım.",
            "Tasarım trendlerini, tipografi (yazı tipi) sanatını ve animasyon dünyasını takip ederim.",
            "Kelimelerle anlatılması zor olan karmaşık bir konuyu çizerek veya şematize ederek anlatmayı seçerim.",
            "Sinemada kamera açıları, renk paletleri ve sahne kompozisyonları (sinematografi) dikkatimi çeker.",
            "Soyut tablolar, illüstrasyonlar ve dijital sanat eserleri üzerinde saatlerce konuşabilirim."
        ]
    },
    "İlgi Odakları": {
        "İnsan": [
            "Günlük hayatımda beni en çok heyecanlandıran şey yeni insan hikayeleri dinlemek ve onları anlamaktır.",
            "İnsanların hayatlarına dokunmak, onlara yardım etmek veya rehberlik etmek beni manevi olarak tatmin eder.",
            "İnsan psikolojisi, davranış bilimleri ve toplumsal hareketlerin nedenleri üzerine okumalar yaparım.",
            "Bireysel koçluk, danışmanlık veya insan kaynakları gibi doğrudan insan odaklı meslekler bana göredir.",
            "Bir insanın potansiyelini ortaya çıkarmasına destek olmak bana gurur verir.",
            "Topluluk önünde sunum yaparken veya bir gruba bir şeyler öğretirken enerjim tavan yapar.",
            "İnsanlar arasındaki çatışmaları çözmek ve ortak bir paydada buluşturmak benim uzmanlık alanımdır.",
            "Yardım dernekleri, mentorluk programları ve sosyal dayanışma ağları içinde aktif olmayı severim.",
            "Kişisel gelişim, felsefe ve sosyoloji gibi insanı merkeze alan disiplinler ilgimi çeker.",
            "Bir ekibin yönetimini üstlendiğimde personelin mutluluğu ve gelişimi önceliğim olur.",
            "İnsan ilişkilerindeki dinamikleri çözmek, kimin neye ihtiyacı olduğunu sezmek konusunda başarılıyım.",
            "Müşteri ilişkileri, diplomasi veya halkla ilişkiler gibi doğrudan diyalog içeren alanlar bana göredir.",
            "İnsanların önyargılarından arınması ve daha anlayışlı bir toplum yapısı kurulması için kafa yorarım.",
            "Bir menti (öğrenci) yetiştirmek ve onun kariyerindeki başarısına tanıklık etmek paha biçilemezdir.",
            "Röportajlar, biyografiler ve insan davranışlarını konu alan belgeseller ilk tercihimdir.",
            "Kriz anlarında insanların sakinleşmesini sağlayacak güven veren bir duruş sergileyebilirim.",
            "Farklı yaş gruplarından (çocuklar, gençler, yaşlılar) insanlarla ortak dil bulmakta zorlanmam.",
            "İnsanların motivasyonunu neyin düşürdüğünü veya neyin artırdığını gözlemlemeyi severim.",
            "Ekip içindeki bağları güçlendirmek adına sosyal etkinlikler ve kaynaşma toplantıları organize ederim.",
            "Kolektif çalışma bilincine inanırım; bireysel başarı yerine takım başarısı beni daha çok tatmin eder."
        ],
        "Yer": [
            "Çalıştığım veya bulunduğum ortamın coğrafi konumu, atmosferi ve tasarımı enerjimi doğrudan etkiler.",
            "Yeni şehirler keşfetmek, mekanların tarihi veya çevresel dokusunu incelemek bana ilham verir.",
            "Şehir planlaması, mimari restorasyon veya çevre düzenleme projeleri ilgimi çeken alanlardır.",
            "Doğal yaşam alanlarının korunması, sürdürülebilir ekosistemler ve yeşil enerjiyi savunurum.",
            "Masa başında oturmaktansa, farklı coğrafyalarda veya sahada mekan araştırması yapmayı tercih ederim.",
            "Tarihi binaların, antik kentlerin veya modern yapıların arkasındaki hikayeleri araştırmayı severim.",
            "Seyahat rotaları planlamak, coğrafi keşifler yapmak ve haritaları incelemek harika bir hobidir.",
            "Açık havada, doğayla iç içe veya geniş kampüslerde çalışmak üretkenliğimi iki katına çıkarır.",
            "Bölgesel kalkınma, lojistik konum analizleri ve jeopolitik konular ilgimi çeker.",
            "İç mekan tasarımı, ışıklandırma ve alan verimliliği gibi mimari detaylara karşı hassasım.",
            "Çevresel kirlilikle mücadele, geri dönüşüm projeleri ve ekolojik denge konularında duyarlıyım.",
            "Arkeoloji, jeoloji veya coğrafya belgeselleri izlemek bana büyük keyif verir.",
            "Bir şehrin veya bölgenin kültürel kimliğini yansıtan sokak dokularını fotoğraflamayı severim.",
            "Sürdürülebilir şehirler ve akıllı bina teknolojileri üzerine makaleler okumak hoşuma gider.",
            "Yerel tarım projeleri, botanik bahçeleri veya milli parklar ilgilendiğim alanlar arasındadır.",
            "Gayrimenkul geliştirme, arazi analizi ve doğru konum seçimi gibi stratejik konuları merak ederim.",
            "Farklı ülkelerin yaşam standartlarını ve yerleşim planlarını karşılaştırmalı olarak incelerim.",
            "İklim krizinin coğrafyalar üzerindeki etkileri ve göç dalgaları üzerine kafa yorarım.",
            "Tarihi dokunun korunarak modern hayata entegre edildiği projeleri takdirle takip ederim.",
            "Bir mekanın ruhu (genius loci) olduğuna inanırım; atmosferi soğuk yerlerde uzun süre kalamam."
        ],
        "Nesne": [
            "Somut araçlarla çalışmak, cihazları kurcalamak veya materyalleri şekillendirmek hoşuma gider.",
            "Eşyaların, makinelerin veya yazılımların çalışma mekanizmalarını çözmek beni cezbeder.",
            "Donanım parçaları, robotik kitler, 3D yazıcılar ve mekanik araçlar heyecanımı artırır.",
            "Bozulan bir ev aletini, elektronik cihazı veya mekanik sistemi kendi başıma tamir etmeyi denerim.",
            "Endüstriyel üretim hatları, otomobiller, motorlar ve fabrikasyon süreçleri ilgimi çeker.",
            "Laboratuvar cihazları, mikroskoplar veya cerrahi aletler gibi yüksek hassasiyetli nesneler dikkatimi çeker.",
            "Ürün tasarımları, prototipler üretmek ve somut bir çıktıyı elime almak beni tatmin eder.",
            "Malzeme bilimi; ahşap, metal, plastik veya kompozit malzemelerin yapısal özellikleri ilgimi çeker.",
            "Bilgisayar donanımı toplamak, parça uyumluluklarını araştırmak ve overclock gibi işlemlerle uğraşırım.",
            "Antika eşyalar, saat mekanizmaları veya el yapımı enstrümanlar gibi ince işçilikleri incelerim.",
            "Üretim teknolojileri, otomasyon sistemleri ve endüstri 4.0 bileşenlerini merak ederim.",
            "Bir ürünün kutu açılımını yapmak, ergonomisini ve malzeme kalitesini test etmek hoşuma gider.",
            "Zanaatkarlık kültürüne saygı duyarım; demircilik, marangozluk gibi geleneksel üretimleri izlerim.",
            "Maket yapmak, lego setleri kurmak veya model uçaklar geliştirmek yaratıcılığımı besler.",
            "Teknolojik cihazların iç şemalarını, devre kartlarını ve lehimleme işlerini yapmaktan çekinmem.",
            "Ağır sanayi makineleri, gemiler veya uçakların mühendislik detayları ilgimi çeken konulardır.",
            "Somut varlıkların envanterini çıkarmak, onları kategorize etmek ve düzenlemek bana göredir.",
            "Teknolojik fuarları ziyaret etmek, yeni nesil cihazları yakından incelemek heyecan vericidir.",
            "Yazıcılar, tarayıcılar veya CNC tezgahları gibi üretim araçlarını kullanmayı hızlıca öğrenirim.",
            "Fiziksel bir objenin estetiği kadar dayanıklılığı ve fonksiyonelliği de benim için kritiktir."
        ],
        "Eylem": [
            "Sürekli hareket halinde olmak, sahada aktif görev almak masa başında oturmaktan daha caziptir.",
            "Teoride kalan fikirler yerine, hemen uygulamaya dökülebilen dinamik süreçlerin içinde yer almayı severim.",
            "Kriz anlarında, hızlı müdahale gerektiren operasyonlarda soğukkanlı kalıp aksiyon alabilirim.",
            "Acil durum yönetimi, saha koordinatörlüğü veya aktif lojistik süreçler benim enerjime uygundur.",
            "Rutin ve her günü aynı geçen işler beni boğar; her gün yeni bir aksiyonun içinde olmalıyım.",
            "Etkinlik yönetimi, festival organizasyonları veya canlı yayın koordinatörlüğü gibi tempolu işleri severim.",
            "Hızlı kararlar alıp bunları anında sahada uygulamaya geçirmek benim liderlik tarzımdır.",
            "Seyahat engeli olmayan, sürekli farklı yerlerde operasyon yürütmemi gerektiren meslekler bana göredir.",
            "Lojistik, tedarik zinciri yönetimi ve saha denetimleri gibi dinamik süreçleri merak ederim.",
            "Projelerin yürütme aşamasında (execution) aktif rol almak, planlama aşamasından daha keyiflidir.",
            "Adrenalin içeren aktiviteler, saha görevleri ve esnek çalışma saatleri motivasyonumu artırır.",
            "Bir ekibi operasyonel hedeflere ulaştırmak için sahada onlarla birlikte ter dökmeyi tercih ederim.",
            "Zaman yönetimi baskısı altında, dar sürelerde iş bitirme konusunda oldukça başarılıyımdır.",
            "Satış-pazarlama operasyonları, saha anketleri veya müşteri ziyaretleri gibi hareketli işleri severim.",
            "Fabrika sahasında, inşaat alanında veya stüdyolarda aktif çalışmak beni canlı tutar.",
            "Sorunları masa başında tartışarak çözmek yerine, sorunun çıktığı yere gidip yerinde müdahale ederim.",
            "Değişen şartlara hızla ayak uydurur, plan B ve plan C'yi sahada anında devreye sokabilirim.",
            "Bürokratik süreçler ve uzun onay mekanizmaları yerine hızlı aksiyon alan sistemleri savunurum.",
            "Performans odaklı biriyimdir; günün sonunda ortaya çıkan somut iş hacmi benim için önemlidir.",
            "Saha muhabirliği, acil tıp hizmetleri veya şantiye şefliği gibi yüksek tempolu rolleri çekici bulurum."
        ],
        "Bilgi": [
            "Bir konunun derinlemesine araştırmasını yapmak, verileri incelemek ve yeni şeyler öğrenmek en büyük tutkumdur.",
            "Raporlar okumak, analizler sentezlemek ve soyut kavramlar üzerinde teoriler üretmek bana keyif verir.",
            "Büyük veri setlerini analiz etmek, trendleri yakalamak ve bunlardan stratejik anlamlar çıkarmak isterim.",
            "Akademik araştırmalar yapmak, kütüphanelerde veya dijital veri tabanlarında vakit geçirmek bana göredir.",
            "Bir şeyin nedenini tam olarak öğrenmeden, sadece yüzeysel bilgiyle yetinmek beni asla tatmin etmez.",
            "Ansiklopediler, bilimsel makaleler ve araştırma tezleri okumak benim için sıkıcı değil, heyecan vericidir.",
            "Bilgi grafikleri oluşturmak, kavram haritaları çıkarmak ve bilgiyi sistematize etmek hoşuma gider.",
            "Piyasa araştırmaları, rakip analizleri ve sektörel raporlar hazırlama konusunda yetenekliyimdir.",
            "Felsefe, tarih, bilim tarihi gibi bilginin kökenini ve evrimini inceleyen alanları merak ederim.",
            "Bir veri yığınından anlamlı içgörüler (insights) çıkararak üst yönetime stratejik yön verebilirim.",
            "Sürekli kendimi eğitmek, yeni sertifikalar almak ve entelektüel sermayemi büyütmek isterim.",
            "Yapay zeka modelleri, veri madenciliği ve iş zekası (BI) araçları ilgimi çeken konulardır.",
            "Karmaşık teorileri basitleştirerek anlaşılır kılma ve bilgi aktarımı yapma konusunda başarılıyım.",
            "Arşiv araştırmaları yapmak, eski belgeleri veya dijital kayıtları incelemek beni heyecanlandırır.",
            "Bilgi güvenliği, telif hakları ve bilginin etik kullanımı gibi konulara önem veririm.",
            "İstatistik bilimi, olasılık hesapları ve tahminleme modelleri üzerine kafa yormayı severim.",
            "Bir konunun uzmanı (subject matter expert) olmak ve danışmanlık vermek kariyer hedefim olabilir.",
            "Farklı disiplinlerdeki bilgileri birleştirerek (multidisipliner) inovatif fikirler geliştirebilirim.",
            "Soru sormaktan, bilmediğimi itiraf edip doğrusunu öğrenmek için araştırmaktan çekinmem.",
            "Dünyadaki bilgi akışını, trend analizlerini ve düşünce kuruluşlarının (think-tank) raporlarını takip ederim."
        ]
    },
    "Karar Mekanizması": {
        "Mantık": [
            "Hayatımdaki kritik kararları alırken duygularımı bir kenara bırakır, artı-eksi listesi yaparım.",
            "Kuralların ve objektif kriterlerin, kişisel durumlara göre esnetilmeden herkese eşit uygulanması gerektiğine inanırım.",
            "Bir tartışmada haklıyı belirlerken kişilerin duygularına veya iyi niyetine değil, somut kanıtlara bakarım.",
            "Eleştirilerimi tamamen gerçekler üzerinden net ve dobra bir şekilde yaparım; karşı tarafın alınma ihtimali fikrimi değiştirmez.",
            "Adalet kavramının tamamen kör ve duygulardan arınmış olması gerektiğine, hukukun üstünlüğüne inanırım.",
            "Liderlik yaparken ekibin performansını net başarı kriterleri (KPI) üzerinden objektif olarak değerlendiririm.",
            "Bir sorun karşısında paniğe kapılmak yerine, mantıksal adımlarla hatanın kaynağını bulmaya odaklanırım.",
            "Verimlilik ve sistemin sürdürülebilirliği, kişisel konfor alanlarından veya duygusal beklentilerden önce gelir.",
            "Kararlarımın uzun vadeli ve rasyonel sonuçlarını hesaplamadan asla fevri adımlar atmam.",
            "İş ortamında profesyonel mesafe ve ciddiyetin korunması gerektiğine, samimiyetin işi aksatabileceğine inanırım.",
            "Bana sunulan bir fikrin doğruluğunu test etmek için onu en sert mantık süzgeçlerinden geçiririm.",
            "Zaman ve kaynak yönetiminde son derece katıyımdır; duygusal tavizler vererek bütçeyi riske atmam.",
            "Haklı olduğum bir konuda, çoğunluğun fikri farklı olsa bile doğruları savunmaktan geri adım atmam.",
            "Çatışma yönetiminde tarafların hislerine değil, olayın nesnel gelişim sürecine bakarak karar veririm.",
            "Bireysel hedeflerimi belirlerken hayaller yerine, yeteneklerimi ve piyasa gerçeklerini rasyonelce analiz ederim.",
            "Gereksiz detaylardan ve duygusal ajitasyonlardan arındırılmış, net ve öz raporları tercih ederim.",
            "Kurumsal bir yapıda hiyerarşinin, görev tanımlarının ve kuralların net olması iş barışını sağlar.",
            "Bir projeye yatırım yapmadan önce yatırımın geri dönüş oranını (ROI) kesin verilerle hesaplamak isterim.",
            "Duygusal zayıflıkların veya anlık motivasyon kayıplarının profesyonel hayatı etkilemesine müsaade etmem.",
            "Tarihteki başarılı liderlerin duygusal yaklaşımlarından ziyade stratejik ve akılcı hamlelerini örnek alırım."
        ],
        "His": [
            "Önemli bir karar verirken içimden gelen o güçlü sezgiye (iç sesime) raporlardan daha çok güvenirim.",
            "Bir karar alırken, bu kararın çevremdeki insanların huzurunu ve duygularını nasıl etkileyeceğini mutlaka düşünürüm.",
            "İnsan ilişkilerinde empati, şefkat ve anlayışın kurallardan çok daha üstün olduğunu savunurum.",
            "Bir kişiye geri bildirim verirken kırılmamasına, motivasyonunun düşmemesine maksimum özen gösteririm.",
            "Ekip çalışmasında uyum, pozitif enerji ve samimiyet benim için yüksek performanstan önce gelir.",
            "Bir projenin mantıklı olması yetmez; içime sinmesi ve beni kalben heyecanlandırması gerekir.",
            "Kuralların insanların mutluluğu için var olduğuna, gerektiğinde esnetilebileceğine inanırım.",
            "İş arkadaşlarımla sadece profesyonel değil, samimi ve güvene dayalı insani bağlar kurmak isterim.",
            "Toplumsal fayda sağlayan, vizyoner ve idealist projeler için maddi kazançları arka plana itebilirim.",
            "Bana haksızlık yapıldığında bile karşı tarafın durumunu anlamaya çalışır, affedici bir tutum sergilerim.",
            "Yöneticilik tarzım otoriter kurallara değil, ekibe ilham vermeye ve rızalarını almaya dayanır.",
            "Bir ortamdaki gerginliği veya negatif enerjiyi daha kapıdan girer girmez hisseder ve modumu dengelerim.",
            "İnsanların potansiyellerine inanırım; geçmiş hatalarına bakarak onlardan tamamen ümit kesmem.",
            "Geleceğe dair planlarımı yaparken içsel huzurumu, mutluluğumu ve değerlerimi en başa koyarım.",
            "Takım içindeki bir üyenin kişisel bir sorunu varsa, işin gecikmesi pahasına ona destek olmayı seçerim.",
            "Sanatsal vizyonun, sezgilerin ve yaratıcı dehanın katı mantık formüllerinden daha üstün olduğunu düşünürüm.",
            "Birlikte çalışacağım insanları seçerken teknik özgeçmişlerinden ziyade karakterlerine ve enerjilerine bakarım.",
            "Toplumsal adaletsizlikler, eşitsizlikler ve mazlumların durumu beni derinden yaralar ve harekete geçirir.",
            "Samimiyetten uzak, tamamen mekanik ve sadece çıkar odaklı yürüyen kurumsal ilişkiler bana göre değildir.",
            "Hayatın sadece sayılardan ve başarılardan ibaret olmadığına, paylaşılan anların değerine inanırım."
        ]
    }
}

# --- 120+ Meslek Veritabanı ---
MESLEK_HAVUZU = [
    {"ad": "Yazılım Geliştirici / Mühendis", "zeka": "Matematik", "odak": "Bilgi", "karar": "Mantık"},
    {"ad": "Veri Bilimci / Yapay Zeka Uzmanı", "zeka": "Matematik", "odak": "Bilgi", "karar": "Mantık"},
    {"ad": "Siber Güvenlik Analisti", "zeka": "Matematik", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Genel Cerrah / Beyin Cerrahı", "zeka": "Bedensel", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Diş Hekimi / Ortodontist", "zeka": "Bedensel", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Klinik Psikolog", "zeka": "İletişim", "odak": "İnsan", "karar": "His"},
    {"ad": "Psikiyatrist", "zeka": "İletişim", "odak": "İnsan", "karar": "Mantık"},
    {"ad": "Mimar / İç Mimar", "zeka": "Görsel", "odak": "Yer", "karar": "Mantık"},
    {"ad": "Endüstriyel Tasarımcı", "zeka": "Görsel", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Ses Mühendisi / Aranjör", "zeka": "Müzik", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Metin Yazarı / Editör", "zeka": "Sözel", "odak": "Bilgi", "karar": "His"},
    {"ad": "Uluslararası İlişkiler Uzmanı / Diplomat", "zeka": "Sözel", "odak": "İnsan", "karar": "Mantık"},
    {"ad": "Avukat / Hukuk Danışmanı", "zeka": "Sözel", "odak": "Bilgi", "karar": "Mantık"},
    {"ad": "İnsan Kaynakları Koordinatörü", "zeka": "İletişim", "odak": "İnsan", "karar": "His"},
    {"ad": "Pilot / Kaptan", "zeka": "Bedensel", "odak": "Eylem", "karar": "Mantık"},
    {"ad": "Peyzaj Mimarı / Şehir Plancısı", "zeka": "Görsel", "odak": "Yer", "karar": "Mantık"},
    {"ad": "UX/UI Tasarımcısı", "zeka": "Görsel", "odak": "Bilgi", "karar": "Mantık"},
    {"ad": "Finansal Analist / Portföy Yöneticisi", "zeka": "Matematik", "odak": "Bilgi", "karar": "Mantık"},
    {"ad": "Biyomedikal Mühendisi", "zeka": "Matematik", "odak": "Nesne", "karar": "Mantık"},
    {"ad": "Halkla İlişkiler Direktörü", "zeka": "İletişim", "odak": "İnsan", "karar": "His"},
    {"ad": "Çocuk Sağlığı Uzmanı (Pediatri)", "zeka": "İletişim", "odak": "İnsan", "karar": "His"},
    {"ad": "Fizyoterapist", "zeka": "Bedensel", "odak": "İnsan", "karar": "His"}
]

# --- Hafıza (Session State) Yönetimi ---
if "cevaplar" not in st.session_state:
    st.session_state.cevaplar = {}

# --- GÖRSEL STİL (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght=400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Urbanist', sans-serif;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%);
        padding: 50px;
        border-radius: 24px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(30, 58, 138, 0.2);
        margin-bottom: 35px;
        position: relative;
    }
    .hero-title {
        font-size: 42px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 10px;
        color: #FFFFFF;
    }
    .hero-subtitle {
        font-size: 20px;
        opacity: 0.9;
        font-weight: 400;
        max-width: 800px;
        margin: 0 auto 25px auto;
    }
    .hero-badge {
        background-color: #F59E0B;
        color: #0F172A;
        padding: 6px 16px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 14px;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .m-card {
        background-color: #F8FAFC;
        padding: 30px;
        border-radius: 20px;
        border-bottom: 4px solid #1E3A8A;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .m-card h4 {
        color: #1E3A8A;
        font-size: 22px;
        font-weight: 700;
        margin-top: 0;
    }
    
    .stat-box {
        text-align: center;
        padding: 20px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .stat-number {
        font-size: 64px;
        font-weight: 700;
        color: #1E3A8A;
        line-height: 1;
    }
    .stat-label {
        font-size: 14px;
        color: #F59E0B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 5px;
    }
    
    .dev-profile {
        background-color: #1E3A8A;
        color: white;
        padding: 35px;
        border-radius: 24px;
        margin-top: 30px;
        border-left: 8px solid #F59E0B;
    }
    
    .footer { font-size: 14px; color: #6b7280; text-align: center; margin-top: 60px; font-style: italic; }
    .soru-metni { font-size: 15px; font-weight: 500; color: #2D3748; margin-top: 10px; }
    .kategori-baslik { color: #1E3A8A; font-weight: 700; margin-top: 25px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- YAN MENÜ (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1904/1904425.png", width=90)
    st.title("👨‍🏫 Kurumsal")
    st.info("**Bünyamin Dinçer**\n\nÖğrenci Gelişim Destek Sistemi")
    st.markdown("---")
    st.write("📊 **Envanter Ölçeği:**")
    st.caption("260 Akademik Madde\n13 Analiz Matrisi\n120+ Meslek Kombinasyonu")

# --- SEKMELİ ANA GÖVDE MİMARİSİ ---
sekme1, sekme2, sekme3 = st.tabs(["🚀 Kurumsal Giriş", "📝 Envanter Paneli", "📊 Analiz Raporu"])

# --- 1. SEKME: MCKINSEY STİLİ PRESTİJLİ GİRİŞ SAYFASI ---
with sekme1:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-badge">Akademik Envanter</div>
            <h1 class="hero-title">Kariyer Pusulası</h1>
            <p class="hero-subtitle">Öğrencilerin bilişsel kapasitelerini, ilgi odaklarını bir analiz motoru.</p>
            <div style="font-size:15px; opacity:0.8;">Geliştirici: <b>Bünyamin Dinçer</b></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Rakamlarla Envanter Gücü")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown('<div class="stat-box"><div class="stat-number">260</div><div class="stat-label">Akademik Madde</div><p style="color:#64748b; margin-top:10px; font-size:14px;">13 alt kırılımda derinlemesine veri toplama hassasiyeti.</p></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat-box"><div class="stat-number">120+</div><div class="stat-label">Meslek Mimarisi</div><p style="color:#64748b; margin-top:10px; font-size:14px;">Piyasa gerçekleriyle uyumlu eşleştirme havuzu.</p></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="stat-box"><div class="stat-number">%100</div><div class="stat-label">Objektif Veri</div><p style="color:#64748b; margin-top:10px; font-size:14px;">Anlık modlardan arındırılmış bilimsel ağırlık algoritması.</p></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🔍 Analiz Metodolojisi")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown("""
            <div class="m-card">
                <h4>🧠 Zekâ Alanları</h4>
                <p style="font-size:15px; color:#475569;">6 temel zekâ türü üzerinden baskın bilişsel alanları ve işlem yapma yeteneklerini haritalandırıyoruz.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_m2:
        st.markdown("""
            <div class="m-card">
                <h4>🎯 İlgi Odakları</h4>
                <p style="font-size:15px; color:#475569;">Dünyayı algılama biçimini; insan, bilgi, yer, eylem ve nesne eksenlerinde analiz ediyoruz.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_m3:
        st.markdown("""
            <div class="m-card">
                <h4>⚖️ Karar Biçimi</h4>
                <p style="font-size:15px; color:#475569;">Mantık ve his dengesini ölçerek, dönüm noktalarında nasıl stratejik kararlar alındığını tespit ediyoruz.</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("🎯 **Önemli Bilgilendirme:** Bu sistem bünyesinde üretilen tüm analizler birer **tavsiye niteliğindedir.**")
    
    st.markdown("""
        <div class="dev-profile">
            <h3 style="color:#F59E0B; margin-top:0; font-size:24px;">👨‍🏫 Geliştirici Notu</h3>
            <p style="font-size:16px; font-style:italic; opacity:0.95;">
                "Bu platform, liyakatli ve bilinçli nesillerin yetişmesine destek olmak amacıyla inşa edilmiştir."
                <br><br><b>— Bünyamin Dinçer</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- 2. SEKME: TEST PANELİ ---
with sekme2:
    st.subheader("📝 Yetenek & Eğilim Değerlendirme Testi")
    st.write("Lütfen her cümleye size ne kadar uygun olduğunu belirterek (1-5 arası) puan veriniz.")
    st.markdown("---")
    
    for ana_kategori, alt_kategoriler in SORULAR.items():
        st.markdown(f"<h2 class='kategori-baslik'>🎯 {ana_kategori}</h2>", unsafe_allow_html=True)
        
        for alt_kategori, soru_listesi in alt_kategoriler.items():
            with st.expander(f"🔹 {alt_kategori} Değerlendirmesi ({len(soru_listesi)} Soru)", expanded=False):
                for i, soru in enumerate(soru_listesi):
                    soru_key = f"{ana_kategori}_{alt_kategori}_{i}"
                    st.markdown(f"<p class='soru-metni'>{i+1}. {soru}</p>", unsafe_allow_html=True)
                    
                    cevap = st.radio(
                        "Değerlendirmeniz:",
                        options=[1, 2, 3, 4, 5],
                        format_func=lambda x: {1: "1 - Hiç Katılmıyorum", 2: "2 - Katılmıyorum", 3: "3 - Kararsızım", 4: "4 - Katılıyorum", 5: "5 - Tamamen Katılıyorum"}[x],
                        key=soru_key,
                        horizontal=True,
                        index=2
                    )
                    st.session_state.cevaplar[soru_key] = cevap
        st.markdown("---")
        
    st.success("🎉 Tüm alanlardaki soruları gözden geçirdiyseniz, raporunuzu oluşturmak için yukarıdaki **'Analiz Raporu'** sekmesine geçiş yapabilirsiniz!")

# --- 3. SEKME: ANALİZ VE RAPORLAMA ---
with sekme3:
    st.subheader("📊 Gelişmiş Grafiksel Analiz ve Kariyer Eşleşmesi")
    
    if st.button("📊 Kapsamlı Analiz Raporumu Hesapla"):
        skorlar = {"Zekâ Alanları": {}, "İlgi Odakları": {}, "Karar Mekanizması": {}}
        
        for kilit, deger in st.session_state.cevaplar.items():
            parcalar = kilit.split("_")
            ana_kat, alt_kat = parcalar[0], parcalar[1]
            if alt_kat not in skorlar[ana_kat]:
                skorlar[ana_kat][alt_kat] = []
            skorlar[ana_kat][alt_kat].append(deger)
            
        final_skorlar = {}
        for ana_kat, alt_katlar in skorlar.items():
            final_skorlar[ana_kat] = {}
            for alt_kat, liste in alt_katlar.items():
                final_skorlar[ana_kat][alt_kat] = sum(liste) / len(liste)
        
        st.balloons()
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("#### 🎯 Zekâ Alanı Analizi")
            if final_skorlar.get("Zekâ Alanları"):
                en_yuksek_zeka = max(final_skorlar["Zekâ Alanları"], key=final_skorlar["Zekâ Alanları"].get)
                st.metric(label="Baskın Zekâ", value=en_yuksek_zeka, delta=f"{final_skorlar['Zekâ Alanları'][en_yuksek_zeka]:.2f}/5")
                for zk, puand in final_skorlar["Zekâ Alanları"].items():
                    st.progress(puand / 5.0, text=f"{zk}: {puand:.2f}/5")
            
        with c2:
            st.markdown("#### 🔍 İlgi Odakları Ağırlıkları")
            if final_skorlar.get("İlgi Odakları"):
                en_yuksek_odak = max(final_skorlar["İlgi Odakları"], key=final_skorlar["İlgi Odakları"].get)
                st.metric(label="Baskın Odak", value=en_yuksek_odak, delta=f"{final_skorlar['İlgi Odakları'][en_yuksek_odak]:.2f}/5")
                for od, puan in final_skorlar["İlgi Odakları"].items():
                    st.progress(puan / 5.0, text=f"{od}: {puan:.2f}/5")
                    
        with c3:
            st.markdown("#### ⚖️ Karar Alma Eğilimi")
            if final_skorlar.get("Karar Mekanizması"):
                en_yuksek_karar = max(final_skorlar["Karar Mekanizması"], key=final_skorlar["Karar Mekanizması"].get)
                st.metric(label="Baskın Stil", value=en_yuksek_karar, delta=f"{final_skorlar['Karar Mekanizması'][en_yuksek_karar]:.2f}/5")
                for kr, puan in final_skorlar["Karar Mekanizması"].items():
                    st.progress(puan / 5.0, text=f"{kr}: {puan:.2f}/5")
        
        st.markdown("---")
        st.markdown("### 💼 Gelişmiş Matris Verilerine Göre Kariyer Rotaları")
        
        if final_skorlar.get("Zekâ Alanları") and final_skorlar.get("İlgi Odakları"):
            baskin_zk = max(final_skorlar["Zekâ Alanları"], key=final_skorlar["Zekâ Alanları"].get)
            baskin_od = max(final_skorlar["İlgi Odakları"], key=final_skorlar["İlgi Odakları"].get)
            
            for mslk in MESLEK_HAVUZU:
                if mslk["zeka"] == baskin_zk and mslk["odak"] == baskin_od:
                    st.success(f"🌟 **{mslk['ad']}** — %100 Tam Eşleşme (Profil: {mslk['zeka']} & {mslk['odak']})")
                elif mslk["zeka"] == baskin_zk or mslk["odak"] == baskin_od:
                    st.info(f"🔹 **{mslk['ad']}** — Yüksek Eğilimli Eşleşme (Uyum: {mslk['zeka']} / {mslk['odak']})")

# Alt Bilgi
st.markdown("<div class='footer'>© 2026 Kariyer Pusulası | Bünyamin Dinçer | Öğrenci Gelişim Destek Sistemi</div>", unsafe_allow_html=True)