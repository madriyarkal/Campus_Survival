# Campus Survival - Kampüste Hayatta Kal
# EEM2005 Programming in Engineering - Ekin Uğur Panko (250416018)

import random

MAX_SCORE = 100
MAX_LIVES = 3
TOTAL_ROUNDS = 10
SUCCESS_SCORE = 70

# Her olay bir sözlüktür. Her seçenek: [seçenek metni, sonuç metni, kaybedilen puan, kaybedilen can]
EVENTS = [
    {"title": "Laboratuvar Dersi", "text": "Devreyi kurdun ama LED yanmıyor.", "options": [
        ["Bağlantıları kontrol et.", "Ters takılmış bir kablo buldun. LED parladı!", 0, 0],
        ["LED'e moral ver.", "LED motivasyon konuşmasından etkilenmedi.", 10, 0],
        ["Kabloları rastgele değiştir.", "Bir şey yandı ama LED değildi. Asistan çok kızdı!", 20, 1]]},
    {"title": "Sınav Sabahı", "text": "Sınava giderken yanlış sınıfa girdin.", "options": [
        ["Hemen kapıdaki listeye bakıp doğru sınıfa koş.", "Son anda doğru sınıfa yetiştin.", 0, 0],
        ["Bu sınava da girerim, ne fark eder.", "Felsefe sınavında Ohm kanununu anlattın.", 20, 1],
        ["Koridorda ağlayarak dolaş.", "Biri sana yol gösterdi ama 10 dakika geç kaldın.", 10, 0]]},
    {"title": "Kantin", "text": "Elindeki kahve dökülmek üzere.", "options": [
        ["Bardağı iki elle sıkıca tut.", "Kahve kurtarıldı, gün kurtarıldı.", 0, 0],
        ["Kahveye 'dur!' diye bağır.", "Kahve dinlemedi, gömleğin kahverengi oldu.", 10, 0],
        ["Laptopun üstünde dengede tutmaya çalış.", "Klavyen artık kahve kokuyor.", 15, 0]]},
    {"title": "Ders Saati", "text": "Derste bilgisayarının şarjı bitmek üzere.", "options": [
        ["Prizin yanına geç ve şarj et.", "Şarj yüzde yüze doğru yükseliyor.", 0, 0],
        ["Ekran parlaklığını sıfıra indir.", "Hiçbir şey göremedin ama şarj biraz dayandı.", 5, 0],
        ["Bilgisayarı güneşe tut.", "Bilgisayarın güneş paneli olmadığını öğrendin.", 10, 0]]},
    {"title": "Kampüs Yolu", "text": "Kampüste aniden yağmur başladı.", "options": [
        ["En yakın binaya sığın.", "Kuru kaldın ve yağmur hemen dindi.", 0, 0],
        ["Çantanı kafana koy.", "Kafan kuru ama defterlerin ıslandı.", 10, 0],
        ["Yağmurda dans et.", "Çok eğlendin ama ertesi gün hasta oldun.", 15, 1]]},
    {"title": "Ödev Teslimi", "text": "Ödev dosyasını 'son_son_kesinson.py' adıyla kaydettin.", "options": [
        ["Hocanın istediği formatta yeniden adlandır.", "Dosya artık düzgün bir isme sahip.", 0, 0],
        ["Olduğu gibi gönder.", "Hoca dosya adını görünce gülümsedi ama puan kırdı.", 10, 0],
        ["Dosya adına bir şiir yaz.", "Sistem bu kadar uzun bir dosya adını kabul etmedi.", 15, 0]]},
    {"title": "Direnç Renkleri", "text": "Laboratuvarda direnç renklerini karıştırdın.", "options": [
        ["Multimetre ile direnci ölç.", "Doğru değeri buldun, devre çalıştı.", 0, 0],
        ["En sevdiğin rengi seç.", "Mor güzel bir renk ama yanlış direnç.", 10, 0],
        ["Bütün dirençleri aynı anda tak.", "Devreden duman çıktı, laboratuvar boşaltıldı!", 20, 1]]},
    {"title": "Otobüs Durağı", "text": "Kampüse giderken yanlış otobüse bindin.", "options": [
        ["İlk durakta inip doğru otobüse bin.", "Biraz geç de olsa kampüse vardın.", 0, 0],
        ["Şoföre rotayı değiştirmesini rica et.", "Şoför seni kibarca reddetti.", 10, 0],
        ["Son durağa kadar git, belki manzara güzeldir.", "Manzara güzeldi ama dersi tamamen kaçırdın.", 20, 0]]},
    {"title": "Sunum Günü", "text": "Sunum sırasında projektör çalışmıyor.", "options": [
        ["Kabloyu ve giriş kaynağını kontrol et.", "Yanlış giriş seçiliymiş, sunum başladı.", 0, 0],
        ["Slaytları elinle havaya çiz.", "Sınıf seni alkışladı ama hoca pek anlamadı.", 10, 0],
        ["Projektöre vur.", "Projektör kapandı ve bir daha açılmadı.", 15, 1]]},
    {"title": "Kütüphane", "text": "Kütüphanede aradığın kitabı bulamıyorsun.", "options": [
        ["Görevliye kitabın yerini sor.", "Kitap yan raftaymış.", 0, 0],
        ["Bütün rafları tek tek dolaş.", "Kitabı buldun ama iki saat geçti.", 5, 0],
        ["Kitabın ismini yüksek sesle çağır.", "Kitap gelmedi, 'sessiz olun' uyarısı aldın.", 10, 0]]},
    {"title": "Çevrimiçi Ders", "text": "Derste internet bağlantın koptu.", "options": [
        ["Telefonundan internet paylaş.", "Derse kaldığın yerden devam ettin.", 0, 0],
        ["Modeme sarılıp bekle.", "Modem duygulandı ama bağlanmadı.", 10, 0],
        ["Uyumaya karar ver.", "Ders bitti, yoklamada yoktun.", 15, 0]]},
    {"title": "Matematik Sınavı", "text": "Sınavda hesap makinenin pili bitti.", "options": [
        ["Yedek pili çantandan çıkar.", "Neyse ki yedek pilin vardı!", 0, 0],
        ["İşlemleri kağıt üzerinde yap.", "Yavaş ama doğru ilerledin.", 5, 0],
        ["Hesap makinesini salla.", "Ekranda sadece 'ERROR' yazdı.", 15, 0]]},
    {"title": "Ölçüm Zamanı", "text": "Multimetrede yanlış ölçüm aralığını seçtin.", "options": [
        ["Ölçümü durdur ve doğru aralığı seç.", "Ölçüm doğru çıktı.", 0, 0],
        ["Sonuç ne çıkarsa onu yaz.", "Raporuna 0.000 volt yazdın.", 10, 0],
        ["Akım ölçerken probları prize sok.", "Sigorta attı, multimetre emekli oldu!", 20, 1]]},
    {"title": "Sınıf Değişikliği", "text": "Ders başlamadan sınıfın değiştirildi.", "options": [
        ["Bölüm duyurularını kontrol et.", "Yeni sınıfı hemen buldun.", 0, 0],
        ["Boş sınıfta tek başına bekle.", "Kimse gelmedi, dersi kaçırdın.", 15, 0],
        ["Arkadaşlarının peşine takıl.", "Onlar da kaybolmuş, birlikte geç kaldınız.", 10, 0]]},
    {"title": "Gece Yarısı", "text": "Ödevini göndermeden bilgisayarın kapandı.", "options": [
        ["Açıp otomatik kaydedilen dosyayı kurtar.", "Dosya kurtarıldı ve zamanında gönderildi.", 0, 0],
        ["Ödevi baştan yaz.", "Yetiştirdin ama çok yoruldun.", 10, 0],
        ["Hocaya 'bilgisayarım ödevimi yedi' de.", "Hoca bu bahaneyi daha önce duymuştu.", 20, 1]]},
    {"title": "Kampüs Kedisi", "text": "Kampüs kedisi laptopunun klavyesine oturdu.", "options": [
        ["Kediyi nazikçe kucağına al.", "Kedi mırladı, kodun güvende.", 0, 0],
        ["Kedinin yazdığı kodu gönder.", "Kod 'asdfghjkl' hatasıyla çalışmadı.", 10, 0],
        ["Kediyle yer kapma yarışına gir.", "Kedi kazandı. Kediler hep kazanır.", 5, 0]]},
]


