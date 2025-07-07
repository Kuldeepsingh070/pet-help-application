def get_recommendations(disease):
    recommendations = {
        "allergy": {
            "treatment": "Consult a vet for antihistamines and avoid allergens.",
            "diet": "Provide hypoallergenic food and avoid processed treats.",
            "vaccines": "No specific vaccine for allergy. Keep up with routine shots."
        },
        "bleeding": {
            "treatment": "Stop the bleeding, bandage, and seek vet care.",
            "diet": "Feed soft food if bleeding is oral. Maintain hydration.",
            "vaccines": "No direct vaccines. Ensure tetanus shots in injury cases."
        },
        "cold": {
            "treatment": "Provide warmth and monitor. Vet may give antibiotics.",
            "diet": "Warm, soft food and plenty of water.",
            "vaccines": "Routine vaccines like Bordetella help prevent respiratory illness."
        },
        "diarrhea": {
            "treatment": "Hydrate and offer probiotics. Vet may suggest antibiotics.",
            "diet": "Boiled rice and chicken or vet-approved bland food.",
            "vaccines": "Keep parvo and distemper vaccines up-to-date."
        },
        "ear infection": {
            "treatment": "Clean ears and apply prescribed medication.",
            "diet": "Low-allergy diet can help with recurring issues.",
            "vaccines": "No direct vaccine. Keep immune system strong with core vaccines."
        },
        "fever": {
            "treatment": "Monitor temperature, hydrate, and consult a vet.",
            "diet": "Light, easy-to-digest meals and fluids.",
            "vaccines": "Maintain general vaccination schedule to prevent infections."
        },
        "fracture": {
            "treatment": "Immobilize and visit vet for X-ray and possible surgery.",
            "diet": "Calcium and protein-rich diet to promote bone healing.",
            "vaccines": "No specific vaccine, but maintain core vaccines during recovery."
        },
        "infection": {
            "treatment": "Antibiotics from vet. Keep area clean.",
            "diet": "Nutritious diet to boost immunity.",
            "vaccines": "Vaccines like rabies and parvo help prevent common infections."
        },
        "limping": {
            "treatment": "Rest and possibly anti-inflammatory medicine.",
            "diet": "Joint supplements and high-protein food.",
            "vaccines": "No direct vaccine. Maintain general schedule."
        },
        "mange": {
            "treatment": "Medicated shampoo and vet-prescribed treatments.",
            "diet": "Boost immune system with high-quality food.",
            "vaccines": "No vaccine, but regular care prevents complications."
        },
        "normal": {
            "treatment": "No treatment needed. Keep pet healthy.",
            "diet": "Balanced commercial or vet-approved homemade food.",
            "vaccines": "Follow full core vaccination schedule: Rabies, DHPP, etc."
        },
        "parvo": {
            "treatment": "Intensive care with IV fluids and antibiotics.",
            "diet": "Bland diet after recovery. Start slow with soft food.",
            "vaccines": "Parvovirus vaccine is essential. Start at 6–8 weeks of age."
        },
        "rabies": {
            "treatment": "Fatal if symptoms appear. Euthanasia often required.",
            "diet": "N/A – emergency situation.",
            "vaccines": "Rabies vaccine is legally mandatory and life-saving."
        },
        "tick": {
            "treatment": "Remove ticks and apply anti-parasitic medicine.",
            "diet": "Iron-rich food if anemia develops.",
            "vaccines": "Tick-borne disease vaccines like Lyme may be suggested in some areas."
        },
        "tumor": {
            "treatment": "Vet may recommend biopsy or surgery.",
            "diet": "Low-carb, high-protein, vet-prescribed cancer diet.",
            "vaccines": "No specific vaccine for tumors. Maintain core vaccines."
        },
        "vomiting": {
            "treatment": "Hydrate, skip one meal, then feed bland food.",
            "diet": "Boiled chicken/rice or prescription food.",
            "vaccines": "Core vaccines help avoid viral causes like parvo."
        },
        "wound": {
            "treatment": "Clean, bandage, and use antibiotics if needed.",
            "diet": "Protein-rich food to help healing.",
            "vaccines": "Ensure tetanus and rabies shots are up-to-date."
        }
    }

    return recommendations.get(disease, {
        "treatment": "Consult a vet.",
        "diet": "Follow vet-advised nutrition.",
        "vaccines": "Ask your vet for vaccination needs."
    })
