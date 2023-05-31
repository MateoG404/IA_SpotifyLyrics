# Clase creada para extraer datos de las canciones 

class Song:
    '''
    Audio Feautures Description

    Danceability =  Danceability describes how suitable a track is for dancing based on a combination of
                    musical elements including tempo, rhythm stability, beat strength, and overall regularity.
                    A value of 0.0 is least danceable and 1.0 is most danceable.
    
    Energy =        Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and 
                    activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal 
                    has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing 
                    to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
    
    Loudness =      The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire 
                    track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound 
                    that is the primary psychological correlate of physical strength (amplitude). Values typically 
                    range between -60 and 0 db.   

    Valance =       A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high 
                    valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound 
                    more negative (e.g. sad, depressed, angry).                
    
    Get from : https://developer.spotify.com/documentation/web-api/reference/get-audio-features                    
    
    '''

    def __init__(self,id):
        self.id = id
        self.name
        self.danceability
        self.energy
        self.loudness
        self.valance 


    #def get_audio_features():   
