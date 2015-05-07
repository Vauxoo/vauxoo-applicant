
# pylint: disable=E1601

"""
Script to test postgres scripts for applicant project
"""

import os
import subprocess
import unittest


PG_USER = os.environ.get('PG_USER', False)


def run_output(cmd, cwd=None):
    """
    Method to run a command in OS
    """
    return subprocess.Popen(
        cmd, stdout=subprocess.PIPE, cwd=cwd).communicate()[0]


def run_psql_query(query, dbname):
    """
    Method to run a psql query command in OS
    """
    cmd = ['psql', '-d', dbname, '-c', query]
    if PG_USER:
        cmd.extend(['-U', PG_USER])
    res = run_output(cmd)
    return res


def psql_output2list(psql_output):
    """
    Method to run a psql query command in OS
    and return list of rows
    """
    newline_count = 0
    lines = []
    for line in psql_output.split('\n'):
        newline_count += 1
        if newline_count == 2:
            # don't append line of '---+---'
            # returned by psql commands
            continue
        new_line = []
        for item in line.split('|'):
            item = item.strip()
            new_line.append(item)
        lines.append(new_line)
    lines = lines[:-3]
    return lines


def psql_output2dict(psql_output):
    """
    Method to run a psql query command in OS
    and return dicts of rows
    where first row is header of keys.
    """
    psql_list = psql_output2list(psql_output)
    return [dict(zip(psql_list[0], row)) for row in psql_list[1:]]


class TestApplicantPostgres(unittest.TestCase):
    """
    Main class to test postgres scripts for applicant project
    """

    def setUp(self):
        """
        Method init of global unittest class
        """
        self.dbname = 'employee_employee'
        self.required_tables = [
            'employee',
            'employee_department',
            'employee_hobby',
        ]
        self.required_fields = {
            'employee': [
                'id', 'first_name', 'last_name',
            ],
            'employee_department': [
                'id', 'name', 'description',
            ],
            'employee_hobby': [
                'id', 'name', 'description',
            ],
        }
        self.required_fields_qty = {
            'employee': 5,
            'employee_department': 3,
            'employee_hobby': 3,
        }
        self.required_records = {
            'employee': 4,
            'employee_department': 6,
            'employee_hobby': 3,
        }

    def test_05_db_tables_requested(self):
        """
        Method to verify that exists requested tables
        """
        print "Start test:" + \
              self.test_05_db_tables_requested.__doc__
        query = """SELECT table_name
                FROM information_schema.tables
                WHERE  table_schema='public'"""
        res = run_psql_query(query, self.dbname)
        res_dict = psql_output2dict(res)
        table_names = [row['table_name'] for row in res_dict]
        for required_table in self.required_tables:
            self.assertEqual(
                required_table in table_names, True,
                "don't exists '%s' table requested"
                % (required_table))
        if len(table_names) == 3:
            print "WARNING: Additional table not implement yet"
        self.assertEqual(
            len(table_names) == 3 or len(table_names) == 4, True,
            "You have created different quantity of tables expected.")
        print "End test:" + \
              self.test_05_db_tables_requested.__doc__

    def test_10_db_fields_requested(self):
        """
        Method to get fields of tables
        and check that requested fields exists
        """
        print "Start test:" + \
              self.test_10_db_fields_requested.__doc__
        for table_name in self.required_fields:
            query = """SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = '%s'""" % table_name
            res = run_psql_query(query, self.dbname)
            res_dict = psql_output2dict(res)
            column_names = [row['column_name'] for row in res_dict]
            if len(column_names) == 0:
                print "WARNING: '%s' Not implement yet" % (table_name, )
                continue
            for required_field in self.required_fields[table_name]:
                self.assertEqual(
                    required_field in column_names, True,
                    "don't exists '%s' column in table '%s'"
                    % (required_field, table_name))
            self.assertEqual(
                self.required_fields_qty[table_name], len(column_names),
                "You have created different quantity of fields" +
                " expected in table '%s'."
                % (table_name))

        # Get all aditional tables (don't exists in required tables)
        query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE  table_schema='public'
            AND table_name NOT IN (%s)""" % \
            ("'" + "','".join(self.required_tables) + "'")
        res = run_psql_query(query, self.dbname)
        res_dict = psql_output2dict(res)
        if len(res_dict) == 0:
            print "WARNING: SECRET TEST CASE not implement yet"
        self.assertEqual(
            len(res_dict) in (0, 1), True,
            "You have created different quantity of tables expected.")

        if len(res_dict) == 1:
            new_table = res_dict[0]['table_name']
            query = """SELECT column_name
                        FROM information_schema.columns
                        WHERE table_name = '%s'""" % new_table
            res = run_psql_query(query, self.dbname)
            res_dict = psql_output2dict(res)
            column_names = [row['column_name'] for row in res_dict]
            self.assertEqual(
                len(column_names), 2,
                "You have different quantity of columns" +
                " expected in table '%s'." % new_table)
        print "End test:" + \
              self.test_10_db_fields_requested.__doc__

    def test_20_db_records_requested(self):
        """
        Method to get numbers of records in tables
        and check that requested records is equal
        to inserted records
        """
        print "Start test:" + \
              self.test_20_db_records_requested.__doc__
        for table_name in self.required_records:
            query = """SELECT *
                    FROM %s""" % table_name
            res = run_psql_query(query, self.dbname)
            res_dict = psql_output2dict(res)
            if len(res_dict) == 0:
                print "WARNING: '%s' Not implement yet" % (table_name, )
            self.assertEqual(
                self.required_records[table_name] == len(res_dict)
                or len(res_dict) == 0,
                True,
                "Request records in table '%s'=%d. Records found=%d"
                % (
                    table_name,
                    self.required_records[table_name],
                    len(res_dict)))
        print "End test:" + \
              self.test_20_db_records_requested.__doc__


if __name__ == '__main__':
    unittest.main()
