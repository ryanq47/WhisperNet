
## Directly from ChatGPT for best practices

1. **PascalCase**: This is used for class names, method names, and property names. The first letter of each word is capitalized, and there are no underscores between words.
    
    - Class names: `public class MyClass`
    - Method names: `public void CalculateTotal()`
    - Property names: `public int Age { get; set; }` <br><br>
2. **camelCase**: This is used for variable names and method parameters. The first letter of the first word is lowercase, and the first letter of subsequent words is capitalized.
    
    - Variable names: `int itemCount;`
    - Method parameters: `public void UpdateCustomer(string name)`<br><br>
3. **PascalCase (for Acronyms)**: If an identifier contains an acronym or an initialism, it should be written in PascalCase.
    
    - Correct: `XmlDocument doc;` (not `XMLDocument doc;`)<br><br>
4. **UPPER_CASE**: This is used for constants. All letters are in uppercase, and words are separated by underscores.
    
    - Constants: `const int MAX_RETRY_ATTEMPTS = 3;`<br><br>
5. **_underscorePrefix**: This convention is used for private fields. The underscore is followed by camelCase.
    
    - Private fields: `private int _counter;`<br><br>
6. **I**-prefix (for Interfaces): Interfaces start with the letter "I", followed by PascalCase.
    
    - Interface name: `public interface ILogger`<br><br>