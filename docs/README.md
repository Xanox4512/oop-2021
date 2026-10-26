# Vellum Roleplay — wybór postaci

Przeróbka przesłanego interfejsu według konceptu: scena o zachodzie słońca, pergaminowa księga w skórzanej oprawie, fotografie na kartach i czerwone pieczęcie.

## Uruchomienie

Podgląd GitHub Pages otwiera `index.html`. Oryginalny punkt wejścia `T4_KsiegaGladka.dc.html` również pozostaje dostępny.
Zachowaj strukturę katalogów; skopiuj całą zawartość archiwum do dotychczasowego katalogu interfejsu. Jeśli zasób RedM wymienia pliki indywidualnie w `fxmanifest.lua`, dodaj do jego sekcji `files` nowe pliki `vellum-shell.js`, `t2/vellum.css` i `assets/**/*`. Manifestu ani kodu Lua nie było w przesłanym archiwum.

Do podglądu w przeglądarce uruchom w tym katalogu `python3 -m http.server 8080` i otwórz `T4_KsiegaGladka.dc.html` przez ten serwer. Nie wymaga npm ani kompilacji. Fonty i grafiki są lokalne; interfejs nie pobiera zasobów z Google Fonts.

## Co zostało zachowane

- Oryginalna struktura Design Component (`x-dc`), React i `support.js`.
- Cztery przykładowe postacie oraz piąte wolne miejsce.
- Wybór postaci, otwieranie i zamykanie księgi, animacje stron oraz obsługa szybkiego przełączania.
- Ustawienie tempa animacji; wygląd materiałów księgi został zastąpiony nowymi teksturami.

Domyślnie otwarta jest karta Jessego, jak w koncepcie. Powrót do widoku ogólnego zamyka księgę; ponowny wybór postaci ją otwiera. Scena w tle jest dekoracyjna, zgodnie z koncepcją; nie jest podglądem modelu postaci z gry.

## Portrety

Dołączono 10 ciemnych portretów sylwetkowych: `assets/portraits/male-1.png` do `male-5.png` i `female-1.png` do `female-5.png`. Pole `female` wybiera zestaw, a numer slotu (1–5) wybiera obraz. Każdy slot ma własny wariant, więc zdjęcia nie powtarzają się nawet przy pięciu postaciach tej samej płci. Przypisanie jest stałe przy ponownym otwieraniu księgi; zmiana slotu zmienia przypisany portret.

Portrety są dodatkowo przyciemnione w `.card-portrait` w `t2/vellum.css`; celowo pokazują przede wszystkim sylwetki. Kadrowanie używa `object-fit: cover`.

Każda strona ma własną rycinę: 1 — ranczo, 2 — stacja kolejowa, 3 — górnicze miasteczko, 4 — leśna chata, 5 — przystań. Pliki to `assets/book-paper.png` oraz `book-paper-2.png` do `book-paper-5.png`. Rycinę wybiera numer strony, także podczas animacji przewracania. Piąta pojawi się, gdy zostanie obsadzony piąty slot; demonstracyjne wolne miejsce nadal wywołuje zdarzenie tworzenia postaci.

Tytuł na okładce korzysta z lokalnej czcionki Playfair Display, bez filtrów tekstur nakładanych na litery.

## Przyciski i integracja

Przesłana wersja miała logikę wyboru kart i animacji. Nie zawierała połączeń NUI `fetch`, `RegisterNUICallback`, obsługi danych z Lua ani funkcji faktycznego dołączania do gry/usuwania postaci. Nie da się zweryfikować tych operacji bez zasobu serwera.

Nowe przyciski udostępniają zdarzenie przeglądarkowe `vellum:action`. Zdarzenia same nie zmieniają danych na serwerze i nie usuwają postaci. Przykład podłączenia we własnym skrypcie integracji:

```js
window.addEventListener('vellum:action', event => {
  const { action, slot, character } = event.detail;
  // Wywołaj tutaj istniejący callback swojego zasobu RedM.
  // Nie zakładaj, że slot jest identyfikatorem postaci na serwerze.
});
```

Dostępne akcje:

- `play`: przycisk „Wejdź do gry”, wybrany slot i jego przykładowe dane.
- `delete-request`: żądanie usunięcia; integracja powinna potwierdzić i wykonać operację.
- `create`: kliknięcie wolnego miejsca; `character` ma wartość `null`.
- `exit-request`: przytrzymanie przycisku wyjścia przez 1,5 s myszą albo klawiszem Enter/Spacja. Puszczenie lub utrata fokusu przerywa odliczanie.

W zwykłej przeglądarce pojawia się dyskretny komunikat diagnostyczny, żeby nie sugerować, że kliknięcie faktycznie dołączyło do gry. Nazw callbacków RedM nie zgadywano.

## Pliki i modyfikacje

- `T4_KsiegaGladka.dc.html`: układ, portrety, domyślny wybór i zdarzenia przycisków.
- `t2/vellum.css`: nowa warstwa wizualna; bazowy `t2/almanach.css` pozostaje bez zmian.
- `vellum-shell.js`: proporcjonalne skalowanie planszy 1920 × 1080 i przytrzymanie przycisku wyjścia.
- `assets/frontier-scene.png`: wygenerowane tło inspirowane przesłanym konceptem.
- `assets/frontier-etching.svg`: dekoracyjna ilustracja farmy na kartach.
- `assets/book-leather.png` i `assets/book-paper.png`: tekstury zużytej skórzanej oprawy i pergaminu z ryciną, wygenerowane do drugiej wersji księgi.
- `assets/fonts/`: lokalne Playfair Display i Libre Baskerville wraz z licencjami OFL.

Sprawdzenie w Chromium obejmuje wybór kart, pieczęć, animacje, szybkie przełączanie, zamykanie/otwieranie księgi, zdarzenia przycisków, anulowanie przytrzymania, obsługę klawiatury i skalowanie przy rozdzielczościach 1280×720, 1366×768, 1669×936, 1920×1080, 2560×1440 oraz 2560×1080. Test w faktycznym CEF RedM wymaga serwera użytkownika.
