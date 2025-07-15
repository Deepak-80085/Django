# Wiki Project

A Wikipedia-like online encyclopedia built with Django as part of the CS50 Web Programming with Python and JavaScript course.

## Overview

This project is a simple encyclopedia that allows users to:

- View available encyclopedia entries
- Search for entries
- Create new entries using Markdown syntax
- Edit existing entries
- Navigate to a random entry
## Features

### Entry Page

- Visiting `/wiki/TITLE` displays the contents of the encyclopedia entry
- If an entry doesn't exist, an error page is shown
- Markdown content is converted to HTML before being displayed

### Index Page

- Lists all available encyclopedia entries
- Each entry title is a clickable link to the corresponding entry page

### Search

- Allows users to search for encyclopedia entries
- If the query matches a title exactly, redirects to that entry page
- Otherwise, displays a search results page with entries that contain the query

### New Page

- Users can create a new encyclopedia entry
- Validates that the entry title doesn't already exist
- Takes both a title and Markdown content for the entry

### Edit Page

- Users can edit the content of an existing encyclopedia entry
- Pre-fills the textarea with the existing Markdown content

### Random Page

- Clicking "Random Page" takes users to a random encyclopedia entry

