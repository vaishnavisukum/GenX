import joblib
def main():
    model = joblib.load("iris.pkl")

    print(model.predict([[4,2.5,5,3]]))

if __name__ == "__main__":
    main()