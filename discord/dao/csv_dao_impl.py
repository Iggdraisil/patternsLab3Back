from discord.dao.csv_dao import CSVDao


class CSVDaoImpl(CSVDao):
    def read_from_file(self) -> list[list[str]]:
        with open(self.filename) as file:
            return [
                entry.split(',')[:-1] for entry in file.readlines()
            ]
