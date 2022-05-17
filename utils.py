import json

def load_candidates_from_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            matches.append(candidate)
    return matches


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json("candidates.json")
    matches =[]
    for candidate in candidates:
        if skill_name.lower() in candidate["skill"].lower().split(", "):
            matches.append(candidate)
    return matches