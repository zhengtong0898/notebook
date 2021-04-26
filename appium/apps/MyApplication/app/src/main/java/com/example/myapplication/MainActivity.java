package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "button_event ";

    @SuppressLint("ClickableViewAccessibility")
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // 给当前Activity增加 secure flag 之后,
        // UIAutomatorViewer 就无法获取到截屏和组件树信息了.
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE,
                             WindowManager.LayoutParams.FLAG_SECURE);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button tv_one_btn = findViewById(R.id.tv_one_btn);

        // 点击事件: 优先级第三
        tv_one_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.e(TAG, "onClick: ");
            }
        });

        // 长按事件: 优先级第二
        tv_one_btn.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {
                Log.e(TAG, "onLongClick: ");
                return false;
            }
        });

        // 触摸事件: 优先级第一
        tv_one_btn.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                Log.e(TAG, "onTouch: " + event.getAction());
                return false;
            }
        });
    }
}