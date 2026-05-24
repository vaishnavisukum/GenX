import joblib
def main():
    model=joblib.load("model.pkl")
    print(model.predict[[7,4,3,2]])


if __name__ == "__main__":
    main()