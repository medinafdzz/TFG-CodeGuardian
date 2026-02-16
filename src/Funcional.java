public class Funcion {

    //variable global
    private int Total = 0;

    //Mal manejo de excepciones / no implementadas
    public void dividir(int numerador, int denominador) {
        try {
            int resultado = numerador / denominador;
            System.out.println("El resultado es: " + resultado);
        } catch (ArithmeticException e) {
            //Devolvera un cero, lo cual es inapropiado
            return 0;
        }
    }

    // Acceso directo a variable global
    //Mala implementación, ya que otro metodo podria modificar el valor de Total sin control
    public void incrementarTotal(int valor) {
        Total += valor;
    }

    public int getTotal() {
        return Total;
    }
}
