import java.util.Random;

public class Picasso{
    public Picasso(){

    }
    public void paint(int width, int height, int anzahlThreads){
        //initialisiere dir eine Leinwand (Canvas)
        Canvas canvas = new Canvas(width,height);
        //erzeuge dir threads-viele Painter-Arbeitspakete und lasse sie von threads-vielen Threads abarbeiten
        //der main-Thread wartet auf die Maler bis diese das Gemälde fertiggestellt haben
        Thread[] t = new Thread[anzahlThreads];
        for (int i = 0; i < anzahlThreads; i++) {
            t[i] = new Thread(new Painter(canvas, i, width, height));
        }
        for (int i = 0; i < anzahlThreads; i++) {
            t[i].start();
        }
        for (int i = 0; i < anzahlThreads; i++) {
            try {
                t[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
    
    public static void main(String[] args){
        int width = 50;
        int height = 50;
        int anzahlThreads = 10;
        new Picasso().paint(width, height, anzahlThreads);
    }
    
}
//Schreibe eine Klasse Painter implements Runnable, die die Leinwand parallelisiert vollmalen soll
//1.) Konstruktor: Übergebe der Klasse Painter alle nötigen Referenzen und Variablen
//2.1) Algorithmus: Solange die Leinwand noch nicht vollgemalt ist, soll sich ein zufälliges Feld auf der Leinwand ausgesucht werden: java.util.Random
//2.2) Ist dieses noch nicht bemalt, soll der Painter mit seiner eigenen Farbe auf dieses Feld malen
//Hinweis: Die Farben sind als Zahlen kodiert, d.h. der Painter soll sie mit seiner Nummer/id bemalen
//Tipp: Nutze hierfür die Methoden finished() hascolor() colorize() der Klasse Canvas sowie nextInt() der Klasse Random; siehe API und Klasse Canvas
class Painter implements Runnable{
    Canvas canvas;
    int farbe;
    int width;
    int height;
    Random r;

    public Painter(Canvas c, int i, int w, int h){
        canvas = c;
        farbe = i;
        width = w;
        height = h;
        r = new Random();
    }

    @Override
    public void run() {
        while(!canvas.finished()){
            int x = r.nextInt(width);
            int y = r.nextInt(height);
            synchronized (canvas) {
                if (canvas.hasColor(x, y) == false) {
                    canvas.colorize(x, y, farbe);
                }
            }
        }
    }
}
    