
## Zadanie

Zadania polegają na napisaniu programów zbierających/parsujących 
metryki systemowe. Zazwyczaj metryki te dostajemy
albo wykonując komendy, albo czytając bezpośrednio z plików.

Dla uproszczenia wyniki wykonania komend umieściliśmy 
w folderach logs_*. 

Dla czterech przypadków: cpu_mhz, cpu_temp, nvme i net
trzeba napisać programy czytające plik lub wykonujące komendę
a następnie parsujące odpowiedź i zwracające dict[str,int].

Metryki: 

### cpu temp
Zbiera temperatury procesora. Jest różnica między procesorami
Intela i AMD. Dla AMD interesuje nas pojedyncza wartość

`Tdie:         +41.0°C`

w postaci pojedynczej liczby float dla klucza `cpu_temp`. 
Dla Intela dostajemy temperatury per core, więc parser powinien wyliczyć
ich średnią:

```
Package id 0:  +29.0°C  (high = +82.0°C, crit = +100.0°C)
Core 0:        +28.0°C  (high = +82.0°C, crit = +100.0°C)
Core 1:        +29.0°C  (high = +82.0°C, crit = +100.0°C)
Core 2:        +29.0°C  (high = +82.0°C, crit = +100.0°C)
Core 3:        +29.0°C  (high = +82.0°C, crit = +100.0°C)
Core 4:        +29.0°C  (high = +82.0°C, crit = +100.0°C)
Core 5:        +28.0°C  (high = +82.0°C, crit = +100.0°C)
```

pozostałe metryki proszę zignorować. 


### cpu_mhz
Tu dostajemy częstości dla każdego z core'ów procesora. Np. dla 
24-threadowego procesora dostajemy de facto 24 liczby float. Parser
powinien brać w konstruktorze 2 argumenty: `freq_idle` i `freq_boosted`, i na ich
podstawie podać ile % core'ów procesora jest aktualnie w stanie `idle` (<=`freq_idle`), ile w stanie
`boosted` (>=`freq_boosted`, i ile w stanie `normal` (między obydwoma).


### nvme
Komenda `nvme smart-log` daje wgląd w aktualne parametry działania dysków NVMe. 
Kluczowe parametry które nas interesują to: 
```
critical_warning
temperature
data_units_written
percentage_used
power_cycles
temperature_sensor_1
temperature_sensor_2
thermal_management_t1_trans_count
thermal_management_t2_trans_count
thermal_management_t1_total_time
thermal_management_t2_total_time
```
Trzeba przeparsować podane pliki i zwrócić wartości powyższych metryk jako liczb całkowitych. 

### net
Tego parsera zostawmy jako wstępny przykład jak parsować te pliki: czytamy linia po linii
i szukamy wybranych fraz, ucinamy zbędne spacje i niewidoczne znaczki etc, tak by 
ostatecznie dostać te liczby które nas interesują. 


