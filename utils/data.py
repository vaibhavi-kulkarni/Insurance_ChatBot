# This file contains information about various insurance company policies, including health, life, motor,
# home, and travel insurance. Each insurance type has predefined plan details from various leading insurance providers.

import random

# Function to generate detailed responses for insurance plans
def generate_plan_response(user_input):
    plans = {
        "health insurance": [
            "Health insurance covers a wide range of medical needs, such as hospitalization, surgeries, "
            "pre-existing conditions, diagnostics, and maternity coverage. Popular plans in India include Star Health, "
            "Care Health, and Religare Health.",
            "Star Health offers Family Health Optima with maternity coverage and cashless network options.",
            "Care Health provides Care Comprehensive with options for pre-existing diseases and emergency ambulance services.",
            "Religare Health offers Care Insurance with coverage for day care treatments, critical illness, and health check-ups."
        ],
        "life insurance": [
            "Life insurance provides a lump sum to your beneficiaries in case of your demise. The types of life insurance "
            "plans include term insurance, endowment plans, and ULIPs. Leading providers are LIC, HDFC Life, and ICICI Prudential.",
            "LIC offers Jeevan Akshay, a plan that provides guaranteed income for life to policyholders.",
            "HDFC Life offers Sampoorn Nivesh, a ULIP plan with flexible investment options and life coverage.",
            "ICICI Prudential offers LifeStage Protection Plan, which adapts to your changing life stage needs with cover for life and critical illness."
        ],
        "motor insurance": [
            "Motor insurance covers accidental damage to your vehicle, theft, and third-party liabilities. Some of the most "
            "trusted providers for car and bike insurance in India are ICICI Lombard, Bajaj Allianz, and Reliance General.",
            "ICICI Lombard offers Car Insurance with features like zero depreciation and cashless garage services.",
            "Bajaj Allianz provides Comprehensive Car Insurance, which covers third-party liability, accidental damages, and theft.",
            "Reliance General offers Auto Insurance with various add-ons like roadside assistance and engine protection."
        ],
        "home insurance": [
            "Home insurance covers damages to your house and belongings, such as from fire, natural disasters, and theft. "
            "You can consider New India Assurance, HDFC ERGO, and Bajaj Allianz for home insurance.",
            "HDFC ERGO's Home Insurance Plan covers fire, flood, and theft. It also protects valuable household items.",
            "Bajaj Allianz Home Secure plan includes protection against burglary, fire, earthquake, and damage to contents.",
            "New India Assurance offers Fire & Special Perils Policy, which covers a wide range of risks including fire, lightning, and natural calamities."
        ],
        "travel insurance": [
            "Travel insurance offers coverage for trip cancellations, medical emergencies, lost luggage, and flight delays. "
            "ICICI Lombard, Tata AIG, and Religare provide travel insurance plans for international and domestic trips.",
            "Tata AIG offers travel insurance with coverage for lost baggage, flight delays, and emergency medical evacuation.",
            "Religare Travel Insurance includes global medical coverage, trip cancellation, and travel delays.",
            "ICICI Lombard provides extensive coverage for international and domestic travel, including emergency medical treatment and trip interruption."
        ]
    }

    # Extract the plan type from the user input to provide relevant details
    for plan in plans:
        if plan in user_input.lower():
            # Randomly return one of the plans from the available options
            return random.choice(plans[plan])
    
    return "Sorry, I couldn't find a specific plan related to that. Could you please clarify?"

# Predefined responses for various insurance-related queries
predefined_system_info = [
    {
        "keywords": ["health insurance", "health"],
        "response": (
            "Health insurance typically covers medical expenses, surgeries, and hospital bills. "
            "In India, popular plans include Star Health Insurance, Care Health Insurance, and Religare Health Insurance."
        )
    },
    {
        "keywords": ["life insurance", "life"],
        "response": (
            "Life insurance ensures financial security for your family in case of an unfortunate event. "
            "Popular plans include LIC, HDFC Life, and ICICI Prudential Life."
        )
    },
    {
        "keywords": ["motor insurance", "car insurance", "bike insurance"],
        "response": (
            "Motor insurance covers damages to your vehicle and third-party liabilities. "
            "In India, insurance companies like ICICI Lombard, Bajaj Allianz, and Reliance General Insurance offer good plans."
        )
    },
    {
        "keywords": ["travel insurance", "travel"],
        "response": (
            "Travel insurance covers trip cancellations, lost luggage, and medical emergencies abroad. "
            "ICICI Lombard, Tata AIG, and Religare Travel Insurance are popular choices in India."
        )
    },
    {
        "keywords": ["home insurance", "home"],
        "response": (
            "Home insurance provides protection against damages to your house and belongings due to disasters, fire, or theft. "
            "Popular providers include New India Assurance, HDFC ERGO, and Bajaj Allianz."
        )
    },
    {
        "keywords": ["types of insurance", "insurance types"],
        "response": (
            "**In India, insurance policies mainly fall into two broad types:**\n\n"
            "**1. Life Insurance** (Covers life-related risks)\n"
            "- Term Insurance\n"
            "- Endowment Plans\n"
            "- Unit Linked Insurance Plans (ULIPs)\n"
            "- Money-Back Policies\n"
            "- Whole Life Insurance\n"
            "- Child Insurance Plans\n"
            "- Retirement/Pension Plans\n\n"
            "**2. General Insurance** (Covers non-life risks)\n"
            "- Health Insurance\n"
            "- Motor Insurance (Car, Bike)\n"
            "- Home Insurance\n"
            "- Travel Insurance\n"
            "- Commercial/Business Insurance\n"
            "- Marine Insurance\n"
            "- Crop Insurance"
        )
    },
    {
        "keywords": ["pre-existing conditions", "health insurance", "conditions"],
        "response": (
            "Health insurance in India typically covers hospitalization expenses, surgeries, day care treatments, pre-and post-hospitalization costs, diagnostic tests, and sometimes even maternity expenses. "
            "You should check with your insurer for the specifics of your plan, including network hospitals and exclusions."
        )
    },
    {
        "keywords": ["plan", "health plan", "life insurance plan", "motor plan", "insurance plan"],
        "response": generate_plan_response
    },
    {
        "keywords": ["best insurance providers", "top insurance", "insurance companies"],
        "response": (
            "Some of the top insurance companies in India include LIC, ICICI Prudential, HDFC Life, Bajaj Allianz, "
            "Star Health, and Tata AIG. These companies offer a wide range of plans tailored to various needs."
        )
    },
    {
        "keywords": ["claim process", "file a claim", "claim insurance"],
        "response": (
            "The insurance claim process typically involves the following steps:\n"
            "1. Notify the insurance company about the incident.\n"
            "2. Submit necessary documents like claim forms, police reports (for motor insurance), hospital bills (for health insurance), etc.\n"
            "3. The insurer reviews your claim and may send an investigator.\n"
            "4. Once verified, the insurance company disburses the claim amount.\n"
            "You can check the specifics of the process with your insurance provider."
        )
    }
]
