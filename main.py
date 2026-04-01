from src.pipeline import run_pipeline
from src.pipeline import load_data

def main():
    data = load_data()
    run_pipeline(data)

if __name__ == "__main__":
    main()
