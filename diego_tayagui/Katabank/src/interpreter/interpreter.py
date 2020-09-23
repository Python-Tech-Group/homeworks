class Interpreter:

    def __init__(self):
        self.numbers = {
            "head": {
                " _ ": [0, 2, 3, 5, 6, 7, 8, 9],
                "   ": [1, 4]
            },
            "body": {
                "| |": [0],
                "|_ ": [5, 6],
                " _|": [2, 3],
                "|_|": [4, 8, 9],
                "  |": [1, 7],
            },
            "footer": {
                "|_|": [0, 6, 8],
                "  |": [1, 4, 7],
                "|_ ": [2],
                " _|": [3, 5, 9],
            }
        }

    def check_concurrences(self, number):
        # Return the numbers can apply with the patterns head, body and footer
        lines = number.splitlines()
        head = self.numbers['head'].get(lines[0], [])
        body = self.numbers["body"].get(lines[1], [])
        footer = self.numbers["footer"].get(lines[2], [])
        return {
            'head': head,
            'body': body,
            'footer': footer
        }

    def read_number(self, number):
        # Return the first number that matches with the 3 patterns
        pattern = self.check_concurrences(number)
        result = [number for number in pattern['head'] if number in pattern['body'] and number in pattern['footer']]
        if result:
            return str(result[0])
        else:
            return ""
