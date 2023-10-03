import os
from typing import Union, List
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, AnalyzeSentimentResult, DocumentError
load_dotenv()


def authenticate_client() -> TextAnalyticsClient:
    key = os.environ.get('AZURE_LANGUAGE_KEY')
    endpoint = os.environ.get('AZURE_LANGUAGE_ENDPOINT')
    credential = AzureKeyCredential(key)
    return TextAnalyticsClient(
            endpoint=endpoint, 
            credential=credential)


def analyze_sentiment(input: str) -> List[Union[AnalyzeSentimentResult, DocumentError]]:
    client = authenticate_client()
    return client.analyze_sentiment(input, show_opinion_mining=True)