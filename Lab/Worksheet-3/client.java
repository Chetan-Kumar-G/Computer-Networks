import java.io.*;
import java.net.*;
public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 8000);
            System.out.println("Connected to server.");
            InputStream is = socket.getInputStream();
            FileOutputStream fos = new FileOutputStream(args[0]);
            int ch;
            while ((ch = is.read()) != -1) {
                fos.write(ch);
            }
            System.out.println("File received successfully.");
            fos.close();
            is.close();
            socket.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}