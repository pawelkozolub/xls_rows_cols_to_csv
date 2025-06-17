from src.config import Config
from src.model import Row, get_rows, update_rows, make_csv


def main():
    config = Config()

    input_file = config.input_file
    output_file = config.output_file
    columns: dict = config.column_data
    rows: list[Row] = get_rows(config.row_data)
    
    print("\nInput and output file paths:")
    print(input_file)
    print(output_file)
    
    print("\nSelected row data:")
    [print(row) for row in rows]

    update_rows(columns, rows, input_file)

    headers = ["parameter", "unit"]
    [headers.append(value) for value in columns.values()]

    make_csv(headers, rows, output_file)


if __name__ == "__main__":
    main()