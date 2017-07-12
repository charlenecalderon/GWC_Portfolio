#include "pitches.h"

int melody[] = {

 NOTE_G4, NOTE_G5, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_E4, NOTE_D4, NOTE_B4, 0, NOTE_G4, NOTE_G4, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_E4, NOTE_D4, NOTE_B4, 0,  NOTE_G4, NOTE_G4, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_E4, NOTE_D4, NOTE_B4, 0


};

int noteDurations[] = {
  4, 4, 4, 4, 4, 4, 2 , 2, 2, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 8 ,
};

void setup() {

  for (int thisNote = 0; thisNote < 30; thisNote++) {
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(8, melody[thisNote], noteDuration);

    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);

  }
};


void loop() {
  // no need to repeat the melody.
};
