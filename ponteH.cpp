// usando ponte H


// constantes globais do projeto
const int controlPin1 = 2;  // pino de controle do motor 1                   
const int controlPin2 = 3;  // pino de controle do motor 2
const int ligarMotor = 9;  // ligar/desligar o motor
const int mudarDirecao = 4;  // pino para mudar de direção
const int mudarOnOff = 5; // pino para ligar/desligar a direção

// variáveis de estado do projeto
int estadoMotor = 0; // estado do motor
int estadoDirecao = 0; // estado da direção
int estadoDirecaoOnOff = 0; // estado da direção ligada/desligada
int estadoLigarMotor = 0; // estado do motor ligado/desligado

int motorAtivo; // estado do botão ligar/desligar motor
int direcaoMotor = 1; // estado do botão mudar direção

// inicialização do projeto
void setup() {
  // seu código aqui, vai ser executado uma vez:
  pinMode(controlPin1, OUTPUT); // pino de controle do motor 1
  pinMode(controlPin2, OUTPUT); // pino de controle do motor 2

  pinMode(mudarDirecao, INPUT); // pino para mudar de direção
  pinMode(mudarOnOff, INPUT); // pino para ligar/desligar a direção
  pinMode(ligarMotor, OUTPUT); // pino para ligar/desligar o motor

  digitalWrite(ligarMotor, LOW); // desliga o motor
}

void loop() {
  
   // seu código aqui, vai ser executado repetidamente:
  estadoMotor = digitalRead(mudarOnOff);
  delay(1);
  estadoDirecao = digitalRead(mudarDirecao);

  if (estadoMotor != estadoLigarMotor) {
    if (estadoMotor == HIGH) {
      motorAtivo =! motorAtivo;
    }
  }

  if (estadoDirecao != estadoDirecaoOnOff) {
    if (estadoDirecao == HIGH) {
      direcaoMotor =! direcaoMotor;
    }
  }

  if (direcaoMotor == 1) {
    digitalWrite(controlPin1, HIGH);
    digitalWrite(controlPin2, LOW);
  }
  else {
    digitalWrite(controlPin1, LOW);
    digitalWrite(controlPin2, HIGH);
  }

  if (motorAtivo == 1) {
    digitalWrite(ligarMotor,HIGH);
  }
  else {
    digitalWrite(ligarMotor, 0);
  }

  estadoDirecaoOnOff = estadoDirecao;
  estadoLigarMotor = estadoMotor;

}