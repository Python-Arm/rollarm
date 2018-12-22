#include <Servo.h>
//by Francesco Paolo Mariani
Servo base;
Servo spalla;
Servo polso;
Servo mano;

char b[4]={0,0,0,0};
char s[4]={0,0,0,0};
char p[4]={0,0,0,0};
char m[4]={0,0,0,0};
int i=0;
int z;
char vet[12];

void setup(){
  Serial.begin(9600);
  base.attach(4);
  spalla.attach(5);
  polso.attach(6);
  mano.attach(7);
}

void loop(){
    if(Serial.available()){
      z = 0;
      }
    while(z<12){
    if(Serial.available()){
      vet[z++]=Serial.read();
    }
    }
    for(i=0;i<3;i++){
      b[i]=vet[i];
      s[i]=vet[i+3];
      p[i]=vet[i+6];
      m[i]=vet[i+9];
       }
    int ib;
    int is;
    int ip;
    int im;
    ib=atoi(b);
    is=atoi(s);
    ip=atoi(p);
    im=atoi(m);
    if(is>30){
    base.write(ib);
    spalla.write(is);
    polso.write(ip);
    mano.write(im);
    }
    else{
    Serial.write("Errore");
    }}


