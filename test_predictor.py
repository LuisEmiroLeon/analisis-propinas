from predictor import PredictorPropinas

def test_prediccion_fri_dinner():
    p = PredictorPropinas()
    resultado = p.predecir(20, 2, "Fri", "Dinner")
    assert resultado == 2.97, f"Esperado 2.97, got {resultado}"

def test_prediccion_thur_lunch():
    p = PredictorPropinas()
    resultado = p.predecir(20, 2, "Thur", "Lunch")
    assert resultado == 2.95, f"Esperado 2.95, got {resultado}"

def test_r2():
    p = PredictorPropinas()
    assert p.r2 == 0.4675