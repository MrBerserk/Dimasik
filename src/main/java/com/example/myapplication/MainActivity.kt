package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import kotlin.math.roundToInt

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun method(view: View) {
        if ((findViewById(R.id.editTextTextPersonName) as EditText).text.isEmpty()
            || (findViewById(R.id.editTextNumber) as EditText).text.isEmpty()
            || (findViewById(R.id.editTextNumberDecimal2) as EditText).text.isEmpty()
            || (findViewById(R.id.editTextNumber3) as EditText).text.isEmpty()
        ) {
            Toast.makeText(this, "All fields must be filled in", Toast.LENGTH_SHORT).show()
        } else {
            val lenOfUserName = (findViewById(R.id.editTextTextPersonName) as EditText).text.length
            val heightOfUser =
                (findViewById(R.id.editTextNumber) as EditText).text.toString().toInt()
            val weightOfUser =
                (findViewById(R.id.editTextNumberDecimal2) as EditText).text.toString().toDouble()
            val ageOfUser =
                (findViewById(R.id.editTextNumber3) as EditText).text.toString().toInt()


            if (heightOfUser == 0) {
                Toast.makeText(this, "Height must be more than 0", Toast.LENGTH_SHORT).show()
            } else if (heightOfUser >= 250) {
                Toast.makeText(this, "Height must be less than 250", Toast.LENGTH_SHORT).show()
            } else if (weightOfUser == 0.0) {
                Toast.makeText(this, "Weight must be more than 0", Toast.LENGTH_SHORT).show()
            } else if (weightOfUser >= 250) {
                Toast.makeText(this, "Weight must be less than 250", Toast.LENGTH_SHORT).show()
            } else if (ageOfUser == 0) {
                Toast.makeText(this, "Age must be more than 0", Toast.LENGTH_SHORT).show()
            } else if (ageOfUser >= 150) {
                Toast.makeText(this, "Age must be less than 150", Toast.LENGTH_SHORT).show()
            } else {
                val tmp = findViewById(R.id.textView) as TextView
                var insideAge =
                    lenOfUserName / 2 + heightOfUser % 11 * 5 + (weightOfUser.roundToInt() - 12) % 10 - ageOfUser % 4 + 10
                tmp.setText("Ваш внутенний возраст $insideAge")
            }
        }
    }
}