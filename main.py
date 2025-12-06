from utils import fetch_data, process_data, save_to_csv


def main():
    url = "https://jsonplaceholder.typicode.com/users"
    raw = fetch_data(url)
    processed = process_data(raw)
    save_to_csv(processed, 'data.csv')

if __name__ == "__main__":
    main()
