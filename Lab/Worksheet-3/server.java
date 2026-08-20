import java.io.*;
import java.net.*;
public class Server {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8000);
            System.out.println("Server is waiting for client...");
            Socket socket = serverSocket.accept();
            System.out.println("Client connected.");
            FileInputStream fis = new FileInputStream(args[0]);
            OutputStream os = socket.getOutputStream();
            int ch;
            while ((ch = fis.read()) != -1) {
                os.write(ch);
            }
            System.out.println("File sent successfully.");
            fis.close();
            os.close();
            socket.close();
            serverSocket.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}