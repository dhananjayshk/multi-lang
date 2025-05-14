import java.net.*;
import java.io.*;

public class App {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8082);
        System.out.println("Starting Java service on port 8082");

        while (true) {
            Socket socket = serverSocket.accept();
            new Thread(() -> {
                try {
                    BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null && !line.isEmpty()) {}

                    String response = "HTTP/1.1 200 OK\r\nContent-Length: 16\r\n\r\nHello from Java!";
                    socket.getOutputStream().write(response.getBytes());
                    socket.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
}
