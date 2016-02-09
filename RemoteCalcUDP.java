import java.io.*;
import java.net.*;

/*
 * Richard Farr (rfarr6)
 * CS 3251
 * 9/21/2014
 * Project 1
 */

class RemoteCalcUDP {
    public static void main(String[] args) throws Exception {

        // Parse input ip and port
        String[] dest = args[0].split(":");
        String query = "";

        // Construct query
        for (int i = 1; i < args.length; i++) {
            query += args[i];
            if (i != args.length-1) query += " ";
        }

        // Create UDP object and set timeout = 2 seconds
        DatagramSocket sock = new DatagramSocket();
        sock.setSoTimeout(2000);

        // Create InetSocketAddress object, which contains ip and port
        InetAddress dest_ip = InetAddress.getByName(dest[0]);
        InetSocketAddress dest_addr = new InetSocketAddress(dest_ip, Integer.parseInt(dest[1]));

        // Create output byte array and buffer for receiving response
        byte[] outData = query.getBytes();
        byte[] inData = new byte[32];

        // Create packet objects and bind to their respective buffers
        DatagramPacket sendPacket = new DatagramPacket(outData, outData.length, dest_addr);
        DatagramPacket receivePacket = new DatagramPacket(inData, inData.length);

        while (true) {

            // Send packet
            sock.send(sendPacket);

            // Attempt to receive packet and print reponse. Timeout will raise an exception.

            try {
                sock.receive(receivePacket);
                String response = new String(receivePacket.getData());
                System.out.println("From server:" + response);
                sock.close();
                break;
            } catch (SocketTimeoutException e) {
                System.out.println("The server has not answered in 2 seconds.");
                System.out.println("Enter 'retry' to resend the message or 'exit' to exit the application:");

                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                String resp = reader.readLine();

                if (!resp.equals("retry")) break;
            }
        }
    }
}

