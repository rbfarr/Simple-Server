import java.io.*;
import java.net.*;

/*
 * Richard Farr (rfarr6)
 * CS 3251
 * 9/21/2014
 * Project 1
 */

class RemoteCalcTCP {
    public static void main(String[] args) throws Exception {

        // Parse input ip and port
        String[] dest = args[0].split(":");
        String query = "";

        // Construct query
        for (int i = 1; i < args.length; i++) {
            query += args[i];
            if (i != args.length-1) query += " ";
        }

        // Create TCP socket

        Socket sock;

        try {
            sock = new Socket(dest[0], Integer.parseInt(dest[1]));
        } catch (ConnectException e) {
            System.out.println("unable to connect to server");
            return;
        }

        // Setup input and output streams
        PrintWriter out = new PrintWriter(sock.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(sock.getInputStream()));

        // Send query to server, and block until response is ready
        out.printf(query);
        while (!in.ready()) {}

        // Print result, and close socket
        System.out.println("From server: " + in.readLine());
        sock.close();
    }
}
