
from Aufgabe1 import Aufgabe1_Beispiel as a_1
import Aufgabe3 as a_3

def main():
    from Aufgabe2_ordner import Aufgabe2 as a_2

    print("=============Aufgabe1============")
    
    
    a_1.Aufgabe1_Beispiel()
    
    print("=============Aufgabe2============")
    
    
    print("---Aufgabe2 a---")
    
    a_2.aufgabe_2_a()
    print("---Aufgabe2 b---")
    
    a_2.aufgabe_2_b()
    print("---Aufgabe2 c---")
    
    print("Interpretation der numerischen Verfahren:")
    print("1. Explizites Euler-Verfahren:")
    print("- Konsistenzordnung 1: Fehler O(tau)")
    print("- Größere Schrittweiten führen zu stärkeren Abweichungen.")
    print("- Geschlossene Bahnen werden nicht exakt erhalten.")
    print()
    print("2. Explizites Heun-Verfahren:")
    print("- Konsistenzordnung 2: Fehler O(tau^2)")
    print("- Deutlich genauer als Euler bei gleicher Schrittweite.")
    print()
    print("3. Runge-Kutta-Verfahren 3. Ordnung:")
    print("- Konsistenzordnung 3: Fehler O(tau^3)")
    print("- Erwartungsgemäß genaueste Ergebnisse bei gleicher Schrittweite.")
    print()
    print("Analytische Einsicht:")
    print("- Stationärer Punkt: (x,y) = (1,1)")
    print("- Der Gleichgewichtspunkt ist ein Zentrum.")
    print("- Analytische Lösungen verlaufen auf geschlossenen Bahnen.")
    print("- Numerische Verfahren erhalten diese Struktur nicht exakt.")
    
    print("=============Aufgabe3============")
    
    
    a_3.Aufgabe3()
    print("---Aufgabe3 d---")# a bis c im aufgebe 3 befehl 
    
    print("Euler:\n- Geringer Rechenaufwand pro Zeitschritt.\n- Konvergenzordnung 1.\n- Für hohe Genauigkeit werden viele Zeitschritte benötigt.")
    print("Heun:\n- Etwas höherer Rechenaufwand pro Zeitschritt.\n- Konvergenzordnung 2.\n- Bessere Genauigkeit bei gleicher Schrittweite.")
    print("Runge-Kutta 3:\n- Höherer Rechenaufwand pro Zeitschritt.\n- Konvergenzordnung 3.\n- Bei ausreichend kleinen Schrittweiten normalerweise die beste Genauigkeit.")
    
    
    
if __name__ == "__main__":
    main()