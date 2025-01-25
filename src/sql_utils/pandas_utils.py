import pandas as pd
from numpy.dtypes import DateTime64DType as dt_dtype

def change_col_types(df,col_list,data_type):
    d_type_cats = [str,int,float,'time']

    for i, col in enumerate(col_list):
        curr_ty = type(df[col].dtype)
        new_dt = data_type[i]
        if (curr_ty, new_dt) == (dt_dtype, str):
            df.loc[:,col] = df[col].dt.strftime("%Y-%m-%d")
        elif new_dt == 'time':
            df.loc[:,col] = pd.to_datetime(df[col], errors='coerce')
        else:
            df.loc[:,col] = df[col].astype(new_dt)
    return df