'''
Prerequisites:
  1. Packages installed: tiktoken, dotenv, openai
  2. Environment: file in the root dir named '.env' with this inside:
    OPENAI_API_KEY=<your_openai_API-KEY_here>

Usage script (bash): `python3 gpt-translate.py <path_to_file>`
*NOTE: If specifying path to file in some directory, do not write / sign in the front of first directory name

Result: The translation saves to `{sourcefileName}-rus.md` file in the same directory as the source file
'''

# Need refactoring on how to read and safe files
# Additionally would be better to create sort of a plug for testing script logic without using GPTs API
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
    print('\nMessage was sent successfully\n')
    outputContentArray = list(
      map(lambda choice: choice.message.content, response.choices)
    )
    return outputContentArray
  # @todo: Fix Error type processing (maybe not only the AttributeError) &
  # Alse error might be raised during/after requesting OpenAI
  except AttributeError:
    print('There is no such attribute')

def insertLinkInTranslationPage(lines, saveName):
  print(saveName)
  lines.insert(0, '---\nhide_from_menu: true\n---\n\n') # to hide translation MD files from menu list (access only by ref)
  link = "\n<span class='translation_button'>[Читать на англ.](/{})</span>\n".format(saveName
    .replace('docs/', '')
    .replace('.md', ''))
  lines[1] = lines[1].split('\n')[0] + link + '\n'.join(lines[1].split('\n')[1:])
  return lines

def insertLinkInEnglishPage(filename, linkFileName):
  link = "\n<span class='translation_button'>[Read in RUS (translated by ChatGPT)](/{})</span>\n".format(linkFileName
    .replace('docs/', '')
    .replace('.md', ''))
  with open(filename, 'r') as sourceFile:
    data = sourceFile.readlines()
  data[0] = data[0] + link
  with open(filename, 'w') as targetFile:
    targetFile.writelines(''.join(data))

def writeAnswerToFile(lines: str) -> None:
  [ pathToSave, fileName ] = translationSourceFilename.rsplit('/', 1) # save in the same dir as the origin file is
  saveName = '{}/{}-rus.md'.format(pathToSave, fileName.rsplit('.')[0])
  linesWithTranslationInfo = insertLinkInTranslationPage(lines, '{}/{}'.format(pathToSave, fileName))
  insertLinkInEnglishPage(translationSourceFilename, saveName)
  try:
    with open(saveName, 'w') as file:
      file.writelines(linesWithTranslationInfo)
  except:
    raise Exception('Error: Something went wrong')


# Final execution
fileContentForTranslation = getFileContent(translationSourceFilename)
print('\nTokens of given strings in the file: {}' .format(tokensOfStrings(fileContentForTranslation, 'cl100k_base')))

writeAnswerToFile(
  askGPT(
   fileContentForTranslation 
  )
)