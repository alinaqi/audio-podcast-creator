# Podcast Generator

This Python script generates an AI-powered podcast by creating a conversation between two speakers and converting it to speech. It uses OpenAI's GPT-4 for conversation generation and their Text-to-Speech API for audio synthesis.

## Features

- Generates engaging conversations based on input text
- Converts the conversation to speech using different voices for each speaker
- Combines individual audio files into a single podcast episode
- Cleans up temporary files after generation

## Requirements

- Python 3.7+
- OpenAI API key
- Required Python packages:
  - openai
  - pydub

## Setup

1. Clone this repository or download the script.

2. Install the required packages:
   ```
   pip install openai pydub
   ```

3. Set up your OpenAI API key:
   - Sign up for an OpenAI account and obtain an API key
   - Replace `<your api key>` in the script with your actual API key:
     ```python
     openai.api_key = "your-actual-api-key-here"
     ```

4. Ensure you have ffmpeg installed on your system (required by pydub for audio processing).

## Usage

1. Run the script:
   ```
   python podcast_generator.py
   ```

2. When prompted, enter the text you want to base your podcast conversation on.

3. The script will generate the conversation, convert it to speech, and combine the audio files.

4. Once complete, you'll find the generated podcast as `podcast.mp3` in the same directory as the script.

## Customization

- You can modify the `system_prompt` to change the style or context of the generated conversation.
- Adjust the `speaker_voice_map` to use different OpenAI voices for the speakers.
- The script currently uses "Ali" and "Lisa" as speakers. You can change these names in the system prompt and the speaker_voice_map.

## Notes

- The script creates temporary audio files in an `audio-files` directory. These are cleaned up after the podcast is generated.
- The quality and coherence of the generated conversation depend on the input text and the AI model's capabilities.

## License

License is do-whatever-you-like :)

## Contributing

[Include guidelines for contributing to the project, if applicable]

## Support

If you encounter any issues or have questions, please write me :)