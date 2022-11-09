import csv


class DBbyCSV:

    def __init__(self, schema, filename):
        self._filename = f"./{filename}.csv"
        try:
            # Check if the file already exits
            f = open(self._filename)
            f.close()
        except IOError:
            # if the file does not exits we create the header
            with open(self._filename, mode="w", encoding="utf-16") as csv_file:
                data_writer = csv.writer(csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                data_writer.writerow(schema.keys())
                
    def insert(self, data):

        id_contact = self.get_last_id() + 1
        line = [id_product] + data

        with open(self._filename, mode="a", encoding="utf-16") as csv_file:
            data_writer = csv.writer(csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
            data_writer.writerow(line)

        return True


    def get_last_id(self):
        
        list_ids = []
        with open(self._filename, mode="r", encoding="utf-16") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            is_header = True
            for row in csv_reader:
                if is_header:
                    is_header = False
                    continue

                if row:
                    list_ids.append(row[0])

        if not list_ids:
            return 0
        
        # we sort the list from largest to smallest and return the element with the large size
        list_ids.sort(reverse = True) 
        return int(list_ids[0])

def get_all(self):

        list_data = []
        list_header = []
        with open(self._filename, mode="r", encoding="utf-16") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value

                    list_data.append(file)

        return list_data

  def get_by_filters(self, filters):

        list_data = []
        list_header = []
        with open(self._filename, mode="r", encoding="utf-16") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}

                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    for key_filter, value_filter in filters.items():
                        matches = re.search(rf"{value_filter}", file[key_filter], re.IGNORECASE)
                        if matches:
                            list_data.append(file)
                            break

        return list_data   


from tempfile import NamedTemporaryFile
import shutil

    def get_by_id(self, id_object):
        list_header = []
        with open(self._filename, mode="r", encoding="utf-16") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    if file["ID"] == id_object:
                        return file

        return {}

      def update(self, id_object, data):
        data_csv = self.get_by_id(id_object)

        if not data_csv:
            raise Exception(" Not found object with  id  send")

        for key, value in data.items():
            data_csv[key] = value

        tempfile = NamedTemporaryFile(mode="w", delete=False, encoding="utf-16")

        list_header = []
        with open(self._filename, mode="r", encoding"utf-16") as csv_file, tempfile:
            csv_reader = csv.reader(csv_file, delimiter=";")
            data_writer = csv.writer(tempfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    data_writer.writerow(row)
                    continue

                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    if file["ID"] != data_csv["ID"]:
                        data_writer.writerow(row)
                        continue

                    for key, value in data_csv.items():
                        file[key] = value

                    data_writer.writerow(file.values())

        shutil.move(tempfile.name, self._filename)
        return True

 def modify_file(self, id_object, data, action):
        data_csv = self.get_by_id(id_object)

        if not data_csv:
            raise Exception( "Not object found with id send ")

        for key, value in data.items():
            data_csv[key] = value

        tempfile = NamedTemporaryFile(mode="w", delete=False, encoding="utf-16")

        list_header = []
        with open(self._filename, mode="r", encoding="utf-16") as csv_file, tempfile:
            csv_reader = csv.reader(csv_file, delimiter=";")
            data_writer = csv.writer(tempfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    data_writer.writerow(row)
                    continue

                # If it is update we update when we do match
                if row and action == "update":
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    if file["ID"] != data_csv["ID"]:
                        data_writer.writerow(row)
                        continue

                    for key, value in data_csv.items():
                        file[key] = value

                    data_writer.writerow(file.values())
                # If it is delete when we do match continue to jump the insert line
                elif row and action == "delete":
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    if file["ID"] == data_csv["ID"]:
                        continue

                    data_writer.writerow(row)

        shutil.move(tempfile.name, self._filename)
        return True


     def delete(self, id_object):
        return self.modify_file(id_object, {}, "delete")

    def update(self, id_object, data):
        return self.modify_file(id_object, data, "update")

    