class Game:
    def __init__(self):
        self.score = MAX_SCORE
        self.lives = MAX_LIVES
        self.round = 0
        # random.sample olayları tekrar etmeden seçer
        self.events = random.sample(EVENTS, TOTAL_ROUNDS)

    def show_status(self):
        print("\n=== KAMPÜSTE HAYATTA KAL ===\n")
        print("Tur:", str(self.round) + "/" + str(TOTAL_ROUNDS))
        print("Puan:", str(self.score) + "/" + str(MAX_SCORE))
        print("Can:", str(self.lives) + "/" + str(MAX_LIVES))

    def get_choice(self):
        # Geçerli bir giriş gelene kadar tekrar sorar
        while True:
            choice = input("\nSeçiminiz: ").strip()
            if choice in ["1", "2", "3"]:
                return int(choice)
            print("Geçersiz giriş! Lütfen 1, 2 veya 3 yazın.")

    def apply_result(self, option):
        result, penalty, life_loss = option[1], option[2], option[3]
        print("\n" + result + "\n")
        if penalty == 0 and life_loss == 0:
            print("Doğru seçim! Puanın korundu.")
        if penalty > 0:
            print("-" + str(penalty), "PUAN")
        if life_loss > 0:
            print("-" + str(life_loss), "CAN")
        self.score = self.score - penalty
        self.lives = self.lives - life_loss
        # Puan 0 ile 100 arasında kalmalıdır
        if self.score > MAX_SCORE:
            self.score = MAX_SCORE
        if self.score < 0:
            self.score = 0
        if self.lives < 0:
            self.lives = 0
        print("\nGüncel puan:", self.score)
        print("Kalan can:", self.lives)

    def play_round(self, event):
        self.show_status()
        print("\nOLAY:", event["title"])
        print("\n" + event["text"] + "\n")
        for i in range(len(event["options"])):
            print(str(i + 1), "-", event["options"][i][0])
        choice = self.get_choice()
        self.apply_result(event["options"][choice - 1])

    def is_over(self):
        return self.score <= 0 or self.lives <= 0

    def show_final(self):
        print("\n========== FİNAL SONUCU ==========")
        print("Tamamlanan tur:", str(self.round) + "/" + str(TOTAL_ROUNDS))
        print("Final puanı:", self.score)
        print("Kalan can:", self.lives)
        if self.lives <= 0:
            print("\nCanın kalmadı! Kampüs bugün seni yendi. OYUN BİTTİ.")
        elif self.score <= 0:
            print("\nPuanın sıfıra düştü! Kampüs bugün seni yendi. OYUN BİTTİ.")
        elif self.score >= SUCCESS_SCORE:
            print("\nTEBRİKLER! Günü başarıyla tamamladın. Gerçek bir mühendis adayısın!")
        else:
            print("\nGünü tamamladın ama başarılı sayılmadın. Yarın tekrar dene!")
        print("==================================")

    def run(self):
        print("\nÇanakkale Onsekiz Mart Üniversitesi'nde yeni bir gün başlıyor...")
        print("Doğru kararlar vererek günü yüksek puanla tamamla!")
        for event in self.events:
            self.round = self.round + 1
            self.play_round(event)
            if self.is_over():
                break
            input("\nDevam etmek için Enter'a bas...")
        self.show_final()


def main():
    while True:
        game = Game()
        game.run()
        answer = input("\nTekrar oynamak ister misin? (e/h): ").strip().lower()
        while answer not in ["e", "h"]:
            answer = input("Lütfen 'e' veya 'h' yazın: ").strip().lower()
        if answer == "h":
            print("\nOynadığın için teşekkürler! Görüşmek üzere.")
            break


if __name__ == "__main__":
    main()
