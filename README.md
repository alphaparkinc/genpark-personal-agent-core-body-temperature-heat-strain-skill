# Core Body Temperature & Physiological Strain Index (PSI) Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Physiological Strain Index (PSI) calculation, core temperature rise rate, heat acclimatization status, and active cooling intervention trigger. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_physiological_strain_index`: Compute Moran Physiological Strain Index (PSI 0-10) from core temperature (°C) and heart rate telemetry.
- `prescribe_active_cooling_emergency_triage`: Synthesize rapid cooling countermeasures (cold water immersion, ice vest, palm cooling) based on PSI score.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_core_body_temperature_heat_strain_skill.server --test
```
