
/**
 * Gibt mehrere Graphen zum Testen vor 
 * 
 * @author Joachim Hofmann
 * @version 1.0
 */
public class TESTGRAPHEN{
    public static GRAPH<STADT> graphPraesentationTiefensucheStartBei0(){
        GRAPH<STADT> a = new GRAPH<STADT>(6);
        a.neuerKnoten(new STADT("0"));
        a.neuerKnoten(new STADT("1"));
        a.neuerKnoten(new STADT("2"));
        a.neuerKnoten(new STADT("3"));
        a.neuerKnoten(new STADT("4"));
        a.neuerKnoten(new STADT("5"));
        a.neueKanteUngerichtet("0","1",1);
        a.neueKanteUngerichtet("0","4",1);
        a.neueKanteUngerichtet("0","3",1);
        a.neueKanteUngerichtet("3","2",1);
        a.neueKanteUngerichtet("4","2",1);
        a.neueKanteUngerichtet("2","5",1);
        return a;
    }

    public static GRAPH<STADT> graphAufgabe5und6(){
        GRAPH<STADT> a = new GRAPH<STADT>(10);
        a.neuerKnoten(new STADT("a"));
        a.neuerKnoten(new STADT("b"));
        a.neuerKnoten(new STADT("c"));
        a.neuerKnoten(new STADT("d"));
        a.neuerKnoten(new STADT("e"));
        a.neuerKnoten(new STADT("f"));
        a.neuerKnoten(new STADT("g"));
        a.neuerKnoten(new STADT("h"));
        a.neuerKnoten(new STADT("j"));
        a.neuerKnoten(new STADT("k"));
        a.neueKanteUngerichtet("a","b",1);
        a.neueKanteUngerichtet("a","c",1);
        a.neueKanteUngerichtet("b","d",1);
        a.neueKanteUngerichtet("b","e",1);
        a.neueKanteUngerichtet("d","h",1);
        a.neueKanteUngerichtet("e","f",1);
        a.neueKanteUngerichtet("c","f",1);
        a.neueKanteUngerichtet("c","g",1);
        a.neueKanteUngerichtet("f","g",1);
        a.neueKanteUngerichtet("f","j",1);
        a.neueKanteUngerichtet("f","k",1);
        return a;
    }

    public static GRAPH<STADT> graphBreitendurchlaufFehlerStartBeiLandshut(){
        GRAPH<STADT> a = new GRAPH<STADT>(10);
        a.neuerKnoten(new STADT("Muenchen"));
        a.neuerKnoten(new STADT("Landshut"));
        a.neuerKnoten(new STADT("Deggendorf"));
        a.neuerKnoten(new STADT("Passau"));
        a.neuerKnoten(new STADT("Straubing"));
        a.neuerKnoten(new STADT("Regensburg"));
        a.neuerKnoten(new STADT("Ingolstadt"));
        a.neuerKnoten(new STADT("Greding"));
        a.neuerKnoten(new STADT("Nuernberg"));
        a.neuerKnoten(new STADT("Bayreuth"));
        a.neueKanteUngerichtet("Muenchen","Landshut",1);
        a.neueKanteUngerichtet("Landshut","Deggendorf",1);
        a.neueKanteUngerichtet("Deggendorf","Passau",1);
        a.neueKanteUngerichtet("Deggendorf","Straubing",1);
        a.neueKanteUngerichtet("Straubing","Regensburg",1);
        a.neueKanteUngerichtet("Ingolstadt","Greding",1);
        a.neueKanteUngerichtet("Greding","Nuernberg",1);
        a.neueKanteUngerichtet("Nuernberg","Bayreuth",1);
        return a;
    }

