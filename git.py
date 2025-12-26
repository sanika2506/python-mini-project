import re

def simple_url_finder():
    """A simpler version of the URL finder."""
    print("Enter your text (type 'END' on a new line to finish):")
    
    # Collect multi-line input
    lines = []
    while True:
        line = input()
        if line.upper() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    if not text.strip():
        print("No input provided.")
        return
    
    # URL pattern
    pattern = r'(https?://\S+|www\.\S+)'
    
    # Find URLs
    urls = re.findall(pattern, text)
    
    # Display results
    if urls:
        print(f"\nFound {len(urls)} URL(s):")
        for i, url in enumerate(urls, 1):
            print(f"{i}. {url}")
    else:
        print("\nNo URLs found.")

# Run the simple version
simple_url_finder()
