class Output:

    @staticmethod
    def write_to_file(file_to, data):
        with open(file_to, "a") as file:
            file.write(data)
