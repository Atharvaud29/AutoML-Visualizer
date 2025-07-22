# app/utils/explanation_engine.py

def explain_preprocessing_step(df, step='missing_values'):
    if step == 'missing_values':
        missing = df.isnull().sum()
        missing_cols = missing[missing > 0].to_dict()
        return {
            'step': 'Missing Value Detection',
            'summary': f'{len(missing_cols)} columns have missing values.',
            'details': missing_cols,
            'reason': 'Handling missing values ensures the model doesn’t fail or produce biased results.'
        }

    elif step == 'categorical_encoding':
        cat_cols = df.select_dtypes(include='object').columns.tolist()
        return {
            'step': 'Categorical Feature Encoding',
            'summary': f'{len(cat_cols)} categorical column(s) detected.',
            'details': {col: 'object' for col in cat_cols},
            'reason': 'Most ML models require categorical features to be converted to numbers using encoding.'
        }

    elif step == 'scaling':
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        return {
            'step': 'Numerical Feature Scaling',
            'summary': f'{len(num_cols)} numeric column(s) detected.',
            'details': {col: str(df[col].dtype) for col in num_cols},
            'reason': 'Scaling numeric features helps models converge faster and avoid being biased by magnitude.'
        }

    return {
        'step': step,
        'summary': 'Step explanation not implemented yet.',
        'details': {},
        'reason': ''
    }
