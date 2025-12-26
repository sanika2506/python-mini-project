# URL Finder Program - Using Only Basic Python Concepts

def get_user_input():
    """Get multi-line input from user."""
    print("\n" + "="*60)
    print("URL FINDER PROGRAM")
    print("="*60)
    print("Enter your text below (press Enter twice to finish):")
    print("-" * 60)
    
    lines = []
    empty_line_count = 0
    
    while True:
        try:
            line = input()
            
            # Check if line is empty
            if line == "":
                empty_line_count += 1
                # If we have two consecutive empty lines, stop
                if empty_line_count >= 2 and lines:
                    break
            else:
                empty_line_count = 0
                lines.append(line)
                
        except EOFError:
            # Handle Ctrl+D or Ctrl+Z
            break
    
    # Join all lines into a single string
    text = "\n".join(lines)
    return text

def is_valid_url_character(char):
    """Check if a character is valid in a URL."""
    # Valid URL characters (simplified)
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_chars += "0123456789"
    valid_chars += "-._~:/?#[]@!$&'()*+,;=%"
    
    return char in valid_chars

def find_urls_basic(text):
    """Find URLs in text using basic string operations only."""
    urls_found = []
    i = 0
    text_length = len(text)
    
    while i < text_length:
        # Look for "http://" or "https://"
        if (i + 7 < text_length and text[i:i+7] == "http://") or \
           (i + 8 < text_length and text[i:i+8] == "https://"):
            
            # Determine start position
            if text[i:i+7] == "http://":
                start = i
                i += 7
            else:
                start = i
                i += 8
            
            # Collect the URL characters
            url = text[start:i]
            
            # Keep adding valid URL characters
            while i < text_length and is_valid_url_character(text[i]):
                url += text[i]
                i += 1
            
            # Check if URL ends with punctuation that shouldn't be included
            while url and url[-1] in ".,;:!?)'\"":
                url = url[:-1]
                i -= 1
            
            if url:
                urls_found.append(url)
        
        # Look for "www."
        elif i + 4 < text_length and text[i:i+4] == "www.":
            start = i
            i += 4
            
            # Collect the URL characters
            url = text[start:i]
            
            # Keep adding valid URL characters
            while i < text_length and is_valid_url_character(text[i]):
                url += text[i]
                i += 1
            
            # Check if URL ends with punctuation that shouldn't be included
            while url and url[-1] in ".,;:!?)'\"":
                url = url[:-1]
                i -= 1
            
            if url:
                urls_found.append(url)
        else:
            i += 1
    
    return urls_found

def clean_urls(urls):
    """Remove duplicates and empty URLs."""
    cleaned = []
    seen = set()
    
    for url in urls:
        if url and url not in seen:
            # Make sure URL starts with http:// if it starts with www.
            if url.startswith("www.") and not url.startswith("http"):
                url = "http://" + url
            
            cleaned.append(url)
            seen.add(url)
    
    return cleaned

def display_urls(urls, original_text):
    """Display the found URLs."""
    print("\n" + "="*60)
    
    if not urls:
        print("RESULT: No URLs found in the text.")
        print("="*60)
        return
    
    print(f"RESULT: Found {len(urls)} URL(s)")
    print("="*60)
    
    # Show each URL with its position
    for index, url in enumerate(urls, 1):
        print(f"\nURL #{index}:")
        print(f"  {url}")
        
        # Find and show all occurrences of this URL in the text
        positions = []
        search_start = 0
        
        while True:
            pos = original_text.find(url, search_start)
            if pos == -1:
                break
            positions.append(pos)
            search_start = pos + 1
        
        if positions:
            print(f"  Found at position(s): {', '.join(str(p) for p in positions)}")
    
    print("\n" + "="*60)
    print("SUMMARY OF FOUND URLS:")
    print("-" * 60)
    
    for index, url in enumerate(urls, 1):
        # Extract domain from URL
        domain = url
        
        # Remove protocol
        if "://" in domain:
            domain = domain.split("://")[1]
        
        # Remove path after domain
        if "/" in domain:
            domain = domain.split("/")[0]
        
        print(f"{index}. {domain} -> Full URL: {url}")

