public class Clase {

//Mal uso de la herencia
public class Calculadora extends java.util.ArrayList<Integer> {

    public void sumarYGuardar(int a, int b) {
        int resultado = a + b;
        this.add(resultado);
    }
}

//Clase que solo guarda resultados, sin funcionalidad adicional
public class DatosResultado {
    private int valor;
    private String autor;

    public int getValor() { return valor; }
    public void setValor(int valor) { this.valor = valor; }
    public String getAutor() { return autor; }
    public void setAutor(String autor) { this.autor = autor; }
}
}
