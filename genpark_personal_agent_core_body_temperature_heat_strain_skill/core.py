# -*- coding: utf-8 -*-
"""Core Body Temperature & Heat Strain Analyzer for GenPark Personal Agent."""
import json
from typing import Dict, Any

class CoreBodyTemperatureHeatStrainAnalyzer:
    @staticmethod
    def calculate_physiological_strain_index(core_temp_c_current: float, hr_current_bpm: float, core_temp_c_rest: float = 37.0, hr_rest_bpm: float = 65.0) -> Dict[str, Any]:
        # Moran PSI formula: 5 * (T_curr - T_rest) / (39.5 - T_rest) + 5 * (HR_curr - HR_rest) / (180.0 - HR_rest)
        temp_comp = 5.0 * (max(0.0, core_temp_c_current - core_temp_c_rest) / max(0.5, 39.5 - core_temp_c_rest))
        hr_comp = 5.0 * (max(0.0, hr_current_bpm - hr_rest_bpm) / max(20.0, 180.0 - hr_rest_bpm))
        psi = round(min(10.0, max(0.0, temp_comp + hr_comp)), 1)
        
        if psi >= 8.0 or core_temp_c_current >= 39.5:
            risk = "CRITICAL_HEAT_EXHAUSTION_STROKE_RISK"
        elif psi >= 6.0 or core_temp_c_current >= 38.5:
            risk = "HIGH_HEAT_STRAIN_PERFORMANCE_LIMIT"
        elif psi >= 3.0:
            risk = "MODERATE_HEAT_EXPOSURE"
        else:
            risk = "LOW_HEAT_STRAIN_SAFE"
            
        return {
            "core_temperature_c": core_temp_c_current,
            "heart_rate_bpm": hr_current_bpm,
            "psi_score": psi,
            "heat_strain_category": risk,
            "requires_cooling_countermeasure": psi >= 6.0
        }

    @staticmethod
    def prescribe_active_cooling_emergency_triage(psi_score: float, core_temp_c: float) -> Dict[str, Any]:
        if core_temp_c >= 39.5 or psi_score >= 8.0:
            triage = [
                "IMMEDIATE COLD WATER IMMERSION (10-15°C water) up to chest with continuous agitation",
                "Apply ice packs to axillae, groin, and neck vasculature",
                "Cease all exertion; dial emergency medical response"
            ]
        elif core_temp_c >= 38.5:
            triage = [
                "Palmar cooling (submerge hands in 15°C water to leverage arteriovenous anastomoses)",
                "Cold towel evaporative fanning in shade",
                "Ingest 500ml ice slurry beverage to extract internal caloric heat"
            ]
        else:
            triage = ["Standard passive rest in shaded ventilated area", "Sip ambient electrolyte hydration"]
        return {"psi_score": psi_score, "core_temp_c": core_temp_c, "emergency_cooling_triage": triage}
