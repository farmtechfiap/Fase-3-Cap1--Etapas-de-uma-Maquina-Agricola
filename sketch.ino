#include <DHT.h>

#define PINO_DHT 15
#define PINO_LDR 34
#define PINO_RELE 26
#define BOTAO_N 12
#define BOTAO_P 14
#define BOTAO_K 27

DHT dht(PINO_DHT, DHT22);

char clima = 'S';

bool n_ligado = false;
bool p_ligado = false;
bool k_ligado = false;

bool anterior_n = HIGH;
bool anterior_p = HIGH;
bool anterior_k = HIGH;

void setup() {

  Serial.begin(115200);

  dht.begin();

  pinMode(PINO_RELE, OUTPUT);

  pinMode(BOTAO_N, INPUT_PULLUP);
  pinMode(BOTAO_P, INPUT_PULLUP);
  pinMode(BOTAO_K, INPUT_PULLUP);

  digitalWrite(PINO_RELE, LOW);

  // CABEÇALHO CSV
  Serial.println("cultura,umidade,ph,status,motivo");
}

void loop() {

  // =========================
  // RECEBE CLIMA DO PYTHON
  // =========================

  if (Serial.available() > 0) {

    char letra = Serial.read();

    if (letra == 'S') {
      clima = 'S';
    }

    else if (letra == 'C') {
      clima = 'C';
    }
  }

  // =========================
  // LOGICA DOS BOTOES NPK
  // =========================

  bool ler_n = digitalRead(BOTAO_N);

  if (ler_n == LOW && anterior_n == HIGH) {
    n_ligado = !n_ligado;
    delay(100);
  }

  anterior_n = ler_n;

  bool ler_p = digitalRead(BOTAO_P);

  if (ler_p == LOW && anterior_p == HIGH) {
    p_ligado = !p_ligado;
    delay(100);
  }

  anterior_p = ler_p;

  bool ler_k = digitalRead(BOTAO_K);

  if (ler_k == LOW && anterior_k == HIGH) {
    k_ligado = !k_ligado;
    delay(100);
  }

  anterior_k = ler_k;

  // =========================
  // LEITURA DOS SENSORES
  // =========================

  float umidade = dht.readHumidity();

  int luz = analogRead(PINO_LDR);

  float valor_ph = map(luz, 0, 4095, 0, 14);

  // =========================
  // REGRAS DO MILHO
  // =========================

  bool ph_certo = (valor_ph >= 5.5 && valor_ph <= 7.5);

  bool solo_seco = (umidade < 55.0);

  bool tem_adubo = (n_ligado && p_ligado && k_ligado);

  bool tempo_sem_chuva = (clima == 'S');

  // =========================
  // STATUS E MOTIVO
  // =========================

  String status;
  String motivo;

  if (solo_seco && ph_certo && tem_adubo && tempo_sem_chuva) {

    digitalWrite(PINO_RELE, HIGH);

    status = "LIGADA";

    motivo = "OK";
  }

  else {

    digitalWrite(PINO_RELE, LOW);

    status = "DESLIGADA";

    if (clima == 'C') {
      motivo = "Chovendo";
    }

    else if (!tem_adubo) {
      motivo = "Falta adubo";
    }

    else if (!ph_certo) {
      motivo = "pH fora ideal";
    }

    else {
      motivo = "Solo molhado";
    }
  }

  // =========================
  // SAIDA CSV
  // =========================

  Serial.print("MILHO");
  Serial.print(",");

  Serial.print(umidade);
  Serial.print(",");

  Serial.print(valor_ph);
  Serial.print(",");

  Serial.print(status);
  Serial.print(",");

  Serial.println(motivo);

  delay(1500);
}