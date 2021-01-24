
class Tabla(object):

    table_record_template = """
    <tr>
        {data}
    </tr>    
    """

    def __init__(self, table_clase="table", table_id="table"):
        super().__init__()
        self.table_clase = table_clase
        self.columns = list()
        self.records = list()
        self.round = 3
        self.table_id = table_id

    def set_head(self,columns):
        self.columns = columns

    def add_record(self,table_data):
        self.records.append(table_data)

    def get_html_table(self):
        return self.table_template()

    def get_table_head(self):
        records = ""
        table_header = """
            <th scope="col">{value}</th>
        """
        for column in self.columns:
            records += table_header.format(value=str(column))
        return self.table_record_template.format(data=records)

    def get_table_body(self):
        records = ""
        table_body= """
            <td>{value}</td>
        """
        for record in self.records:
            record_str = ""
            for value in record:
                record_str += table_body.format(value=str(value))
            records += self.table_record_template.format(data=record_str)
        return records

    def table_template(self):
        table_html = """
        <table id="{table_id}" class="{table_clase}">
        <thead>
            {table_head}
        </thead>
        <tbody>
            {table_body}
        </tbody>
        </table>
        """
        return table_html.format(table_id=self.table_id,table_clase=self.table_clase, table_head=self.get_table_head(), table_body=self.get_table_body())


    def apriori_table(self,rules):
        self.set_head(["#","Regla","Soporte","Confianza","Elevación"])
        n = 0
        for rule in rules:
            support = round(rule.support,self.round)
            records = None
            for statistic in rule.ordered_statistics:
                items = (",".join(x for x in statistic.items_base), ",".join(x for x in statistic.items_add if x != "nan"))
                confidence = round(statistic.confidence,self.round)
                lift = round(statistic.lift,self.round)
                record = [str(n), self.apriori_rule(items), support, confidence, lift]
                if records is None:
                    records = [record]              
                else:
                    if records[-1][3] != record[3] and records[-1][4] != record[4]:
                        records.append(record)
                n += 1
            for record in records:
                self.add_record(record)
        return self.table_template()

    def apriori_rule(self, items):
        return '{ant} -> {cons}'. format(ant=items[0],cons=items[1])
