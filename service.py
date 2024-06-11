from ollama import OllamaModelForDisease
import mongodbrepo


ollama_model = OllamaModelForDisease()


def __preprocess_text(text):
    # Replace consecutive spaces, newlines and tabs
    return text.replace("'", "")


def __fetch_disease_details_from_llm(disease_name: str):
    causes, symptoms, remedies, harmful_foods, beneficial_foods = ollama_model.invoke(disease_name)
    causes = __preprocess_text(causes)
    symptoms = __preprocess_text(symptoms)
    remedies = __preprocess_text(remedies)
    harmful_foods = __preprocess_text(harmful_foods)
    beneficial_foods = __preprocess_text(beneficial_foods)

    return causes, symptoms, remedies, harmful_foods, beneficial_foods


def __fetch_disease_details_from_db(disease_name, disease_type):
    for record in mongodbrepo.fetch_from_db(
            {'$and': [{'disease_name': disease_name}, {'disease_type': disease_type}]}):
        return record


def __insert_disease_details_in_db(disease_name, disease_type, causes, symptoms, remedies, harmful_foods, beneficial_foods):
    # disease_id = str(uuid.uuid4())
    record = {
        'disease_name': disease_name,
        'disease_type': disease_type,
        'causes': causes,
        'symptoms': symptoms,
        'remedies': remedies,
        'harmful_foods': harmful_foods,
        'beneficial_foods': beneficial_foods
    }
    mongodbrepo.insert_in_db(record)


def fetch_disease_details(disease_name, disease_type):
    db_result = __fetch_disease_details_from_db(disease_name, disease_type)
    if not db_result:
        causes, symptoms, remedies, harmful_foods, beneficial_foods = __fetch_disease_details_from_llm(disease_name)
        __insert_disease_details_in_db(disease_name, disease_type, causes, symptoms, remedies, harmful_foods,
                                       beneficial_foods)
        return {'disease_name': disease_name, 'disease_type': disease_type, 'causes': causes, 'symptoms': symptoms,
                'remedies': remedies, 'harmful_foods': harmful_foods, 'beneficial_foods': beneficial_foods}
    else:
        db_result.pop('_id')
        return db_result