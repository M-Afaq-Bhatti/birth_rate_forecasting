def test_model_training():
    from src.data_ingestion import load_latest_data
    from src.preprocessing import preprocess_data
    from src.model import train_model

    df = load_latest_data()
    X, y, _ = preprocess_data(df)
    model = train_model(X, y)
    
    # Basic sanity check
    assert model is not None, "Model training returned None"
