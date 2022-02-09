
/**
 * Klasse Taxi_Schlangen_TESTER.
 * 
 * @author      Joachim Hofmann
 * @version     1.0
 */
public class Taxi_Schlangen_TESTER
{
    private TAXI_SCHLANGE ts;
    

    /**
     * Konstruktor für Objekte der Klasse Taxi_Schlangen_TESTER
     */
    public Taxi_Schlangen_TESTER()
    {
        // Schlange der Laenge 3 erzeugen
        
        System.out.println("TEST startet: ------------------------");
        System.out.println();
        this.ts = new TAXI_SCHLANGE(3);
        System.out.println("Neue Taxischlange der Laenge 3 erzeugt");
        if ( this.ts.istLeer() ) {
            System.out.println("Die Schlange ist leer");
        }
        else {
            System.out.println("FEHLER bei Methode'istLeer()' !!!");
        }
        System.out.println();
        
        // 3 Taxis erzeugen und einreihen
        
        System.out.println("--- Erzeuge 3 Taxis und reihe sie ein:");
        System.out.println();
        
        boolean b0 = true;
        TAXI t1 = new TAXI("EVBG T 1");
        System.out.println("Neues Taxi 'EVBG T 1' erzeugt");
        boolean b1 = this.ts.hintenEinreihen(t1);
        if (b1) {
            System.out.println("Taxi 'EVBG T 1' hinten eingereiht");
        }
        else {
            System.out.println("Einreihen von Taxi 1 FEHLGESCHLAGEN !!!");
        }
        if ( this.ts.nenneAnzahl() == 1 ) {
            System.out.println("Es ist 1 Taxi in der Schlange");
        }
        else {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b0 = false;
        }
        System.out.println();
        
        TAXI t2 = new TAXI("EVBG T 2");
        System.out.println("Neues Taxi 2 erzeugt");
        boolean b2 = this.ts.hintenEinreihen(t2);
        if (b2) {
            System.out.println("Taxi 'EVBG T 2' hinten eingereiht");
        }
        else {
            System.out.println("Einreihen von Taxi 2 FEHLGESCHLAGEN !!!");
        }
        if ( this.ts.nenneAnzahl() == 2 ) {
            System.out.println("Es sind 2 Taxis in der Schlange");
        }
        else {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b0 = false;
        }
        System.out.println();
        
        TAXI t3 = new TAXI("EVBG T 3");
        System.out.println("Neues Taxi 'EVBG T 3' erzeugt");
        boolean b3 = this.ts.hintenEinreihen(t3);
        if (b3) {
            System.out.println("Taxi 'EVBG T 3' hinten eingereiht");
        }
        else {
            System.out.println("Einreihen von Taxi 3 FEHLGESCHLAGEN !!!");
        }
        if ( this.ts.nenneAnzahl() == 3 ) {
            System.out.println("Es sind 3 Taxis in der Schlange");
        }
        else {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b0 = false;
        }
        System.out.println();
        
        // weiteres Taxi in volle Schlange einreihen
        
        System.out.println("--- Versuche ein Taxi zu viel einzureihen:");
        System.out.println();
        
        TAXI t4 = new TAXI("EVBG T 4");
        System.out.println("Neues Taxi 4 erzeugt");
        boolean b4 = this.ts.hintenEinreihen(t4);
        if (b4) {
            System.out.println("FEHLER bei voller Schlange !!!");
        }
        else {
            System.out.println("Schlange voll, Taxi kann nicht eingereiht werden");
        }
        boolean b5 = true;
        if ( this.ts.nenneAnzahl() != 3 ) {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b5 = false;
        }
        System.out.println();
        
        // Taxis wieder abfahren lassen
        System.out.println("--- Taxis wieder abfahren lassen:");
        System.out.println();
        
        t1 = this.ts.vorneEntnehmen();
        boolean b6 = t1.nenneKFZ().equals("EVBG T 1");
        if (b6) {
            System.out.println("Taxi mit KFZ 'EVBG T 1' abgefahren");
        }
        else {
            System.out.println("FEHLER !!! Taxi mit KFZ '" + t1.nenneKFZ() + "' abgefahren");
        }
        if ( this.ts.nenneAnzahl() != 2) {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
        }
        System.out.println();
        
        t2 = this.ts.vorneEntnehmen();
        boolean b7 = t2.nenneKFZ().equals("EVBG T 2");
        if (b7) {
            System.out.println("Taxi mit KFZ 'EVBG T 2' abgefahren");
        }
        else {
            System.out.println("FEHLER !!! Taxi mit KFZ '" + t2.nenneKFZ() + "' abgefahren");
        }
        if ( this.ts.nenneAnzahl() != 1) {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
        }
        System.out.println();
        
        t3 = this.ts.vorneEntnehmen();
        boolean b8 = t3.nenneKFZ().equals("EVBG T 3");
        if (b8) {
            System.out.println("Taxi mit KFZ 'EVBG T 3' abgefahren");
        }
        else {
            System.out.println("FEHLER !!! Taxi mit KFZ '" + t3.nenneKFZ() + "' abgefahren");
        }
        boolean b9 = true;
        if ( this.ts.nenneAnzahl() != 0) {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b9 = false;
        }
        System.out.println();
        
        if ( !this.ts.istLeer() ) {
            System.out.println("FEHLER bei Methode 'istLeer()' !!!");
            b9 = false;
        }
        else {
            System.out.println("Die Schlange ist leer");
        }
        System.out.println();
        
        // Versuch, Taxi aus leerer Schlange zu entnehmen
        
        System.out.println("--- Versuche Taxi aus leerer Schlange zu entnehmen:");
        System.out.println();
        
        t4 = this.ts.vorneEntnehmen();
        boolean b10 = true;
        if ( t4 == null ) {
            System.out.println("Kann kein Taxi aus leerer Schlange entnehmen");
        }
        else {
            System.out.println("FEHLER beim Entnehmen aus leerer Schlange !!!");
            b10 = false;
        }
        if ( this.ts.nenneAnzahl() == 0 ) {
            System.out.println("Die Schlange ist und bleibt leer");
        }
        else {
            System.out.println("FEHLER bei Methode 'nenneAnzahl()' !!!");
            b10 = false;
        }
        System.out.println();
        
        // Zusammenfassung
        
        System.out.println("---------------------------------------");
        System.out.println("Zusammenfassung:");
        System.out.println();
        if (b0 && b1 && b2 && b3) {
            System.out.println("Einreihen fehlerfrei    :-)");
        }
        else {
            System.out.println("FEHLER beim Einreihen der Taxis    :-(");
        }
        if (!b4 && b5) {
            System.out.println("Ueberladen der Schlange nicht moeglich    :-)");
        }
        else {
            System.out.println("FEHLER beim Ueberladen der Schlange    :-(");
        }
        if (b6 && b7 && b8 && b9) {
            System.out.println("Entnehmen fehlerfrei    :-)");
        }
        else {
            System.out.println("FEHLER beim Entnehmen der Taxis    :-(");
        }
        if (b10) {
            System.out.println("Entnehmen bei leerer Schlange nicht moeglich    :-)");
        }
        else {
            System.out.println("FEHLER beim Entnehmen aus leerer Schlange    :-(");
        }
    }
    
    
    
}
