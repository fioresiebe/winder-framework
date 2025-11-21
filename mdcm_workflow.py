"""
Multi-Dimensional Contextual Matrix (MDCM) Workflow
A rigorous framework for holistic data interpretation with economic context
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Any
from enum import Enum
from datetime import datetime
import json


# ============================================================================
# ENUMERATIONS AND TYPE DEFINITIONS
# ============================================================================

class ConfidenceLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class GrowthRegime(Enum):
    HIGH_GROWTH = "high_growth"
    MODERATE_GROWTH = "moderate_growth"
    STAGNATION = "stagnation"
    RECESSION = "recession"


class InflationRegime(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    DEFLATION = "deflation"


class InterestRateRegime(Enum):
    ACCOMMODATIVE = "accommodative"
    NEUTRAL = "neutral"
    RESTRICTIVE = "restrictive"


class CreditConditions(Enum):
    LOOSE = "loose"
    NORMAL = "normal"
    TIGHT = "tight"


class InvestorSentiment(Enum):
    RISK_ON = "risk_on"
    NEUTRAL = "neutral"
    RISK_OFF = "risk_off"


class SensitivityLevel(Enum):
    HIGH = "high"  # 0.7-1.0 correlation
    MODERATE = "moderate"  # 0.3-0.7 correlation
    LOW = "low"  # 0-0.3 correlation
    COUNTER_CYCLICAL = "counter_cyclical"  # negative correlation


# ============================================================================
# DATA CLASSES FOR CONTEXT LAYERS
# ============================================================================

@dataclass
class TemporalContext:
    """Layer 1: Temporal Context Analysis"""
    measurement_period: str
    seasonality_comparison: Dict[str, float]  # year: value
    trend_trajectory: str  # "ascending", "descending", "stable"
    recent_events: List[Dict[str, str]]  # [{"date": "", "event": "", "impact": ""}]
    lifecycle_stage: str  # "introduction", "growth", "maturity", "decline"
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class CompetitiveContext:
    """Layer 2: Competitive Landscape Context"""
    market_share_data: Dict[str, float]  # competitor: share
    competitor_actions: List[Dict[str, str]]  # [{"date": "", "competitor": "", "action": ""}]
    industry_benchmarks: Dict[str, float]  # metric_name: benchmark_value
    market_dynamics: str  # "zero_sum", "market_expansion", "consolidation"
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class CustomerSegmentContext:
    """Layer 3: Customer Segment Stratification"""
    segment_breakdown: Dict[str, float]  # segment_name: metric_value
    cohort_analysis: Dict[str, Dict[str, float]]  # cohort: {metric: value}
    high_value_performance: Dict[str, Any]
    segment_variance_analysis: str
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class OrganizationalContext:
    """Layer 4: Organizational Context"""
    resource_allocation: Dict[str, Any]  # budget, headcount, tools
    strategic_priority_level: str  # "high", "medium", "low"
    team_composition: Dict[str, Any]
    process_maturity: str
    organizational_changes: List[str]
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class MacroeconomicIndicators:
    """5A: Macroeconomic Indicators"""
    federal_funds_rate: float
    interest_rate_trajectory: str
    cost_of_capital: float
    gdp_growth_rate: float
    unemployment_rate: float
    consumer_confidence_index: float
    business_investment_trends: str
    currency_dynamics: Optional[Dict[str, float]] = None
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class SectorEconomics:
    """5B: Sector-Specific Economic Dynamics"""
    sector_growth_rate: float
    vc_funding_trends: str
    industry_margin_trends: str
    customer_industry_health: Dict[str, Any]
    customer_financial_stress_indicators: List[str]
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class MarketStructureEconomics:
    """5C: Market Structure Economics"""
    input_cost_dynamics: Dict[str, float]  # input: cost_change_pct
    supply_chain_pressures: str
    capacity_utilization: float
    price_elasticity: float
    income_elasticity: float
    substitution_effects: str
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class FiscalRegulatoryEconomics:
    """5D: Fiscal & Regulatory Economics"""
    fiscal_policy_stance: str  # "stimulus", "neutral", "austerity"
    tax_policy_changes: List[str]
    subsidy_programs: List[str]
    compliance_cost_burden: float
    regulatory_uncertainty: str
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class LaborEconomics:
    """5E: Labor Economics"""
    wage_inflation_key_roles: float
    talent_availability: str
    turnover_rate: float
    productivity_trends: str
    wage_competitiveness: str
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class InflationPurchasingPower:
    """5F: Inflation & Purchasing Power"""
    headline_inflation: float
    core_inflation: float
    sector_specific_inflation: float
    real_vs_nominal_growth: Dict[str, float]
    wage_price_dynamics: str
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class FinancialMarkets:
    """5G: Financial Market Conditions"""
    equity_market_valuations: Dict[str, float]  # metric: value
    credit_spreads: float
    ipo_exit_environment: str
    investor_sentiment: InvestorSentiment
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class MacroEnvironmentalContext:
    """Layer 5: Comprehensive Macro-Environmental Context"""
    macroeconomic_indicators: MacroeconomicIndicators
    sector_economics: SectorEconomics
    market_structure: MarketStructureEconomics
    fiscal_regulatory: FiscalRegulatoryEconomics
    labor_economics: LaborEconomics
    inflation_purchasing_power: InflationPurchasingPower
    financial_markets: FinancialMarkets
    
    # Economic regime classification
    growth_regime: GrowthRegime
    inflation_regime: InflationRegime
    interest_rate_regime: InterestRateRegime
    credit_conditions: CreditConditions
    investor_sentiment: InvestorSentiment
    
    # Technology and social context
    technological_shifts: List[str] = field(default_factory=list)
    social_cultural_movements: List[str] = field(default_factory=list)
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class MeasurementIntegrityContext:
    """Layer 6: Measurement Integrity Context"""
    data_collection_methodology: str
    definition_consistency: bool
    sample_size: int
    statistical_significance: bool
    instrumentation_bias: List[str]
    methodology_changes: List[str]
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


@dataclass
class StrategicAlignmentContext:
    """Layer 7: Strategic Alignment Context"""
    goal_hierarchy: Dict[str, str]  # metric: strategic_goal
    trade_offs: List[str]
    stakeholder_expectations: Dict[str, float]  # stakeholder: expected_value
    opportunity_costs: List[str]
    
    interrogation_responses: Dict[str, str] = field(default_factory=dict)
    
    def add_interrogation(self, question: str, response: str):
        self.interrogation_responses[question] = response


# ============================================================================
# ECONOMIC ANALYSIS COMPONENTS
# ============================================================================

@dataclass
class EconomicSensitivity:
    """Economic sensitivity mapping for a specific metric"""
    factor: str
    sensitivity_level: SensitivityLevel
    correlation_coefficient: float
    explanation: str


@dataclass
class EconomicScenario:
    """Economic scenario modeling"""
    scenario_name: str  # "base", "upside", "downside"
    probability: float
    gdp_growth: float
    interest_rate_forecast: float
    key_assumptions: List[str]
    metric_forecast: float
    forecast_explanation: str


@dataclass
class EconomicRiskFactor:
    """Economic risk identification"""
    risk_description: str
    probability: float
    impact_severity: str  # "high", "medium", "low"
    leading_indicators: List[str]
    mitigation_strategies: List[str]


@dataclass
class EconomicContextAnalysis:
    """Complete economic context analysis"""
    regime_classification: Dict[str, str]
    key_indicators: Dict[str, Any]
    sensitivity_analysis: List[EconomicSensitivity]
    scenarios: List[EconomicScenario]
    risk_factors: List[EconomicRiskFactor]
    opportunity_factors: List[str]
    leading_indicator_dashboard: Dict[str, float]


# ============================================================================
# CONTEXT INTEGRATION
# ============================================================================

@dataclass
class ContextPattern:
    """Identified patterns in context analysis"""
    pattern_type: str  # "confluence", "contradiction"
    involved_layers: List[str]
    description: str
    causal_relationships: List[str]


@dataclass
class WeightedInterpretation:
    """Weighted interpretation based on context"""
    primary_interpretation: str
    alternative_interpretations: List[Tuple[str, float]]  # (interpretation, probability)
    confidence_level: ConfidenceLevel
    confidence_rationale: str
    layer_weights: Dict[str, float]  # layer_name: relevance_weight


@dataclass
class ActionabilityAssessment:
    """Actionability assessment output"""
    enabled_decisions: List[str]
    recommended_actions: List[str]
    additional_data_needed: List[str]
    monitoring_cadence: str
    success_metrics: List[str]


# ============================================================================
# CONTEXTUALIZED METRIC BRIEF
# ============================================================================

@dataclass
class ContextualizedMetricBrief:
    """Complete deliverable from MDCM analysis"""
    
    # Metadata
    metric_name: str
    analysis_date: datetime
    analyst: str
    
    # Stage 1: Metric Isolation
    raw_metric_value: float
    time_period: str
    scope: str
    initial_observation: str
    
    # Stage 2: Context Layers
    temporal_context: TemporalContext
    competitive_context: CompetitiveContext
    customer_segment_context: CustomerSegmentContext
    organizational_context: OrganizationalContext
    macro_environmental_context: MacroEnvironmentalContext
    measurement_integrity_context: MeasurementIntegrityContext
    strategic_alignment_context: StrategicAlignmentContext
    
    # Stage 3: Context Integration
    identified_patterns: List[ContextPattern]
    
    # Stage 4: Weighted Interpretation
    weighted_interpretation: WeightedInterpretation
    
    # Stage 5: Actionability
    actionability_assessment: ActionabilityAssessment
    
    # Economic Analysis
    economic_context_analysis: EconomicContextAnalysis
    
    # Executive Summary
    executive_summary: str = ""
    
    def generate_executive_summary(self):
        """Generate one-paragraph synthesis"""
        self.executive_summary = f"""
        {self.metric_name} measured at {self.raw_metric_value} for {self.time_period}. 
        Primary interpretation: {self.weighted_interpretation.primary_interpretation}
        Economic regime: {self.macro_environmental_context.growth_regime.value}, with 
        {self.weighted_interpretation.confidence_level.value} confidence.
        Key action: {self.actionability_assessment.recommended_actions[0] if self.actionability_assessment.recommended_actions else 'Further analysis required'}.
        """
        return self.executive_summary
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for export"""
        
        # Helper function to convert objects to JSON-serializable format
        def serialize_value(obj):
            if isinstance(obj, Enum):
                return obj.value
            elif isinstance(obj, datetime):
                return obj.isoformat()
            elif hasattr(obj, '__dict__'):
                return {k: serialize_value(v) for k, v in obj.__dict__.items()}
            elif isinstance(obj, dict):
                return {k: serialize_value(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [serialize_value(item) for item in obj]
            elif isinstance(obj, tuple):
                return tuple(serialize_value(item) for item in obj)
            else:
                return obj
        
        return {
            "metadata": {
                "metric_name": self.metric_name,
                "analysis_date": self.analysis_date.isoformat(),
                "analyst": self.analyst
            },
            "raw_metric": {
                "value": self.raw_metric_value,
                "period": self.time_period,
                "scope": self.scope,
                "initial_observation": self.initial_observation
            },
            "executive_summary": self.executive_summary,
            "contexts": {
                "temporal": serialize_value(self.temporal_context.__dict__),
                "competitive": serialize_value(self.competitive_context.__dict__),
                "customer_segment": serialize_value(self.customer_segment_context.__dict__),
                "organizational": serialize_value(self.organizational_context.__dict__),
                "macro_environmental": {
                    "macroeconomic": serialize_value(self.macro_environmental_context.macroeconomic_indicators.__dict__),
                    "sector": serialize_value(self.macro_environmental_context.sector_economics.__dict__),
                    "market_structure": serialize_value(self.macro_environmental_context.market_structure.__dict__),
                    "fiscal_regulatory": serialize_value(self.macro_environmental_context.fiscal_regulatory.__dict__),
                    "labor": serialize_value(self.macro_environmental_context.labor_economics.__dict__),
                    "inflation": serialize_value(self.macro_environmental_context.inflation_purchasing_power.__dict__),
                    "financial_markets": serialize_value(self.macro_environmental_context.financial_markets.__dict__),
                    "regimes": {
                        "growth": self.macro_environmental_context.growth_regime.value,
                        "inflation": self.macro_environmental_context.inflation_regime.value,
                        "interest_rate": self.macro_environmental_context.interest_rate_regime.value,
                        "credit": self.macro_environmental_context.credit_conditions.value,
                        "investor_sentiment": self.macro_environmental_context.investor_sentiment.value
                    },
                    "technological_shifts": self.macro_environmental_context.technological_shifts,
                    "social_cultural_movements": self.macro_environmental_context.social_cultural_movements
                },
                "measurement_integrity": serialize_value(self.measurement_integrity_context.__dict__),
                "strategic_alignment": serialize_value(self.strategic_alignment_context.__dict__)
            },
            "patterns": [serialize_value(p.__dict__) for p in self.identified_patterns],
            "interpretation": {
                "primary": self.weighted_interpretation.primary_interpretation,
                "alternatives": self.weighted_interpretation.alternative_interpretations,
                "confidence": self.weighted_interpretation.confidence_level.value,
                "rationale": self.weighted_interpretation.confidence_rationale,
                "layer_weights": self.weighted_interpretation.layer_weights
            },
            "economic_analysis": {
                "regime": self.economic_context_analysis.regime_classification,
                "sensitivities": [serialize_value(s.__dict__) for s in self.economic_context_analysis.sensitivity_analysis],
                "scenarios": [serialize_value(s.__dict__) for s in self.economic_context_analysis.scenarios],
                "risks": [serialize_value(r.__dict__) for r in self.economic_context_analysis.risk_factors],
                "opportunities": self.economic_context_analysis.opportunity_factors,
                "leading_indicators": self.economic_context_analysis.leading_indicator_dashboard
            },
            "actionability": {
                "decisions": self.actionability_assessment.enabled_decisions,
                "actions": self.actionability_assessment.recommended_actions,
                "data_needs": self.actionability_assessment.additional_data_needed,
                "monitoring": self.actionability_assessment.monitoring_cadence,
                "success_metrics": self.actionability_assessment.success_metrics
            }
        }
    
    def export_to_json(self, filepath: str):
        """Export brief to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    def generate_report(self) -> str:
        """Generate formatted text report"""
        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║           CONTEXTUALIZED METRIC BRIEF (CMB)                               ║
║           Multi-Dimensional Contextual Matrix Analysis                    ║
╚═══════════════════════════════════════════════════════════════════════════╝

METADATA
--------
Metric: {self.metric_name}
Analysis Date: {self.analysis_date.strftime('%Y-%m-%d')}
Analyst: {self.analyst}

EXECUTIVE SUMMARY
-----------------
{self.executive_summary}

RAW METRIC PERFORMANCE
----------------------
Value: {self.raw_metric_value}
Period: {self.time_period}
Scope: {self.scope}
Initial Observation: {self.initial_observation}

═══════════════════════════════════════════════════════════════════════════
CONTEXT LAYER ANALYSIS
═══════════════════════════════════════════════════════════════════════════

LAYER 1: TEMPORAL CONTEXT
--------------------------
Lifecycle Stage: {self.temporal_context.lifecycle_stage}
Trend Trajectory: {self.temporal_context.trend_trajectory}

Seasonality Comparison:
{self._format_dict(self.temporal_context.seasonality_comparison)}

Recent Events:
{self._format_list_of_dicts(self.temporal_context.recent_events)}

Key Interrogations:
{self._format_dict(self.temporal_context.interrogation_responses)}

LAYER 2: COMPETITIVE CONTEXT
-----------------------------
Market Dynamics: {self.competitive_context.market_dynamics}

Market Share Data:
{self._format_dict(self.competitive_context.market_share_data)}

Industry Benchmarks:
{self._format_dict(self.competitive_context.industry_benchmarks)}

Competitor Actions:
{self._format_list_of_dicts(self.competitive_context.competitor_actions)}

Key Interrogations:
{self._format_dict(self.competitive_context.interrogation_responses)}

LAYER 3: CUSTOMER SEGMENT CONTEXT
----------------------------------
Segment Variance: {self.customer_segment_context.segment_variance_analysis}

Segment Breakdown:
{self._format_dict(self.customer_segment_context.segment_breakdown)}

High-Value Performance:
{self._format_dict(self.customer_segment_context.high_value_performance)}

Key Interrogations:
{self._format_dict(self.customer_segment_context.interrogation_responses)}

LAYER 4: ORGANIZATIONAL CONTEXT
--------------------------------
Strategic Priority: {self.organizational_context.strategic_priority_level}
Process Maturity: {self.organizational_context.process_maturity}

Resource Allocation:
{self._format_dict(self.organizational_context.resource_allocation)}

Organizational Changes:
{self._format_list(self.organizational_context.organizational_changes)}

Key Interrogations:
{self._format_dict(self.organizational_context.interrogation_responses)}

LAYER 5: MACRO-ENVIRONMENTAL CONTEXT
-------------------------------------

ECONOMIC REGIME CLASSIFICATION:
- Growth: {self.macro_environmental_context.growth_regime.value}
- Inflation: {self.macro_environmental_context.inflation_regime.value}
- Interest Rate: {self.macro_environmental_context.interest_rate_regime.value}
- Credit Conditions: {self.macro_environmental_context.credit_conditions.value}
- Investor Sentiment: {self.macro_environmental_context.investor_sentiment.value}

5A: MACROECONOMIC INDICATORS
Federal Funds Rate: {self.macro_environmental_context.macroeconomic_indicators.federal_funds_rate}%
GDP Growth: {self.macro_environmental_context.macroeconomic_indicators.gdp_growth_rate}%
Unemployment: {self.macro_environmental_context.macroeconomic_indicators.unemployment_rate}%
Consumer Confidence: {self.macro_environmental_context.macroeconomic_indicators.consumer_confidence_index}

5B: SECTOR ECONOMICS
Sector Growth Rate: {self.macro_environmental_context.sector_economics.sector_growth_rate}%
VC Funding Trends: {self.macro_environmental_context.sector_economics.vc_funding_trends}
Industry Margins: {self.macro_environmental_context.sector_economics.industry_margin_trends}

5C: MARKET STRUCTURE ECONOMICS
Price Elasticity: {self.macro_environmental_context.market_structure.price_elasticity}
Income Elasticity: {self.macro_environmental_context.market_structure.income_elasticity}
Capacity Utilization: {self.macro_environmental_context.market_structure.capacity_utilization}%

5D: FISCAL & REGULATORY ECONOMICS
Fiscal Policy: {self.macro_environmental_context.fiscal_regulatory.fiscal_policy_stance}
Compliance Cost Burden: {self.macro_environmental_context.fiscal_regulatory.compliance_cost_burden}%

5E: LABOR ECONOMICS
Wage Inflation (Key Roles): {self.macro_environmental_context.labor_economics.wage_inflation_key_roles}%
Turnover Rate: {self.macro_environmental_context.labor_economics.turnover_rate}%
Talent Availability: {self.macro_environmental_context.labor_economics.talent_availability}

5F: INFLATION & PURCHASING POWER
Headline Inflation: {self.macro_environmental_context.inflation_purchasing_power.headline_inflation}%
Core Inflation: {self.macro_environmental_context.inflation_purchasing_power.core_inflation}%
Sector-Specific Inflation: {self.macro_environmental_context.inflation_purchasing_power.sector_specific_inflation}%

5G: FINANCIAL MARKETS
Credit Spreads: {self.macro_environmental_context.financial_markets.credit_spreads}bps
IPO/Exit Environment: {self.macro_environmental_context.financial_markets.ipo_exit_environment}
Investor Sentiment: {self.macro_environmental_context.financial_markets.investor_sentiment.value}

LAYER 6: MEASUREMENT INTEGRITY
-------------------------------
Methodology: {self.measurement_integrity_context.data_collection_methodology}
Definition Consistent: {self.measurement_integrity_context.definition_consistency}
Sample Size: {self.measurement_integrity_context.sample_size}
Statistically Significant: {self.measurement_integrity_context.statistical_significance}

Instrumentation Bias:
{self._format_list(self.measurement_integrity_context.instrumentation_bias)}

Key Interrogations:
{self._format_dict(self.measurement_integrity_context.interrogation_responses)}

LAYER 7: STRATEGIC ALIGNMENT
-----------------------------
Goal Hierarchy:
{self._format_dict(self.strategic_alignment_context.goal_hierarchy)}

Trade-offs:
{self._format_list(self.strategic_alignment_context.trade_offs)}

Stakeholder Expectations:
{self._format_dict(self.strategic_alignment_context.stakeholder_expectations)}

Key Interrogations:
{self._format_dict(self.strategic_alignment_context.interrogation_responses)}

═══════════════════════════════════════════════════════════════════════════
INTEGRATED INTERPRETATION
═══════════════════════════════════════════════════════════════════════════

IDENTIFIED PATTERNS
-------------------
{self._format_patterns(self.identified_patterns)}

WEIGHTED INTERPRETATION
-----------------------
Confidence Level: {self.weighted_interpretation.confidence_level.value.upper()}

Primary Interpretation:
{self.weighted_interpretation.primary_interpretation}

Alternative Interpretations:
{self._format_alternatives(self.weighted_interpretation.alternative_interpretations)}

Confidence Rationale:
{self.weighted_interpretation.confidence_rationale}

Layer Relevance Weights:
{self._format_dict(self.weighted_interpretation.layer_weights)}

═══════════════════════════════════════════════════════════════════════════
ECONOMIC CONTEXT ANALYSIS
═══════════════════════════════════════════════════════════════════════════

ECONOMIC SENSITIVITY ANALYSIS
------------------------------
{self._format_sensitivities(self.economic_context_analysis.sensitivity_analysis)}

ECONOMIC SCENARIO MODELING
---------------------------
{self._format_scenarios(self.economic_context_analysis.scenarios)}

ECONOMIC RISK FACTORS
----------------------
{self._format_risks(self.economic_context_analysis.risk_factors)}

ECONOMIC OPPORTUNITY FACTORS
-----------------------------
{self._format_list(self.economic_context_analysis.opportunity_factors)}

LEADING INDICATOR DASHBOARD
----------------------------
{self._format_dict(self.economic_context_analysis.leading_indicator_dashboard)}

═══════════════════════════════════════════════════════════════════════════
STRATEGIC IMPLICATIONS & ACTIONABILITY
═══════════════════════════════════════════════════════════════════════════

ENABLED DECISIONS
-----------------
{self._format_list(self.actionability_assessment.enabled_decisions)}

RECOMMENDED ACTIONS
-------------------
{self._format_list(self.actionability_assessment.recommended_actions)}

ADDITIONAL DATA NEEDED
----------------------
{self._format_list(self.actionability_assessment.additional_data_needed)}

MONITORING PLAN
---------------
Cadence: {self.actionability_assessment.monitoring_cadence}

Success Metrics:
{self._format_list(self.actionability_assessment.success_metrics)}

╔═══════════════════════════════════════════════════════════════════════════╗
║                          END OF REPORT                                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""
        return report
    
    # Helper formatting methods
    def _format_dict(self, d: Dict) -> str:
        if not d:
            return "  (None provided)"
        return "\n".join([f"  • {k}: {v}" for k, v in d.items()])
    
    def _format_list(self, lst: List) -> str:
        if not lst:
            return "  (None provided)"
        return "\n".join([f"  • {item}" for item in lst])
    
    def _format_list_of_dicts(self, lst: List[Dict]) -> str:
        if not lst:
            return "  (None provided)"
        result = []
        for item in lst:
            result.append("  • " + ", ".join([f"{k}: {v}" for k, v in item.items()]))
        return "\n".join(result)
    
    def _format_patterns(self, patterns: List[ContextPattern]) -> str:
        if not patterns:
            return "  (None identified)"
        result = []
        for p in patterns:
            result.append(f"""
  Pattern Type: {p.pattern_type}
  Involved Layers: {', '.join(p.involved_layers)}
  Description: {p.description}
  Causal Relationships: {', '.join(p.causal_relationships)}
""")
        return "\n".join(result)
    
    def _format_alternatives(self, alternatives: List[Tuple[str, float]]) -> str:
        if not alternatives:
            return "  (None provided)"
        return "\n".join([f"  • {interp} (Probability: {prob:.1%})" 
                         for interp, prob in alternatives])
    
    def _format_sensitivities(self, sensitivities: List[EconomicSensitivity]) -> str:
        if not sensitivities:
            return "  (None provided)"
        result = []
        for s in sensitivities:
            result.append(f"""
  Factor: {s.factor}
  Sensitivity: {s.sensitivity_level.value} (r = {s.correlation_coefficient:.2f})
  Explanation: {s.explanation}
""")
        return "\n".join(result)
    
    def _format_scenarios(self, scenarios: List[EconomicScenario]) -> str:
        if not scenarios:
            return "  (None provided)"
        result = []
        for s in scenarios:
            result.append(f"""
  Scenario: {s.scenario_name.upper()} (Probability: {s.probability:.1%})
  GDP Growth: {s.gdp_growth}%
  Interest Rate Forecast: {s.interest_rate_forecast}%
  Metric Forecast: {s.metric_forecast}
  Explanation: {s.forecast_explanation}
  Key Assumptions:
{self._format_list(s.key_assumptions)}
""")
        return "\n".join(result)
    
    def _format_risks(self, risks: List[EconomicRiskFactor]) -> str:
        if not risks:
            return "  (None identified)"
        result = []
        for r in risks:
            result.append(f"""
  Risk: {r.risk_description}
  Probability: {r.probability:.1%} | Impact: {r.impact_severity}
  Leading Indicators: {', '.join(r.leading_indicators)}
  Mitigation: {'; '.join(r.mitigation_strategies)}
""")
        return "\n".join(result)


# ============================================================================
# MDCM WORKFLOW ENGINE
# ============================================================================

class MDCMWorkflow:
    """
    Multi-Dimensional Contextual Matrix Workflow Engine
    
    Orchestrates the complete MDCM analysis process from metric isolation
    through actionability assessment.
    """
    
    def __init__(self, metric_name: str, analyst: str):
        self.metric_name = metric_name
        self.analyst = analyst
        self.analysis_date = datetime.now()
    
    def stage1_metric_isolation(
        self,
        raw_value: float,
        time_period: str,
        scope: str,
        initial_observation: str
    ) -> Dict[str, Any]:
        """Stage 1: Metric Isolation & Initial Observation"""
        return {
            "raw_metric_value": raw_value,
            "time_period": time_period,
            "scope": scope,
            "initial_observation": initial_observation
        }
    
    def stage2_context_mapping(
        self,
        temporal: TemporalContext,
        competitive: CompetitiveContext,
        customer_segment: CustomerSegmentContext,
        organizational: OrganizationalContext,
        macro_environmental: MacroEnvironmentalContext,
        measurement_integrity: MeasurementIntegrityContext,
        strategic_alignment: StrategicAlignmentContext
    ) -> Dict[str, Any]:
        """Stage 2: Systematic Context Mapping"""
        return {
            "temporal_context": temporal,
            "competitive_context": competitive,
            "customer_segment_context": customer_segment,
            "organizational_context": organizational,
            "macro_environmental_context": macro_environmental,
            "measurement_integrity_context": measurement_integrity,
            "strategic_alignment_context": strategic_alignment
        }
    
    def stage3_context_integration(
        self,
        contexts: Dict[str, Any]
    ) -> List[ContextPattern]:
        """Stage 3: Context Integration & Pattern Recognition"""
        patterns = []
        
        # This is where you would implement pattern detection logic
        # For now, returning empty list - to be implemented based on specific use case
        
        return patterns
    
    def stage4_weighted_interpretation(
        self,
        contexts: Dict[str, Any],
        patterns: List[ContextPattern],
        layer_weights: Dict[str, float]
    ) -> WeightedInterpretation:
        """Stage 4: Weighted Interpretation"""
        
        # This would contain your interpretation logic
        # Placeholder implementation
        
        primary_interpretation = "Placeholder: Integrate weighted context analysis here"
        alternatives = [
            ("Alternative interpretation 1", 0.3),
            ("Alternative interpretation 2", 0.2)
        ]
        
        return WeightedInterpretation(
            primary_interpretation=primary_interpretation,
            alternative_interpretations=alternatives,
            confidence_level=ConfidenceLevel.MEDIUM,
            confidence_rationale="Based on available context data",
            layer_weights=layer_weights
        )
    
    def stage5_actionability_assessment(
        self,
        interpretation: WeightedInterpretation
    ) -> ActionabilityAssessment:
        """Stage 5: Actionability Assessment"""
        
        # Placeholder implementation
        
        return ActionabilityAssessment(
            enabled_decisions=["Decision 1", "Decision 2"],
            recommended_actions=["Action 1", "Action 2"],
            additional_data_needed=["Data point 1", "Data point 2"],
            monitoring_cadence="Weekly",
            success_metrics=["Metric 1", "Metric 2"]
        )
    
    def conduct_economic_analysis(
        self,
        macro_context: MacroEnvironmentalContext,
        metric_historical_data: Optional[Dict[str, List[float]]] = None
    ) -> EconomicContextAnalysis:
        """Conduct comprehensive economic context analysis"""
        
        # Economic regime classification
        regime_classification = {
            "growth": macro_context.growth_regime.value,
            "inflation": macro_context.inflation_regime.value,
            "interest_rate": macro_context.interest_rate_regime.value,
            "credit": macro_context.credit_conditions.value,
            "investor_sentiment": macro_context.investor_sentiment.value
        }
        
        # Placeholder sensitivity analysis
        sensitivities = [
            EconomicSensitivity(
                factor="Consumer Confidence",
                sensitivity_level=SensitivityLevel.HIGH,
                correlation_coefficient=0.75,
                explanation="Historical strong correlation with metric performance"
            ),
            EconomicSensitivity(
                factor="Interest Rates",
                sensitivity_level=SensitivityLevel.MODERATE,
                correlation_coefficient=-0.45,
                explanation="Negative correlation due to cost of capital impact"
            )
        ]
        
        # Scenario modeling
        scenarios = [
            EconomicScenario(
                scenario_name="base",
                probability=0.60,
                gdp_growth=1.5,
                interest_rate_forecast=5.0,
                key_assumptions=[
                    "Soft landing achieved",
                    "No major financial disruptions",
                    "Gradual monetary policy easing"
                ],
                metric_forecast=0.0,  # To be calculated
                forecast_explanation="Moderate growth with stabilizing conditions"
            ),
            EconomicScenario(
                scenario_name="downside",
                probability=0.25,
                gdp_growth=-1.0,
                interest_rate_forecast=4.5,
                key_assumptions=[
                    "Recession occurs",
                    "Credit conditions tighten significantly",
                    "Consumer spending contracts"
                ],
                metric_forecast=0.0,  # To be calculated
                forecast_explanation="Economic contraction impacts performance"
            ),
            EconomicScenario(
                scenario_name="upside",
                probability=0.15,
                gdp_growth=3.0,
                interest_rate_forecast=4.0,
                key_assumptions=[
                    "Strong recovery",
                    "Productivity gains materialize",
                    "Business confidence rebounds"
                ],
                metric_forecast=0.0,  # To be calculated
                forecast_explanation="Favorable economic conditions drive growth"
            )
        ]
        
        # Risk factors
        risks = [
            EconomicRiskFactor(
                risk_description="Customer financial distress due to high interest rates",
                probability=0.35,
                impact_severity="high",
                leading_indicators=[
                    "Customer payment delays",
                    "Credit rating downgrades",
                    "Bankruptcy filings in customer base"
                ],
                mitigation_strategies=[
                    "Implement flexible payment terms",
                    "Diversify customer base",
                    "Build cash reserves"
                ]
            )
        ]
        
        # Opportunity factors
        opportunities = [
            "Market consolidation creating acquisition targets",
            "Competitor weakness enabling market share gains",
            "Technological disruption favoring nimble players"
        ]
        
        # Leading indicators
        leading_indicators = {
            "Consumer Confidence Index": macro_context.macroeconomic_indicators.consumer_confidence_index,
            "Credit Spreads": macro_context.financial_markets.credit_spreads,
            "Unemployment Rate": macro_context.macroeconomic_indicators.unemployment_rate,
            "Sector VC Funding": 0.0  # Placeholder
        }
        
        return EconomicContextAnalysis(
            regime_classification=regime_classification,
            key_indicators={
                "gdp_growth": macro_context.macroeconomic_indicators.gdp_growth_rate,
                "inflation": macro_context.inflation_purchasing_power.headline_inflation,
                "interest_rate": macro_context.macroeconomic_indicators.federal_funds_rate
            },
            sensitivity_analysis=sensitivities,
            scenarios=scenarios,
            risk_factors=risks,
            opportunity_factors=opportunities,
            leading_indicator_dashboard=leading_indicators
        )
    
    def execute_full_analysis(
        self,
        raw_value: float,
        time_period: str,
        scope: str,
        initial_observation: str,
        temporal: TemporalContext,
        competitive: CompetitiveContext,
        customer_segment: CustomerSegmentContext,
        organizational: OrganizationalContext,
        macro_environmental: MacroEnvironmentalContext,
        measurement_integrity: MeasurementIntegrityContext,
        strategic_alignment: StrategicAlignmentContext,
        layer_weights: Optional[Dict[str, float]] = None
    ) -> ContextualizedMetricBrief:
        """
        Execute complete MDCM analysis workflow
        
        Returns a comprehensive ContextualizedMetricBrief
        """
        
        # Default layer weights if not provided
        if layer_weights is None:
            layer_weights = {
                "temporal": 0.15,
                "competitive": 0.15,
                "customer_segment": 0.20,
                "organizational": 0.10,
                "macro_environmental": 0.25,
                "measurement_integrity": 0.05,
                "strategic_alignment": 0.10
            }
        
        # Stage 1: Metric Isolation
        metric_data = self.stage1_metric_isolation(
            raw_value, time_period, scope, initial_observation
        )
        
        # Stage 2: Context Mapping
        contexts = self.stage2_context_mapping(
            temporal, competitive, customer_segment, organizational,
            macro_environmental, measurement_integrity, strategic_alignment
        )
        
        # Stage 3: Context Integration
        patterns = self.stage3_context_integration(contexts)
        
        # Stage 4: Weighted Interpretation
        interpretation = self.stage4_weighted_interpretation(
            contexts, patterns, layer_weights
        )
        
        # Stage 5: Actionability Assessment
        actionability = self.stage5_actionability_assessment(interpretation)
        
        # Economic Analysis
        economic_analysis = self.conduct_economic_analysis(macro_environmental)
        
        # Create Contextualized Metric Brief
        brief = ContextualizedMetricBrief(
            metric_name=self.metric_name,
            analysis_date=self.analysis_date,
            analyst=self.analyst,
            raw_metric_value=raw_value,
            time_period=time_period,
            scope=scope,
            initial_observation=initial_observation,
            temporal_context=temporal,
            competitive_context=competitive,
            customer_segment_context=customer_segment,
            organizational_context=organizational,
            macro_environmental_context=macro_environmental,
            measurement_integrity_context=measurement_integrity,
            strategic_alignment_context=strategic_alignment,
            identified_patterns=patterns,
            weighted_interpretation=interpretation,
            actionability_assessment=actionability,
            economic_context_analysis=economic_analysis
        )
        
        # Generate executive summary
        brief.generate_executive_summary()
        
        return brief


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def example_workflow():
    """
    Example demonstrating complete MDCM workflow execution
    """
    
    # Initialize workflow
    workflow = MDCMWorkflow(
        metric_name="Monthly Active Users (MAU)",
        analyst="Juliet"
    )
    
    # Prepare context data
    temporal = TemporalContext(
        measurement_period="December 2024",
        seasonality_comparison={"2023": 80000, "2022": 75000, "2021": 70000},
        trend_trajectory="ascending",
        recent_events=[
            {"date": "2024-12-05", "event": "Competitor major outage", "impact": "5-day service disruption"},
            {"date": "2024-11-15", "event": "Reduced account creation friction", "impact": "Lower signup barriers"}
        ],
        lifecycle_stage="growth"
    )
    temporal.add_interrogation(
        "What was our performance in this exact period last year?",
        "80,000 MAU in December 2023, representing 25% growth YoY"
    )
    
    competitive = CompetitiveContext(
        market_share_data={"Our Company": 15.5, "Competitor A": 35.0, "Competitor B": 25.0},
        competitor_actions=[
            {"date": "2024-12-05", "competitor": "Competitor A", "action": "Major service outage (5 days)"}
        ],
        industry_benchmarks={"MAU Growth Rate": 12.0, "Free-to-Paid Conversion": 5.5},
        market_dynamics="market_expansion"
    )
    
    customer_segment = CustomerSegmentContext(
        segment_breakdown={"Free Tier": 80000, "Paid Tier": 20000},
        cohort_analysis={
            "Q4 2024": {"mau": 25000, "conversion": 3.0},
            "Q3 2024": {"mau": 20000, "conversion": 5.0}
        },
        high_value_performance={"enterprise": 5000, "growth": 2.0},
        segment_variance_analysis="80% of growth from free tier, paid flat"
    )
    
    organizational = OrganizationalContext(
        resource_allocation={"budget": 500000, "headcount": 12, "tools": "standard"},
        strategic_priority_level="medium",
        team_composition={"engineers": 6, "product": 3, "marketing": 3},
        process_maturity="established",
        organizational_changes=[]
    )
    
    # Economic context components
    macroeconomic = MacroeconomicIndicators(
        federal_funds_rate=5.5,
        interest_rate_trajectory="restrictive",
        cost_of_capital=8.5,
        gdp_growth_rate=1.8,
        unemployment_rate=3.8,
        consumer_confidence_index=88.0,
        business_investment_trends="contracting"
    )
    
    sector = SectorEconomics(
        sector_growth_rate=8.0,
        vc_funding_trends="down 30% YoY",
        industry_margin_trends="compressing",
        customer_industry_health={"smb": "stressed", "enterprise": "stable"},
        customer_financial_stress_indicators=["15% increase in payment delays"]
    )
    
    market_structure = MarketStructureEconomics(
        input_cost_dynamics={"cloud_infrastructure": 11.0, "labor": 23.0},
        supply_chain_pressures="moderate",
        capacity_utilization=75.0,
        price_elasticity=-1.8,
        income_elasticity=1.2,
        substitution_effects="increasing to free alternatives"
    )
    
    fiscal_regulatory = FiscalRegulatoryEconomics(
        fiscal_policy_stance="neutral",
        tax_policy_changes=["R&D credit expansion"],
        subsidy_programs=[],
        compliance_cost_burden=5.0,
        regulatory_uncertainty="moderate"
    )
    
    labor = LaborEconomics(
        wage_inflation_key_roles=7.5,
        talent_availability="tight",
        turnover_rate=15.0,
        productivity_trends="stable",
        wage_competitiveness="competitive"
    )
    
    inflation = InflationPurchasingPower(
        headline_inflation=4.2,
        core_inflation=3.8,
        sector_specific_inflation=6.1,
        real_vs_nominal_growth={"nominal": 25.0, "real": 18.9},
        wage_price_dynamics="wages lagging prices"
    )
    
    financial_markets = FinancialMarkets(
        equity_market_valuations={"saas_multiple": 6.0, "previous": 12.0},
        credit_spreads=250.0,
        ipo_exit_environment="frozen",
        investor_sentiment=InvestorSentiment.RISK_OFF
    )
    
    macro_environmental = MacroEnvironmentalContext(
        macroeconomic_indicators=macroeconomic,
        sector_economics=sector,
        market_structure=market_structure,
        fiscal_regulatory=fiscal_regulatory,
        labor_economics=labor,
        inflation_purchasing_power=inflation,
        financial_markets=financial_markets,
        growth_regime=GrowthRegime.MODERATE_GROWTH,
        inflation_regime=InflationRegime.MODERATE,
        interest_rate_regime=InterestRateRegime.RESTRICTIVE,
        credit_conditions=CreditConditions.TIGHT,
        investor_sentiment=InvestorSentiment.RISK_OFF,
        technological_shifts=["AI integration becoming table stakes"],
        social_cultural_movements=["Remote work normalization"]
    )
    
    measurement_integrity = MeasurementIntegrityContext(
        data_collection_methodology="Server-side tracking via analytics platform",
        definition_consistency=True,
        sample_size=100000,
        statistical_significance=True,
        instrumentation_bias=["Free tier users may have multiple accounts"],
        methodology_changes=["Lowered account creation friction in November"]
    )
    
    strategic_alignment = StrategicAlignmentContext(
        goal_hierarchy={"MAU": "Volume metric", "Strategic Goal": "High-value customer acquisition"},
        trade_offs=["Optimized volume over monetization", "Free tier growth over paid growth"],
        stakeholder_expectations={"Board": 90000, "Investors": 95000},
        opportunity_costs=["Could have focused on enterprise sales", "Delayed feature development"]
    )
    
    # Execute full analysis
    brief = workflow.execute_full_analysis(
        raw_value=100000,
        time_period="December 2024",
        scope="All user segments, global",
        initial_observation="25% MoM increase appears strong but needs context",
        temporal=temporal,
        competitive=competitive,
        customer_segment=customer_segment,
        organizational=organizational,
        macro_environmental=macro_environmental,
        measurement_integrity=measurement_integrity,
        strategic_alignment=strategic_alignment
    )
    
    # Generate and print report
    report = brief.generate_report()
    print(report)
    
    # Export to JSON
    brief.export_to_json("mdcm_analysis_mau_dec2024.json")
    
    return brief


if __name__ == "__main__":
    # Run example workflow
    example_brief = example_workflow()
    
    print("\n" + "="*80)
    print("MDCM Workflow executed successfully!")
    print("="*80)