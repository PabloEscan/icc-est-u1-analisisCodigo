import java.util.Random;


public class Benchmarking {
    
    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking(){
        long currentMilis = System.currentTimeMillis();     //Sacar fecha, usa la fecha epoch
        long currentNano = System.nanoTime();               //Inicia desde que se ejecuto el computador

        System.out.println(currentMilis);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100_000_000);
        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMilis = medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano = medidorConNanoTime(tarea);

        System.out.println("Tiempo en milisegundos: "+ tiempoDuracionMilis);
        System.out.println("Tiempo en nanosegundos: " + tiempoDuracionNano);
    }

    public int[] generarArregloAleatorio(int tamaño){
        int[] array= new int[tamaño];
        Random random = new Random();
        for(int i=0; i < tamaño; i++){
            array[i] = random.nextInt(10000000);
        }
        return array;
    }

    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }

    public double medidorConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
}