    public static GRAPH<STADT> graphDijkstraSkript(){
        GRAPH<STADT> a = new GRAPH<STADT>(6);
        a.neuerKnoten(new STADT("a"));
        a.neuerKnoten(new STADT("b"));
        a.neuerKnoten(new STADT("c"));
        a.neuerKnoten(new STADT("d"));
        a.neuerKnoten(new STADT("e"));
        a.neuerKnoten(new STADT("f"));
        a.neueKanteUngerichtet("a","b",2);
        a.neueKanteUngerichtet("a","c",5);
        a.neueKanteUngerichtet("a","d",1);
        a.neueKanteUngerichtet("b","d",2);
        a.neueKanteUngerichtet("b","c",3);
        a.neueKanteUngerichtet("c","d",3);
        a.neueKanteUngerichtet("c","e",1);
        a.neueKanteUngerichtet("c","f",5);
        a.neueKanteUngerichtet("d","e",1);
        a.neueKanteUngerichtet("e","f",2);
        return a;
    }

    public static GRAPH<STADT> graphLabyrinthStartBeist(){
        GRAPH<STADT> a = new GRAPH<STADT>(18);
        a.neuerKnoten(new STADT("st"));
        a.neuerKnoten(new STADT("a"));
        a.neuerKnoten(new STADT("b"));
        a.neuerKnoten(new STADT("c"));
        a.neuerKnoten(new STADT("d"));
        a.neuerKnoten(new STADT("e"));
        a.neuerKnoten(new STADT("f"));
        a.neuerKnoten(new STADT("g"));
        a.neuerKnoten(new STADT("h"));
        a.neuerKnoten(new STADT("i"));
        a.neuerKnoten(new STADT("j"));
        a.neuerKnoten(new STADT("k"));
        a.neuerKnoten(new STADT("l"));
        a.neuerKnoten(new STADT("m"));
        a.neuerKnoten(new STADT("n"));
        a.neuerKnoten(new STADT("o"));
        a.neuerKnoten(new STADT("p"));
        a.neuerKnoten(new STADT("zi"));
        a.neueKanteUngerichtet("st","a",1);
        a.neueKanteUngerichtet("a","b",1);
        a.neueKanteUngerichtet("a","d",1);
        a.neueKanteUngerichtet("b","c",1);
        a.neueKanteUngerichtet("b","i",1);
        a.neueKanteUngerichtet("d","g",1);
        a.neueKanteUngerichtet("d","e",1);
        a.neueKanteUngerichtet("e","f",1);
        a.neueKanteUngerichtet("h","i",1);
        a.neueKanteUngerichtet("i","p",1);
        a.neueKanteUngerichtet("j","zi",1);
        a.neueKanteUngerichtet("j","m",1);
        a.neueKanteUngerichtet("k","m",1);
        a.neueKanteUngerichtet("l","n",1);
        a.neueKanteUngerichtet("m","n",1);
        a.neueKanteUngerichtet("n","p",1);
        a.neueKanteUngerichtet("p","o",1);
        a.neueKanteUngerichtet("j","e",1);
        return a;
    }

    public static GRAPH<STADT> graphAutobahn(){
        GRAPH<STADT> a = new GRAPH<STADT>(10);
        a.neuerKnoten(new STADT("BT"));
        a.neuerKnoten(new STADT("N"));
        a.neuerKnoten(new STADT("R"));
        a.neuerKnoten(new STADT("DON"));
        a.neuerKnoten(new STADT("IN"));
        a.neuerKnoten(new STADT("LA"));
        a.neuerKnoten(new STADT("A"));
        a.neuerKnoten(new STADT("M"));
        a.neuerKnoten(new STADT("PA"));
        a.neuerKnoten(new STADT("DEG"));
        a.neueKanteUngerichtet("BT","N",90);
        a.neueKanteUngerichtet("N","DON",100);
        a.neueKanteUngerichtet("N","R",100);
        a.neueKanteUngerichtet("N","IN",110);
        a.neueKanteUngerichtet("DON","IN",60);
        a.neueKanteUngerichtet("DON","A",45);
        a.neueKanteUngerichtet("IN","R",70);
        a.neueKanteUngerichtet("IN","LA",54);
        a.neueKanteUngerichtet("IN","A",80);
        a.neueKanteUngerichtet("LA","R",65);
        a.neueKanteUngerichtet("R","DEG",70);
        a.neueKanteUngerichtet("DEG","PA",50);
        a.neueKanteUngerichtet("LA","M",70);
        a.neueKanteUngerichtet("IN","M",55);
        a.neueKanteUngerichtet("A","M",80);
        a.neueKanteUngerichtet("DEG","LA",70);
        return a;
    }

