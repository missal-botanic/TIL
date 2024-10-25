
## 공통

### model.fit(X,y)
X는 여러 특성(2D 배열): 여러 샘플과 여러 특성을 고려해야 하기 때문에 2D 배열 형식이 필요합니다.
y는 단일 결과(1D 배열): 각 샘플에 대해 하나의 목표 값만 필요하므로 1D 배열 형식이 필요합니다.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

### LogisticRegression(), DecisionTreeClassifier()

model = LogisticRegression() / model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)



### XGBoost
xgb_model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

xgb_model.fit(X_train, y_train)

y_pred_xgb = xgb_model.predict(X_test)

## 평가

### LogisticRegression(), DecisionTreeClassifier()
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

### XGBoost
mse_xgb = mean_squared_error(y_test, y_pred_xgb)
print(f'XGBoost 모델의 MSE: {mse_xgb}')





