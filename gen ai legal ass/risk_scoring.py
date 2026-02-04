RISK_KEYWORDS = {
    "penalty": 3,
    "indemnity": 3,
    "terminate": 2,
    "auto-renew": 2,
    "non-compete": 3,
    "intellectual property": 2,
    "arbitration": 2,
}

def score_clause(clause):
    score = 0
    for key, value in RISK_KEYWORDS.items():
        if key.lower() in clause.lower():
            score += value

    if score >= 3:
        return "High"
    elif score == 2:
        return "Medium"
    else:
        return "Low"

def overall_contract_risk(clauses):
    risks = [score_clause(c) for c in clauses]
    if "High" in risks:
        return "High"
    elif "Medium" in risks:
        return "Medium"
    return "Low"
def clause_risk_score(clause):
    clause_lower = clause.lower()

    high_risk_terms = [
        "indemnify", "penalty", "liquidated damages",
        "non-compete", "exclusive", "irrevocable",
        "unilateral", "terminate at any time"
    ]

    medium_risk_terms = [
        "termination", "arbitration",
        "jurisdiction", "governing law",
        "confidentiality", "auto-renewal"
    ]

    if any(term in clause_lower for term in high_risk_terms):
        return "High"
    elif any(term in clause_lower for term in medium_risk_terms):
        return "Medium"
    else:
        return "Low"

