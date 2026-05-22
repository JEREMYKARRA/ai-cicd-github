import ast
from google import genai
import sys
import os

def extract_functions(file):
    
    functions = []
    
    with open(file, "r") as f:
        source = f.read()
        tree = ast.parse(source)
        
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                args = [arg.arg for arg in node.args.args]
                docstring = ast.get_docstring(node) or ""
                source_code = ast.get_source_segment(source, node)
                
                functions.append({
                    "name": func_name,
                    "args": args,
                    "docstring": docstring,
                    "source": source_code
                })
        
        
    return functions

def generate_tests_for_functions(func_info):
    
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    prompt = f"""Generate pytest tests for this Python function.
    
    Function name: {func_info['name']}
    Arguments: {', '.join(func_info['args'])}
    Docstring:{func_info['docstring']}
    
    Source code:
    
    {func_info['source']}
    
    Requirements:
    1. Generate 3-5 meaningful cases.
    2. Do not generate testcases like `assert True`.
    3. Be verbose in the tests generated.
    4. Include edge cases(empty inputs, None values, etc)
    5. Include assertions that actually test behaviour.
    """
    
    response = client.models.generate_content(
        model = 'gemini-2.5-flash', contents=prompt
    )
    
    return response.text

def main():
    changed_files = sys.argv[1:] if len(sys.argv)>1 else []
    
    if not changed_files:
        print("No Python files provided for test generation.")
        return

    all_tests = []
    
    for file_path in changed_files:
        if not file_path.endswith('.py'):
            continue
        if file_path.startswith('tests/'):
            continue
        
        if not os.path.exists(file_path):
            continue
        
        print(f"Analysing: {file_path}")
        
        functions = extract_functions(file_path)
        
        for function in functions:
            if function['name'].startswith('_'):
                continue
            
            response = generate_tests_for_functions(function)
            all_tests.append(response)
    
    os.makedirs('tests', exist_ok=True)
    with open('tests/test_generated.py',"w") as file:
        if len(all_tests) > 0:
            file.write("import pytest\n\n")
        file.write("\n\n".join(all_tests))
        
if __name__=="__main__":
    main()