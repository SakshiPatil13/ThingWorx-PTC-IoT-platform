#include <sram.h>

/*
 Example of using a Stream object to store the message payload

 Uses SRAM library: https://github.com/ennui2342/arduino-sram
 but could use any Stream based class such as SD

  - connects to an MQTT server
  - publishes "hello world" to the topic "outTopic"
  - subscribes to the topic "inTopic"
*/

#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <SRAM.h>

// Update these with values suitable for your network.
byte mac[]    = { 0xA2, 0xDA, 0xF2, 0x16, 0x2E }; 
IPAddress ip(192, 168, 0, 115); // local "static" ip
IPAddress server(192, 168, 0, 2);  // server (gateway) ip
 
SRAM sram(4, SRAM_1024);

void callback(char* topic, byte* payload, unsigned int length) {
  sram.seek(1);

  // do something with the message
  for(uint8_t i=0; i<length; i++) {
    Serial.write(sram.read());
  }
  Serial.println();

  // Reset position for the next message to be stored
  sram.seek(1);
}

EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient, sram);

void setup()
{
  Ethernet.begin(mac, ip);
  if (client.connect("arduinoClient")) {
    client.publish("outTopic","hello world");
    client.subscribe("inTopic");
  }

  sram.begin();
  sram.seek(1);

  Serial.begin(9600);
}

void loop()
{
  client.loop();
}


