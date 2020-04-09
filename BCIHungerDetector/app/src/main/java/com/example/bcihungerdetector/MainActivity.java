package com.example.bcihungerdetector;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.pm.PackageManager;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraManager;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;


public class MainActivity extends AppCompatActivity {


    public static TextView txtStatus, txtResultIndex, txtTime;
    private EditText etIp, etPort;
    private Button btnConnect, btnFlashlight;
    private CameraManager cameraManager;
    private String cameraId;
    private ClientSocket clientSocket;
    public static ListView lstViewResponses;
    public static ArrayAdapter<String> arrayAdapter;
    public static List<String> elements;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initialize();


    }

    /*
    * check if flash enable on the phone
    * */
    private boolean isFlashEnabled(){
        return getApplicationContext()
                .getPackageManager()
                .hasSystemFeature(PackageManager.FEATURE_CAMERA_FRONT);
    }

    private void initialize(){

        if(!isFlashEnabled());

        cameraManager = (CameraManager) getSystemService(Context.CAMERA_SERVICE);
        try{
            cameraId = cameraManager.getCameraIdList()[0];
        }catch (CameraAccessException e){
            e.printStackTrace();
        }


        txtStatus = findViewById(R.id.txtConnectionStatus);
        txtTime = findViewById(R.id.txtTime);
        etIp = findViewById(R.id.etIp);
        etPort = findViewById(R.id.etPort);
        btnConnect = findViewById(R.id.btnConnect);
        btnFlashlight = findViewById(R.id.btnFlashlight);
        lstViewResponses = findViewById(R.id.lstViewResponses);
        txtResultIndex = findViewById(R.id.txtResultIndex);
        elements = new ArrayList<>();


        arrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, elements);
        lstViewResponses.setAdapter(arrayAdapter);


        etIp.setText("192.168.1.35");
        etPort.setText("9999");


        /*
        implement socket connection configuration
        on button click listener
         */
        btnConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String ipAddress = etIp.getText().toString();
                int port = Integer.parseInt(etPort.getText().toString());

                clientSocket = new ClientSocket(ipAddress, port);
                clientSocket.setDevice(cameraManager, cameraId);
                clientSocket.start();
            }
        });


        btnFlashlight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    cameraManager.setTorchMode(cameraId, false);
                } catch (CameraAccessException e) {
                    e.printStackTrace();
                }

            }
        });



    }


}
