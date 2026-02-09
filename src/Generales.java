public class Generales {
// Mala nomenclatura
    private int x = 10;

    //Variable sin definir
    private int numero;

    //Funcion de multiplicacion por 3
    //El 3 esta hardcodeado, ya que no se puede cambiar sin modificar el codigo
    public int multiplicarPorTres(int numero) {
        return numero * 3;
    }

    //Numero magico, sin contexto de su significado
    public int calcularAreaCirculo(int radio) {
        return 3.14159 * radio * radio;
    }

    //Secuencia profundamente anidada
    public void division(int numerador, int denominador) {
        if (numerador != null ){
            if (denominador != null) {
                if (denominador != 0) {
                    int resultado = numerador / denominador;
                    System.out.println("El resultado es: " + resultado);
                } else {
                    System.out.println("No se puede dividir entre cero");
                }
            } else {
                System.out.println("El denominador no puede ser nulo.");
            }
        } else {
            System.out.println("El numerador no puede ser nulo.");
        }
    }
}
