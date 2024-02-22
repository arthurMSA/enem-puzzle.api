from typing import Dict
import json
from bson import json_util

def parseDocumentToJson(document: Dict):
    print(document)
    return json.loads(json_util.dumps(document))