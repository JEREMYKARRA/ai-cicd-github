from google import genai
import sys

client = genai.Client()

def code_review(code_diff):
    prompt = f"""You are a code reviewer. Review the following code diff and provide feedback.
    Focus on:
    - Security
    - Bugs
    - Performance issues
    - Good coding practice violations
    
    For each issue, highlight:
    - Severity i.e HIGH/MEDIUM/LOW
    - Description of the issue
    - Suggested fix
    
    If there is no problem with the code, just say so.
    
    Code to review: {code_diff}
    
    Provide in a structured and clear format.
    """
    
    response = client.models.generate_content(
        model= 'gemini-2.5-flash', contents=prompt
    )
    
    return response.text

if __name__=="__main__":
    if len(sys.argv)>1:
        diff_file = sys.argv[1]
        with open(diff_file, 'r') as file:
            diff_content = file.read()
    else:
        diff_content = sys.stdin.read()
    
    review = code_review(diff_content)
    print(review)