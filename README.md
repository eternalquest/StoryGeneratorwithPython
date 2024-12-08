# **StoryGenerator**

This script reads a text file (`story.txt`) and identifies placeholders wrapped in `<` and `>`. It prompts the user to input custom words to replace these placeholders, generating a personalized story.

## **Features**

- Reads a text file containing a story.
- Detects placeholders wrapped in `<` and `>` (e.g., `<name>`).
- Prompts the user to input replacements for each placeholder.
- Outputs the modified story with the user-provided words.

## **Usage**

1. **Create a `story.txt` file** in the same directory as the script. The file should contain a story with placeholders wrapped in `<` and `>`.  
   Example:
   ```
   Once upon a time, there was a <character> who lived in a <place>.
   ```

2. **Run the script**:
   ```bash
   python storyGenerator.py
   ```

3. **Enter inputs when prompted**:
   ```
   enter a word for <character>: hero
   enter a word for <place>: castle
   ```

4. **View the customized story** printed in the console.

   Example Output:
   ```
   Once upon a time, there was a hero who lived in a castle.
   ```

## **File Structure**

```
project/
│
├── storyGenerator.py     # The main Python script
├── story.txt             # Text file containing the story
```

## **Script Logic**

1. **Read the Story File**: 
   - Opens and reads `story.txt`.

2. **Identify Placeholders**: 
   - Searches for text enclosed in `<` and `>`.
   - Stores these placeholders in a `set` to ensure unique entries.

3. **Collect User Input**:
   - Prompts the user for a replacement word for each placeholder.

4. **Replace Placeholders**:
   - Replaces the placeholders in the story with user-provided inputs.

5. **Display the Final Story**:
   - Prints the modified story with the user's custom words.

## **Requirements**

- Python 3.x

## **Example Use Case**

This script is ideal for creating personalized stories, Mad Libs, or simple text-based games. Users can modify the `story.txt` file to create new customizable experiences.
---
