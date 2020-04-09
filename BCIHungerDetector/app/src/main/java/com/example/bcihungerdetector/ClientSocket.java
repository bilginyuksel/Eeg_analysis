package com.example.bcihungerdetector;

import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraManager;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class ClientSocket extends Thread {

    private static final String TAG = "SOCKET";
    private Socket socket ;
    private BufferedReader bufferedReader ;
    private OutputStream outputStream;
    private String address;
    private int port;

    private CameraManager cameraManager;
    private String cameraId;

    private Handler listHandler, statusHandler, resultIndexHandler;
    private Message listMessage, statusMessage, resultIndexMessage;



    public ClientSocket(String address, int port){
        this.address = address;
        this.port = port;

        listMessage = new Message();
        statusMessage = new Message();
        resultIndexMessage = new Message();

        listHandler = new Handler(Looper.getMainLooper()){
            @Override
            public void handleMessage(Message msg){
                MainActivity.elements.add(String.valueOf(listMessage.obj));
                MainActivity.arrayAdapter.notifyDataSetChanged();
            }
        };


        statusHandler = new Handler(Looper.getMainLooper()){
            @Override
            public void handleMessage(Message msg){
                MainActivity.txtStatus.setText(String.valueOf(msg.obj));
            }
        };

        resultIndexHandler = new Handler(Looper.getMainLooper()){
            @Override
            public void handleMessage(Message msg){
                String index = msg.obj.toString().split(",")[0];
                String time = msg.obj.toString().split(",")[1];
                MainActivity.txtResultIndex.setText(index);
                MainActivity.txtTime.setText(time);
            }
        };

    }



    public void setDevice(CameraManager cameraManager, String cameraId) {
        this.cameraId = cameraId;
        this.cameraManager = cameraManager;
    }


    @Override
    public void run() {
        super.run();

        try {
            socket = new Socket(address, port);
            Log.d(TAG, "Connection completed successfully.");
            statusMessage = new Message();
            statusMessage.obj = "Connection completed successfully.";
            statusHandler.sendMessage(statusMessage);

            outputStream = socket.getOutputStream();

            OutputStreamWriter outputStreamWriter =
                    new OutputStreamWriter(outputStream, "UTF-8");
            outputStreamWriter.write("generate,666");
            outputStreamWriter.flush();


            bufferedReader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream(), "UTF-8")
            );

            String data = "";
            int counter = 1;

            while (!data.equals("Stop")){

                data = bufferedReader.readLine();
                Log.d(TAG, String.format("Server : %s", data));

                if (data.contains("Index")){
                    Log.d(TAG, data.split(",")[1]);
                    resultIndexMessage = new Message();
                    String[] splittedData = data.split(",");
                    resultIndexMessage.obj = splittedData[1] + "," + splittedData[2];
                    resultIndexHandler.sendMessage(resultIndexMessage);
                    break;
                }


                listMessage = new Message();
                listMessage.obj = String.format("%d) %s",counter++, data);
                listHandler.sendMessage(listMessage);


                /*
                 Print data and control if leftBackward
                 came for the flashlight.
                 */
                if (data.equals("RightLeg")) {
                    try { cameraManager.setTorchMode(cameraId, true);
                    } catch (CameraAccessException e) { e.printStackTrace(); }
                }



                if(data.equals("Stop")) break;

            }

            Log.d(TAG,"Connection closed.");
            statusMessage = new Message();
            statusMessage.obj = "Connection closed.";
            statusHandler.sendMessage(statusMessage);
            close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    private void close() throws IOException{
        socket.close();
        bufferedReader.close();
    }
}