def show_text_with_highlights(text, urls):
    """Show the original text with URLs highlighted."""
    if not urls:
        print("\nOriginal text (no URLs found):")
        print("-" * 60)
        print(text)
        return
    
    print("\n" + "="*60)
    print("ORIGINAL TEXT WITH URLS HIGHLIGHTED")
    print("="*60)
    
    # Create a list to mark which characters are part of URLs
    is_url_char = [False] * len(text)
    
    # Mark URL characters
    for url in urls:
        search_start = 0
        while True:
            pos = text.find(url, search_start)
            if pos == -1:
                break
            
            # Mark all characters in this URL
            for i in range(pos, pos + len(url)):
                if i < len(is_url_char):
                    is_url_char[i] = True
            
            search_start = pos + 1
    
    # Display text with highlights
    print("\n[URLs are shown in UPPERCASE for highlighting]")
    print("-" * 60)
    
    i = 0
    while i < len(text):
        if is_url_char[i]:
            # Start of a URL - collect and display in uppercase
            url_text = ""
            while i < len(text) and is_url_char[i]:
                url_text += text[i].upper()  # Convert to uppercase for highlighting
                i += 1
            print(url_text, end="")
        else:
            # Normal text
            print(text[i], end="")
            i += 1
    
    print("\n" + "-" * 60)

def save_to_file(urls, text, filename):
    """Save results to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("="*60 + "\n")
            file.write("URL FINDER RESULTS\n")
            file.write("="*60 + "\n\n")
            
            file.write(f"Total URLs found: {len(urls)}\n\n")
            
            if urls:
                file.write("URLS FOUND:\n")
                file.write("-" * 40 + "\n")
                for index, url in enumerate(urls, 1):
                    file.write(f"{index}. {url}\n")
                file.write("\n")
            
            file.write("ORIGINAL TEXT:\n")
            file.write("-" * 40 + "\n")
            file.write(text + "\n")
            
            if urls:
                file.write("\nURL LOCATIONS:\n")
                file.write("-" * 40 + "\n")
                for url in urls:
                    positions = []
                    search_start = 0
                    while True:
                        pos = text.find(url, search_start)
                        if pos == -1:
                            break
                        positions.append(str(pos))
                        search_start = pos + 1
                    
                    if positions:
                        file.write(f"{url}: positions {', '.join(positions)}\n")
        
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    """Main program function."""
    # Get input from user
    text = get_user_input()
    
    # Check if user entered anything
    if not text.strip():
        print("\n" + "!"*60)
        print("ERROR: No text was entered!")
        print("!"*60)
        return
    
    # Find URLs using basic string operations
    print("\n" + "-"*60)
    print("Searching for URLs...")
    raw_urls = find_urls_basic(text)
    
    # Clean the URLs (remove duplicates, add protocol if needed)
    urls = clean_urls(raw_urls)
    
    # Display results
    display_urls(urls, text)
    
    # Show text with highlights
    show_text_with_highlights(text, urls)
    
    # Ask if user wants to save results
    if urls:
        print("\n" + "="*60)
        save_option = input("Do you want to save these results to a file? (yes/no): ").strip().lower()
        
        if save_option in ['yes', 'y', 'ye']:
            filename = input("Enter filename (or press Enter for 'urls_found.txt'): ").strip()
            
            if not filename:
                filename = "urls_found.txt"
            
            # Make sure filename ends with .txt
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            if save_to_file(urls, text, filename):
                print(f"\n✓ Results successfully saved to '{filename}'")
            else:
                print("\n✗ Failed to save results to file.")
    
    # Show final message
    print("\n" + "="*60)
    print("PROGRAM COMPLETED")
    print("="*60)

# Run the program
if __name__ == "__main__":
    main()
