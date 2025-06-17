import csv
import openpyxl


class Row():
    def __init__(self, 
            tag: str,
            tab_name: str, 
            row: str, 
            name: str, 
            unit_src: str, 
            conversion: float, 
            unit: str
            ):
        self.tag = tag
        self.tab_name = tab_name
        self.row = row
        self.name = name
        self.unit_src = unit_src
        self.conversion = conversion
        self.unit = unit
        self.values: list[float] = []
    
    def add_value(self, value: float) -> None:
        self.values.append(value * self.conversion)

    def get_values(self) -> list[float]:
        return self.values

    def get_row(self) -> list:
        row = [self.name, self.unit]
        row.extend(self.values)
        return row

    def __str__(self) -> str:
        return f"{self.tag}({self.tab_name}, {self.row}, {self.name}, {self.unit_src}, {self.conversion}, {self.unit})"


def get_rows(row_data: dict) -> list[Row]:
    rows: list[Row] = []
    for k, v in row_data.items():
        rows.append(Row(k, v["tab"], v["row"], v["name"], v["unit_src"], v["conv"], v["unit"]))
    return rows


def update_rows(columns: dict, rows: list[Row], file_path: str) -> None:
    workbook: openpyxl.Workbook = openpyxl.load_workbook(file_path, data_only=True)
    print("\nSelected column data:")
    for col_name, case_name in columns.items():
        print(f"Column: {col_name}, Case: {case_name}")
        for row in rows:
            sheet = workbook[row.tab_name]
            cell_adr = col_name + row.row
            value = sheet[cell_adr].value

            if isinstance(value, (float, int)):
                row.add_value(value)
            elif isinstance(value, str):
                row.add_value(float(value))
            else:
                row.add_value(0.0)
    

def make_csv(headers: list[str], rows: list[Row], filename="result.csv") -> None:
    with open(filename, "w", newline="") as f:
        csvwriter = csv.writer(f, delimiter=";")
        csvwriter.writerow(headers)
        for row in rows:
            csvwriter.writerow(row.get_row())
    print(f"\nOutput file: {filename} has been saved.")