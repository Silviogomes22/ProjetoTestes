class CsvExtract:
    def __init__(self) -> None:
        pass

    def extract(self) -> list:
        return list(open("books.csv", "r", encoding="utf-8"))
        
    def format_str_price_to_float(self, price: str) -> float:
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0
