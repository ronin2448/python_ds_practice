class Record():
    def __init__(self, id, last_name, count):
        self.id = id
        self.last_name = last_name
        self.count = count

    def __repr__(self):
        return "id: {} | last name: {} | count: {} ".format(self.id,self.last_name, self.count)

if __name__ == "__main__":
    records = list()
    records.append( Record("A1", "Roberts", 124))
    records.append( Record("C1", "Jefferson", 1))
    records.append( Record("A2", "Li", 224))
    records.append( Record("A4", "Valdez", 5))
    records.append( Record("G1", "Jackson", 8))

    print(records)
    print(sorted(records,key=lambda r : (r.id, r.count)))  # sort by id, count
    print(sorted(records, key=lambda r: (r.id)))  # sort by ascending id
    print(sorted(records, key=lambda r: (str.lower(r.id))))  # sort by id (case insensitve)


    #https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    # Complex sorts
    def descend_id_asc_count(list_vals):
        # sort by id (desc), and count (asc)
        # double sort is possible because sort is stable
        vals = sorted(list_vals, key=lambda r : r.count)
        vals.sort(key=lambda r : r.id, reverse=True)
        return vals

    print( descend_id_asc_count(records))