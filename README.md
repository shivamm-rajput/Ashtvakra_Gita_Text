While developing the Ashtavakra Gita verse extractor, I encountered some small issues that would impact the outcome. Here is how I resolved them:

1. Verse Structure (2 Lines + Verse Number)

In the text, a verse is terminated with something like: // Avg_1.5. I observed that prior to this, there are two lines of verse text.

What I did:
I created a pattern that only catches two lines plus the verse number format. This ensures that I only gather complete and correct verses.

2. Additional Text in the File

The file contains some additional lines such as headers, notes, or blank lines which are not verses.

What I did:
I skipped everything that does not fit the verse format. Only lines that end with // Avg_1.5 (or the like) are caught.

3. Sanskrit Letters

The lines have special characters such as ś, ā, and ī. These may be broken if encoding is incorrect.

What I did:
I employed UTF-8 encoding when saving the JSON, and also didn't force English-only characters. This preserves the Sanskrit characters.
