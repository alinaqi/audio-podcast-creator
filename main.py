import os
import json
import openai
from pydub import AudioSegment

# Set your OpenAI API key
openai.api_key = "<your api key>"



# System prompt for conversation generation
system_prompt = """You are an experienced podcast host for 'CX Overview' podcast. 
Create an engaging conversation between two people, Ali and Lisa, based on the given text. 
Make the conversation at least 3000 characters long with a lot of emotion.
Use short sentences that can be easily used with speech synthesis.
Include excitement during the conversation.
Avoid mentioning last names.
Include filler words like 'um' or repeat words to make the conversation more natural.
Sascha is writing the articles and Marina is asking insightful questions.
Format the response as a JSON array of objects, each with 'speaker' and 'text' keys."""

# Map speakers to specific voices
speaker_voice_map = {
    "Ali": "onyx",
    "Lisa": "nova"
}

def generate_conversation(input_text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text}
        ]
    )
    return json.loads(response.choices[0].message.content)

def synthesize_speech(text, speaker, index):
    response = openai.audio.speech.create(
        model="tts-1",
        voice=speaker_voice_map[speaker],
        input=text
    )
    
    filename = f"audio-files/{index:03d}_{speaker}.mp3"
    with open(filename, "wb") as out:
        out.write(response.content)
    print(f'Audio content written to file "{filename}"')
    return filename

def generate_podcast(input_text):
    # Create a conversation from the input text
    conversation = generate_conversation(input_text)
    
    # Ensure the audio-files directory exists
    os.makedirs('audio-files', exist_ok=True)
    
    # Generate audio for each part of the conversation
    audio_files = []
    for index, part in enumerate(conversation):
        speaker = part['speaker']
        text = part['text']
        audio_file = synthesize_speech(text, speaker, index)
        audio_files.append(audio_file)
    
    # Combine the audio files
    combined = AudioSegment.empty()
    for audio_file in audio_files:
        segment = AudioSegment.from_mp3(audio_file)
        combined += segment
    
    # Export the final podcast
    combined.export("podcast.mp3", format="mp3")
    
    # Clean up temporary files
    for file in audio_files:
        os.remove(file)
    
    print("Podcast generated successfully as 'podcast.mp3'")

def main():
    print("Welcome to the Podcast Generator!")
    input_text = input("Please enter the text for your podcast: ")
    
    generate_podcast(input_text)
    
    print("You can now play back the generated podcast.mp3 file.")

if __name__ == "__main__":
    main()