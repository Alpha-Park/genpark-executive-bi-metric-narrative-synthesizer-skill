from client import ExecutiveBiMetricNarrativeSynthesizerClient

def main():
    client = ExecutiveBiMetricNarrativeSynthesizerClient()
    res = client.synthesize_executive_brief('CAC Payback Period', 11.2, 14.5)
    print('Executive Narrative Synthesizer: ' + res['narrative_id'])
    print('Brief: ' + res['executive_summary_sentence'])
    print('Memo URL: ' + res['executive_memo_url'])

if __name__ == '__main__':
    main()
