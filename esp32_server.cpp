#include <WiFi.h>
#include <HTTPClient.h>

// Replace with your network credentials
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// Replace with the IP address and port of your desktop server
const char* serverUrl = "http://192.168.1.100:8080/api/sensor-data";

int counter = 1;

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.println("ESP32 IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"value\": " + String(counter) + "}";
    int responseCode = http.POST(payload);

    Serial.print("Sent value: ");
    Serial.print(counter);
    Serial.print(" | Server response: ");
    Serial.println(responseCode);

    http.end();
  } else {
    Serial.println("WiFi not connected!");
  }

  counter++;
  if (counter > 10) counter = 1;

  delay(5000); // wait 5 seconds
}
