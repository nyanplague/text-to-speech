import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir


class Converter:
    def __init__(self):
        self.session = Session(profile_name="default")
        self.polly = self.session.client("polly")


    def convert(self, text):
        try:
            response = self.polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                                VoiceId="Joanna")
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)


        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
               file_name = os.path.join("/Users/admin/Desktop/text_to_speech_project/results", "speech.mp3")
               try:
                    with open(file_name, "wb") as file:
                       file.write(stream.read())
               except IOError as error:
                  print(error)
                  sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)

        return file_name




