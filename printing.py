"""
Make printing text as easy as a Python call.
By Nabeel Sherazi, sherazi.n@husky.neu.edu

This library simplifies the win32print library to make printing more intuitive.

CLASSES:
Printer - Creates a printer object handle. Specify which printer to use by either
string of name or printer number as specified by get_printers static method.

METHODS/CLASS:
Printer.start_job - Starts a new print job. Returns job ID
Printer.write - Write a string to the print spool. Returns number of bytes added.
Printer.send_job - Send the job to be printer. Returns total number of bytes sent to print.
Printer.print_file - Creates job and sends a text file to be printed. Returns tuple of job
ID and total number of bytes printed.

METHODS/STATIC:
get_printers - Enumerates available printers on system.

BUGS:
Email at sherazi.n@husky.neu.edu
"""

import win32print


class Printer:
    """A class to simplify printing text."""
    def __init__(self, printer_name=win32print.GetDefaultPrinter()):
        """Create Printer handle. Specify which printer to use by either string
        of name or number as specified by get_printers method."""
        if type(printer_name) is int:
            printer_name = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)[printer_name][2]
        self.printer = win32print.OpenPrinter(printer_name)

    def start_job(self, doc_name):
        """Start a new print job. Returns job ID"""
        self.job = win32print.StartDocPrinter(self.printer, 1, (doc_name, None, "RAW"))
        self.total_bytes = 0
        win32print.StartPagePrinter(self.printer)
        return self.job

    def write(self, text):
        """Write a string to the print spool. Returns number of bytes added."""
        bytes_sent = win32print.WritePrinter(self.printer, bytes(text, "utf-8"))
        self.total_bytes += bytes_sent
        return bytes_sent

    def send_job(self):
        """Send the job to be printer. Returns total number of bytes sent to print."""
        win32print.EndPagePrinter(self.printer)
        win32print.EndDocPrinter(self.printer)
        return self.total_bytes

    @staticmethod
    def get_printers():
        for num, info in enumerate(win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)):
            print(str(num) + " = " + info[2])

    def print_file(self, fname):
        """Creates job and sends a text file to be printed. Returns tuple of job
        ID and total number of bytes printed."""
        with open(fname, "r") as f:
            self.start_job(str(fname))
            for line in f:
                if len(line) < 80:
                    self.write(line)
                else:
                    start, end = 0, 80
                    while end < len(line):
                        self.write(line)
                        start += 80
                        end += 80
            self.send_job
        return (self.job, self.total_bytes)
