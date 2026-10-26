

## Kurs programowania obiektowego 2021

https://github.com/teamWSIZ/oop-2021/network

#Forked

Nothing to see here!

## Interaktywny podgląd Vellum RedM NUI

![Podgląd interfejsu Vellum](docs/podglad.png)

[Okładka księgi](docs/okladka.png) · [10 sylwetek i 5 rycin](docs/warianty.png)

Pełna strona wraz z grafikami i fontami znajduje się w [`docs`](docs). Nie wymaga npm ani kompilacji. Można wybierać karty postaci, przewracać strony księgi i sprawdzać przyciski. Działanie przycisków w przeglądarce jest demonstracyjne; nie łączy z serwerem RedM.

### Podgląd online przez GitHub Pages

Jednorazowo w tym repozytorium otwórz **Settings → Pages → Build and deployment**:

1. **Source:** `Deploy from a branch`.
2. **Branch:** `codex/vellum-redm-nui`.
3. **Folder:** `/docs`.
4. Kliknij **Save** i poczekaj, aż GitHub zakończy publikację.

Docelowy adres: **https://xanox4512.github.io/oop-2021/**. Adres zacznie działać dopiero po włączeniu i pomyślnym opublikowaniu GitHub Pages. Status publikacji i aktualny adres GitHub pokaże w **Settings → Pages**. Ten podgląd nie wymaga scalania zmian do `master`.

### Podgląd lokalny

Po sklonowaniu repozytorium i przełączeniu na `codex/vellum-redm-nui` uruchom:

```sh
python3 -m http.server 8080 --directory docs
```

Następnie otwórz `http://localhost:8080` w przeglądarce. Serwer należy uruchomić w głównym katalogu repozytorium. Szczegóły interfejsu i zdarzeń przycisków: [`docs/README.md`](docs/README.md).

Gotowa paczka do pobrania: [`Vellum-RedM-NUI.zip`](Vellum-RedM-NUI.zip).
