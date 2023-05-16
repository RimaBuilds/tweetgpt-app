
# Titter GPT 🐦 

Generate creative tweets and threads with ChatGPT, powered by OpenAI's GPT-3 model.

![Titter GPT Screenshot](screenshot.png)

This project is adapted from [emailGPT](https://github.com/lucasmccabe/emailGPT) by [Lucas McCabe](https://github.com/lucasmccabe) and utilizes the reverse ChatGPT method from [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) using the [revChatGPT](https://pypi.org/project/revChatGPT/) package and [streamlit app](https://streamlit.io/). The original emailGPT project is licensed under the [MIT License](https://github.com/lucasmccabe/emailGPT/blob/main/LICENSE).

## Features

- Generate tweet options based on a given topic, tone, and style.
- Customize the tone and style for each tweet.
- choose between single tweet or twitter thread.
- Easy-to-use interface built with Streamlit.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/rimabuilds/tweetGPT-app.git
   cd tweetGPT-app
   ```

2. Create and activate a virtual environment (optional, but recommended):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Open your browser and visit `http://localhost:8501` to use the app.

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)
