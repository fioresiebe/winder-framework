# Multi-Dimensional Contextual Matrix (MDCM)

A rigorous Python framework for holistic data interpretation that goes beyond surface-level metrics analysis.

## Overview

The MDCM framework systematically evaluates business metrics through seven critical context layers plus comprehensive economic analysis, transforming gut-feel interpretation into reproducible, defensible methodology.

**Problem it solves:** Most organizations make strategic decisions based on metrics taken at face value, missing critical context that fundamentally changes interpretation.

**Solution:** Structured workflows that force comprehensive contextual analysis before drawing conclusions from data.

## Features

- **7-Layer Context Analysis**: Temporal, Competitive, Customer Segment, Organizational, Macro-Environmental, Measurement Integrity, Strategic Alignment
- **Economic Framework**: Macroeconomic indicators, sector dynamics, market structure, fiscal/regulatory environment, labor economics, inflation analysis, financial markets
- **Scenario Modeling**: Base/upside/downside economic scenarios with probability weighting
- **Risk Assessment**: Systematic identification of economic and strategic risk factors
- **Exportable Reports**: Generate comprehensive PDF-style reports and structured JSON outputs
- **Production-Ready**: Clean Python code with type hints, dataclasses, and documentation

## Installation

### Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/julietgalliano/mdcm-workflow.git
cd mdcm-workflow
```

2. The framework is ready to use - no installation required!

## Quick Start
```python
from mdcm_workflow import MDCMWorkflow, TemporalContext, CompetitiveContext
# ... other imports

# Initialize workflow
workflow = MDCMWorkflow(
    metric_name="Monthly Active Users",
    analyst="Your Name"
)

# Create context objects with your data
temporal = TemporalContext(
    measurement_period="Q4 2024",
    seasonality_comparison={"2023": 80000, "2022": 75000},
    trend_trajectory="ascending",
    recent_events=[{"date": "2024-12-01", "event": "Product launch", "impact": "Major"}],
    lifecycle_stage="growth"
)

# ... define other contexts ...

# Execute analysis
brief = workflow.execute_full_analysis(
    raw_value=100000,
    time_period="Q4 2024",
    scope="Global",
    initial_observation="Strong growth observed",
    temporal=temporal,
    competitive=competitive,
    customer_segment=customer_segment,
    organizational=organizational,
    macro_environmental=macro_environmental,
    measurement_integrity=measurement_integrity,
    strategic_alignment=strategic_alignment
)

# Generate outputs
print(brief.generate_report())
brief.export_to_json("analysis_output.json")
```

## Use Cases

- **Investment Analysis**: Evaluate whether startup metrics indicate real traction or context-driven illusions
- **Strategic Planning**: Make data-informed decisions with full contextual understanding
- **Consulting**: Produce rigorous client reports that go beyond surface-level analysis
- **Education**: Teach students systematic approaches to data interpretation
- **Product Analytics**: Understand what's really driving metric movements

## Framework Philosophy

The MDCM is built on three core principles:

1. **No metric exists in a vacuum** - All data must be interpreted through multiple contextual lenses
2. **Systematic beats intuitive** - Structured frameworks prevent cognitive biases and blind spots
3. **Context determines meaning** - The same number can indicate success, failure, or neutrality depending on surrounding conditions

## Documentation

### The Seven Context Layers

1. **Temporal Context**: Seasonality, trends, lifecycle stage, event proximity
2. **Competitive Context**: Market share, competitor actions, industry benchmarks
3. **Customer Segment Context**: Disaggregation, cohort analysis, high-value performance
4. **Organizational Context**: Resource allocation, team changes, strategic priorities
5. **Macro-Environmental Context**: Economic indicators, sector dynamics, market structure, fiscal policy, labor economics, inflation, financial markets
6. **Measurement Integrity**: Methodology consistency, statistical significance, instrumentation bias
7. **Strategic Alignment**: Goal hierarchy, trade-offs, stakeholder expectations, opportunity costs

### Output: Contextualized Metric Brief (CMB)

Each analysis produces a comprehensive brief containing:
- Executive summary
- Raw metric performance
- 7-layer context analysis with interrogation responses
- Pattern identification (confluence/contradiction)
- Weighted interpretation with confidence levels
- Economic scenario modeling
- Risk and opportunity factors
- Actionable recommendations
- Monitoring plan

## Examples

See `examples/` directory for:
- SaaS revenue growth analysis
- E-commerce conversion rate evaluation
- Mobile app engagement assessment

## Contributing

Contributions welcome! This framework is designed to be extended and adapted. Areas for contribution:

- Additional economic models
- Pattern detection algorithms
- Industry-specific context layers
- Visualization tools
- Integration with data sources

## Roadmap

**Workflow 2**: Combining Qualitative + Quantitative Analysis (coming soon)

**Workflow 3**: Applying Critical Lenses to Data (coming soon)

## License

MIT License - see LICENSE file for details

## Author

Created by Juliet - bridging legal frameworks, technical systems, and strategic thinking.

## Citation

If you use this framework in academic work, please cite:
```
Multi-Dimensional Contextual Matrix (MDCM)
https://github.com/julietgalliano/mdcm-workflow
```

## Support

For questions, issues, or discussions, please open an issue on GitHub.

---

**Note**: This framework provides structured analytical methodology. The interpretation logic in stages 3-5 are currently placeholder implementations designed to be customized for specific use cases. The framework excels at organizing context systematically; domain expertise is required for final interpretation.