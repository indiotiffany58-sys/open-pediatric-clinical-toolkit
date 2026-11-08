"""
Pediatric Dosing & Anthropometric Calculator
Part of the Open Pediatric & Clinical Simulation Toolkit
"""

def calculate_bsa_mosteller(weight_kg: float, height_cm: float) -> float:
    """Calculates Body Surface Area (BSA) in m^2 using Mosteller formula."""
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive values.")
    return ((weight_kg * height_cm) / 3600) ** 0.5


def holliday_segar_fluids(weight_kg: float) -> dict:
    """Calculates daily and hourly maintenance IV fluids for pediatric patients."""
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")
    
    if weight_kg <= 10:
        daily_ml = weight_kg * 100
    elif weight_kg <= 20:
        daily_ml = 1000 + ((weight_kg - 10) * 50)
    else:
        daily_ml = 1500 + ((weight_kg - 20) * 20)
        
    hourly_ml = round(daily_ml / 24, 2)
    return {"daily_ml": round(daily_ml, 2), "hourly_ml_hr": hourly_ml}


def calculate_medication_dose(weight_kg: float, dose_mg_per_kg: float, frequency_per_day: int) -> dict:
    """Calculates total daily dose and individual dose in mg."""
    total_daily_mg = weight_kg * dose_mg_per_kg
    single_dose_mg = total_daily_mg / frequency_per_day
    return {
        "total_daily_mg": round(total_daily_mg, 2),
        "single_dose_mg": round(single_dose_mg, 2),
        "doses_per_day": frequency_per_day
    }

if __name__ == "__main__":
    # Example clinical test case: 14 kg patient, 95 cm
    print("BSA (m2):", round(calculate_bsa_mosteller(14.0, 95.0), 2))
    print("Maintenance Fluids:", holliday_segar_fluids(14.0))
    print("Amoxicillin High-Dose (90 mg/kg/day BID):", calculate_medication_dose(14.0, 90, 2))
  
