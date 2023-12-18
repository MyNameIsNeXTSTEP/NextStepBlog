'''
Prerequisites:
  1. Packages installed: tiktoken, dotenv, openai
  2. Environment: file in the root dir named '.env' with this inside:
    OPENAI_API_KEY=<your_openai_API-KEY_here>

Usage: (bash) python3 gpt-translate.py '<path_to_file>'
*NOTE: If specifying path to file in some directory, do not write / sign in the front of first directory name

Result: The translation saves to `gpt-translation-response.md` file in the root dir
'''

import sys
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI


translationSourceFilename = sys.argv[1]
load_dotenv()


def getFileContent(filename: str):
  with open(filename, 'r') as sourceFile:
    return sourceFile.read()

def tokensOfStrings(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    numTokens = len(encoding.encode(string))
    return numTokens

def askGPT(content: str):
  '''return type - https://platform.openai.com/docs/api-reference/chat/object'''
  prompt = 'Translate this whole text to russian keeping the markdown layout and semantics of document content:\n' + content
  try:
    response = OpenAI().chat.completions.create(
      model="gpt-4",
      messages=[{ 'role': 'user', 'content': prompt }],
    )
    print('Message was sent successfully')
    return list(
      map(lambda choice: choice.message.content, response.choices)
    )
  # @todo: Fix Error type processing (maybe not only the AttributeError) &
  # Alse error might be raised during/after requesting OpenAI
  except AttributeError:
    print('There is no such attribute')

def writeAnswerToFile(lines: str) -> None:
  try:
    with open('gpt-translation-response.md', 'w') as file:
      file.writelines(lines)
  except:
    raise Exception('Error: Something went wrong')

fileContentForTranslation = getFileContent(translationSourceFilename)
print('\nTokens of given strings in the file: %s' % tokensOfStrings(
  fileContentForTranslation, 'cl100k_base')
  )

writeAnswerToFile(
  askGPT(
   fileContentForTranslation 
  )
)