# Automatic and Customized Piano Fingering <h1>
  ## ***Irina Lee*** <h2>
  
  ### Overview <h3>
  >> Piano fingering is a numbering guide written on sheet music meant to help pianists play with greater comfort and fluidity, with the numbers 1-5 representing the thumb through pinky respectively. Although sheet music publishing companies often write in fingering, different pianists with varying hand spans will find that these pre-written fingerings cannot be applied to them. My solution proposes an algorithm that takes in a user's hand span and an image file of sheet music and output another image file with the calculated fingering customized to the user.
  
  ### Requirements <h3>
  >> The coding language used for this project is Python. Import the Python library *re* for the use of regular expressions. Download LilyPond music notation software to read the output. Download *Sibelius* or a similar software to create MIDI files.
  
  ### Installation Instructions <h3>
  >> Download the CURRENTVERSION file and the text files. The text files are test cases converted from MIDI files. To create your own test cases with the same formatting, input the notes of the piece into Sibelius and export a MIDI file. The playback device should be the same as the current device. Next, convert the binary MIDI file into a text file. I used a convertor provided by [Flash Music Games](http://flashmusicgames.com/midi/mid2txt.php). The text file is not affected by whether it was sent as an absolute or delta timestamp type. Sample text files have been provided.
  
  ### Run Instructions <h3>
  >> Run the PianoNumbering file from a Python IDE.
  
  >> #### Sample Output <h4>
  >>>> After inputting the MIDI text file, below is an example of the output. The first is from the generated LilyPond file, the second is the printed output.\
  >>>> ![alt text](https://raw.githubusercontent.com/IrinaLee521/Irina-Lee/master/Resources/MaryHadALamb.PNG)\
  >>>> **Output:** [[128, [69], [3]], [128, [67], [2]], [128, [65], [1]], [128, [67], [2]], [128, [69], [3]], [128, [69], [3]], [256, [69], [3]], [128, [67], [2]], [128, [67], [2]], [256, [67], [2]], [128, [69], [3]], [128, [72], [5]], [256, [72], [5]]]


  
  
