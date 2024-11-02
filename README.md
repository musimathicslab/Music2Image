# Music2Image
Music2Image è un applicazione che è stata sviluppata da A. Salzano "Musica Algoritmica e Sound Computing" durante l'anno accademico 2023/2024.

## Descrizione

Questo progetto utilizza tecnologie di intelligenza artificiale per generare immagini a partire da testo sintetizzato. Combinando modelli di riconoscimento vocale e di generazione di immagini, mira a creare esperienze visive uniche in tempo reale, in particolare per applicazioni musicali.

## Funzionamento

1. **Input Audio**: Il progetto inizia con un input audio, che può essere una traccia musicale o una performance vocale dal vivo.

2. **Trascrizione del testo**: Utilizzando un modello di trascrizione, l'audio presente nel brano musicale viene estratto.

3. **Sintesi del Testo**: Utilizzando un modello di sintesi, il testo trascritto viene sintetizzato, questo passaggio è fondamentale per estrarre le parole e i concetti chiave che per la generazione delle immagini.

4. **Generazione delle Immagini**:
   - Il testo sintetizzato viene passato a **Stable Diffusion**, un modello di intelligenza artificiale per la generazione di immagini. Questo modello è progettato per interpretare il testo e generare immagini coerenti con i contenuti descritti.
   - Le immagini vengono create in tempo reale e possono essere proiettate su uno schermo LED o visualizzate in altre modalità interattive.
  
## Istruzioni per l'Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/musimathicslab/Music2Image
2. Naviga nella cartella del progetto:
   ```bash   
   cd Music2Image\Music2ImageGenerator
3. Installa le dipendenze:
    ```bash   
   pip install -r requirements.txt
4. Esegui il codice
   
**Nota**: Alcune librerie, come quelle per la scheda video, potrebbero richiedere versioni specifiche. Assicurati di controllare la compatibilità con il tuo hardware.



## Configurazione
**Nel codice, potresti trovare le seguenti righe commentate che potrebbero essere necessarie:**
``` python
   #Specificare il percorso completo di ffmpeg se pydub non riesce a trovarlo
   #AudioSegment.converter = ""
   #AudioSegment.ffprobe = ""
   ```

   Inoltre, assicurati di specificare il percorso dell'audio desiderato:
   ``` python
   # Specificare il path dell'audio
   audio_path = "..."
   ```

## Esempi di Immagini Generate

Di seguito sono riportati alcuni esempi di immagini generate utilizzando il testo del brano "Yellow Submarine" dei Beatles.

![Immagine 1](https://i.imgur.com/COoMSwT.png)


## Documentazione
Per ulteriori dettagli sul funzionamento si rimanda alla cartella "documentation".
