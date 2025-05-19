# AI Prompt Tester

A Python tool for testing and evaluating AI prompts using OpenAI's GPT-4 model. This tool helps you analyze the effectiveness of your prompts by measuring response length, token usage, and assigning scores.

## Features

- Tests prompts against GPT-4
- Calculates token usage and costs
- Assigns scores based on response length
- Exports results to CSV
- Supports batch processing of prompts

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sayheyrey/py-prompt-tester.git
cd py-prompt-tester
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```
Then edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Prepare your prompts in a CSV file with a column named "Prompt". You can use the example format from `AI_Prompts_Testing_Template - AI_Prompt_Testing_Template.csv`.

2. Run the script:
```bash
python test_prompts.py
```

The script will:
- Process the first 10 prompts by default
- Generate responses using GPT-4
- Calculate token usage and costs
- Assign scores based on response length (5.0-10.0 scale)
- Save results to `AI_Prompts_Testing_Template - TESTED.csv`

## Output Format

The script generates a CSV file with the following columns:
- Original prompt
- GPT-4 response
- Token cost
- Score (5.0-10.0, based on response length)

## Customization

You can modify the following parameters in `test_prompts.py`:
- Number of prompts to test (currently set to 10)
- Temperature setting (currently 0.7)
- Scoring formula (currently based on response length)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 