# Decorator for report formatting
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print("        DYNAMIC REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Report:
    template = "General Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def set_template(cls, new_template):
        cls.template = new_template

    # Magic Method
    def __str__(self):
        return f"Template : {Report.template}\nTitle    : {self.title}\nContent  : {self.content}"

    # Decorated Method
    @report_decorator
    def display(self):
        print(self)


# Main Program
Report.set_template("Student Performance Report")

title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

report = Report(title, content)
report.display()
