#include <SPI.h>
#include <Ethernet.h>
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; // Dirección MAC de la Shield
IPAddress ip(192, 168, 0, 99); // Dirección IP que deseas asignar
EthernetServer server(80); // Puerto en el que escuchará el servidor (usualmente 80)


void setup() {
Ethernet.begin(mac, ip);
server.begin();

}

void loop() {
EthernetClient client = server.available();

if (client) {
  // Lee la solicitud del cliente y envía la respuesta
  // Puedes manejar diferentes rutas y responder según la solicitud
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println();
  client.println("<html><body><h1>Hola desde Arduino!</h1></body></html>");
  client.stop();
}

}
