
class String:

    @staticmethod
    def replaceUnacceptedString(in_string: str, in__replacementChar: str) -> str:
        wildcard = ['|', '\\', '/', ':', '*', '?', '"', '<', '>']
        if in__replacementChar in wildcard:
            in__replacementChar = '_'
        for char in wildcard:
            in_string = in_string.replace(char, in__replacementChar)

        return in_string