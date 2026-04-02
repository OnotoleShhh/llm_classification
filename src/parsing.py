import json
import re
import pandas as pd

def parsing(llm_answer, expected_rows_ids):
   """
   Function protects from:
      - markdown fences
      - bad JSON shape
      - header rows
      - empty rows
      - string "row_id" instead of integer row ID
      - random extra rows
      - missing predictions
   """
   # clear markdown fences
   cleaned_text = llm_answer.strip()
   cleaned_text = re.sub(r"^```json\s*", "", cleaned_text)
   cleaned_text = re.sub(r"^```\s*", "", cleaned_text)
   cleaned_text = re.sub(r"\s*```$", "", cleaned_text)

   # parse json
   json_answ = json.loads(cleaned_text)

   # validate rows
   valid_rows = []
   
   for row in json_answ:
      # check if row contains valid dictionary
      if not isinstance(row, dict):
         continue

      # must contain required keys
      if "row_id" not in row or "label" not in row:
         continue

      row_id = row['row_id']
      label = row['label']

      # row_id must be an integer
      if not isinstance(row_id, int):
         continue

      # label is non-empty string
      if not isinstance(label, str) or label.strip() == "":
         continue

      # indexes in batch belongs to the passed data
      if row_id not in expected_rows_ids:
         continue

      valid_rows.append({
         "row_id": row_id,
         "label": label.strip()
      })

      # detect missing rows
      df_validated = pd.DataFrame(valid_rows)
      returned_ids = set(df_validated['row_id']) if not df_validated.empty else set()
      missing_ids = set(expected_rows_ids) - returned_ids

   return valid_rows, missing_ids