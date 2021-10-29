### Obiektowe klasy opisujące komputery PC (wolnostojące i laptopy)

- wykorzystać strukturę dziedziczenia 
- elemety typowe: 
   1. motherboard(1), 
   2. cpu(1),  
   3. memory_chip (DDR4, SODIMM, buffered-RAM) ... bank1..4,
   4. hard_drive (sata1..4), 
   5. pcie (3), 
   6. GPU (1)
  
- ustawić konstruktory tak by całość dało się spiąć poprawnie
- napisać kilka metod do operowania komputerem, i ukryć jego 
  zmienne (prywatne) tak by nie można było całośći "rozwalić"
  

User stories: 
- mamy PC, przy konstrukcji musimy podać MB, oraz CPU, List[RAM], GPU na PCIe
  ↑↑ to w konstuktorze
  
- PC powinien mieć własność running/not-running
- przy wyłączonym można wymianiać wszystko.... ale metodami, nie przez zmianę zmiennych
- metody powinny brać pozycję na którą instalujemy sprzęt
- powinny być dostępne gettery by sprawdzić co gdzie jest zamontowane



