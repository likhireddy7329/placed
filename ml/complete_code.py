import pandas as pd
def onehot():
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.model_selection import train_test_split
    df = pd.read_csv("C:\\placement prediction\placement_prediction_app\placement_predict_50k_Dataset1.csv")
    nominal_cols = ['Gender','City']
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['PlacementStatus'])
    ohe = OneHotEncoder(drop='first',sparse_output=False,handle_unknown='ignore')
    train_ohe = ohe.fit_transform(train_df[nominal_cols])
    test_ohe = OneHotEncoder(drop='first',handle_unknown='ignore')
    ohe_cols= ohe.get_feature_names_out(nominal_cols)
    train_ohe_df=pd.DataFrame(train_ohe, columns=ohe_cols, index=train_df.index)
    print(train_ohe_df.head())
    #df = load_data()
    #summarize(df)

    #
    #
    #outlier(df)
onehot()