    public static GRAPH<STADT> graphAutobahnErweitert(){
        GRAPH<STADT> a = new GRAPH<STADT>(50);
        //TODO weiterausbauen
        a.neuerKnoten(  new STADT("Muenchen") );
        a.neuerKnoten(  new STADT("Landshut")  );
        a.neueKanteUngerichtet( "Muenchen" , "Landshut" , 73 );
        a.neuerKnoten(  new STADT("Deggendorf")  );
        a.neueKanteUngerichtet("Landshut" , "Deggendorf" , 73 );
        a.neuerKnoten(  new STADT("Passau") );
        a.neueKanteUngerichtet( "Deggendorf" , "Passau" , 54 );
        a.neuerKnoten(  new STADT("Straubing")  );
        a.neueKanteUngerichtet( "Deggendorf" , "Straubing" , 35 );
        a.neuerKnoten(  new STADT("Regensburg")  );
        a.neueKanteUngerichtet( "Regensburg" , "Straubing" , 47 );
        a.neuerKnoten(  new STADT("Ingolstadt") );
        a.neuerKnoten( new STADT("Greding") );
        a.neueKanteUngerichtet( "Ingolstadt", "Greding" , 39 );
        a.neuerKnoten( new STADT("Bayreuth") );
        a.neuerKnoten( new STADT("Nuernberg") );
        a.neueKanteUngerichtet( "Nuernberg" , "Greding" , 57 );
        a.neueKanteUngerichtet( "Nuernberg" , "Bayreuth" , 51 );
        a.neuerKnoten(  new STADT("Neumarkt (OPf)") );
        a.neueKanteUngerichtet( "Neumarkt (OPf)" ,"Nuernberg" , 48 );
        a.neueKanteUngerichtet( "Neumarkt (OPf)" ,"Regensburg" , 71 );
        a.neuerKnoten(  new STADT("Donauwoerth") );
        a.neuerKnoten( new STADT("Augsburg") );
        a.neueKanteUngerichtet( "Donauwoerth" , "Augsburg" , 44 );
        a.neueKanteUngerichtet( "Muenchen", "Augsburg" , 80 );
        a.neueKanteUngerichtet("Augsburg", "Ingolstadt", 60);
        a.neuerKnoten(  new STADT("Dreieck Landsberg") );
        a.neueKanteUngerichtet( "Dreieck Landsberg" ,"Augsburg" , 42 );
        a.neueKanteUngerichtet( "Muenchen" , "Dreieck Landsberg", 61 );
        a.neuerKnoten(  new STADT("Kreuz Memmingen") );
        a.neueKanteUngerichtet( "Kreuz Memmingen" , "Dreieck Landsberg" , 59 );
        a.neuerKnoten(  new STADT("Ulm") );
        a.neueKanteUngerichtet( "Ulm" , "Kreuz Memmingen" , 59 );
        a.neueKanteUngerichtet( "Ulm" , "Dreieck Landsberg" , 88 );
        a.neuerKnoten(  new STADT("Heidenheim") );
        a.neueKanteUngerichtet( "Heidenheim" , "Ulm" , 55 );
        a.neuerKnoten(  new STADT("Kreuz Feuchtwangen") );
        a.neueKanteUngerichtet( "Kreuz Feuchtwangen" , "Heidenheim" , 72 );
        a.neueKanteUngerichtet( "Kreuz Feuchtwangen" , "Nuernberg" , 91 );
        return a;
    }
}
