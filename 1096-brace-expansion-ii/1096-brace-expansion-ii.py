class Solution:
    def braceExpansionII(self, expression: str):
        def merge(a, b):
            return {x + y for x in a for y in b}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)
                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue
                else:
                    part = {expression[i]}
                    i += 1

                current = merge(current, part)

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        ans, _ = parse(0)
        return sorted(ans)