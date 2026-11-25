# main.py - Entry point for the grader
# Entry validated: output is 1-200 chars, one funny line, deterministic.
# Writes a funny line to the specified output file and validates constraints.

import os

# Define the exact required line as a Python string constant
LINE = "Twelve senior directors spent an hour watching the project manager slowly hunt and peck his password into a locked PDF nobody asked for.\n"

def main():
    # Get output directory from environment or default to 'out'
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    
    # Create the output directory if it does not exist
    os.makedirs(out_dir, exist_ok=True)
    
    # Construct the full path to entry.txt
    out_path = os.path.join(out_dir, "entry.txt")
    
    # Content to be written
    content = LINE
    
    # Validate content according to the exact rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content failed validation constraints.")
        
    # Write the content to the file using UTF-8 encoding
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Print the output path and the character count
    print(out_path)
    print(len(content))

if __name__ == "__main__":
    main()
