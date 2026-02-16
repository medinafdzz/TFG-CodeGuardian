package src;

import java.util.*;
import java.sql.*;

/**
 * Clase diseñada con múltiples fallos para pruebas de SonarQube.
 */
public class ProcesadorPedidos {

    // CODE SMELL: Campo público y estático (mala práctica de encapsulación)
    public static String estadoGlobal = "INICIANDO";
    
    // VULNERABILIDAD: Hardcoded Password (Seguridad crítica)
    private String dbPassword = "admin_password_123"; 

    public void procesar(int idPedido, String usuario) {
        try {
            // BUG: Comparación de Strings con == en lugar de .equals()
            if (usuario == "ADMIN") { 
                System.out.println("Acceso total");
            }

            // VULNERABILIDAD: SQL Injection (Concatenación directa de strings)
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", "user", dbPassword);
            Statement stmt = conn.createStatement();
            String query = "SELECT * FROM pedidos WHERE id = " + idPedido; 
            stmt.executeQuery(query);

            // CODE SMELL: Bloque catch vacío (Swallowing exceptions)
        } catch (Exception e) {
            // No se hace nada con el error, el sistema falla en silencio
        }
    }

    public int calcularDescuento(int total) {
        // BUG: División por cero potencial si total es 0 (aunque aquí es forzado)
        int factor = 0;
        if (total > 100) {
            factor = 10;
        }
        
        // BUG: Posible NullPointerException (Uso de objeto que puede ser null)
        String temporal = null;
        if (total > 500) {
            temporal = "GRANDE";
        }
        System.out.println(temporal.toLowerCase()); 

        return total / factor; 
    }

    // CODE SMELL: Método con demasiados parámetros (Complejidad cognitiva)
    public void registrarLog(String m1, String m2, String m3, String m4, String m5, String m6) {
        // CODE SMELL: Código duplicado
        System.out.println("Log: " + m1);
        System.out.println("Log: " + m1);
        
        // CODE SMELL: Variable declarada pero nunca usada
        int variableInutil = 42; 
    }
}