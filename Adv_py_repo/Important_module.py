import pandas as pd
def clean_columns (df):
    df.columns = (
        df.columns
            .str.strip()
            .str.upper()
            .str.replace('_', '__')
    )
    return df

import pandas as pd
def clean_columns (df):
    df.columns = (
        df.columns
            .str.strip()
            .str.upper()
            .str.replace('_', '__')
    )
    return df

def missing_summ(df):
    total = df.isna().sum()
    pct = (total / len(df) * 100) .round(2)
    out = pd.DataFrame({"missing_cnt": total,"missing_pct": pct})
    out = out.sort_values(["missing_cnt","missing_pct"], ascending = False)
    return out