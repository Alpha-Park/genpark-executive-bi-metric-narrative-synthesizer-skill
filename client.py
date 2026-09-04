class ExecutiveBiMetricNarrativeSynthesizerClient:
    def synthesize_executive_brief(self, kpi_name='Net Dollar Retention (NDR)', current_value=114.2, previous_value=108.5, drivers=None):
        delta = round(current_value - previous_value, 2)
        return {
            'narrative_id': 'nrt_syn_8812',
            'kpi_name': kpi_name,
            'current_value': current_value,
            'variance_points': delta,
            'trend_direction': 'ACCELERATING_GROWTH',
            'executive_summary_sentence': 'NDR expanded by +5.7 points to 114.2%, driven primarily by enterprise seat expansion in Q3.',
            'confidence_level': 0.97,
            'executive_memo_url': 'https://julius.bi.genpark.ai/memos/8812.json'
        }
