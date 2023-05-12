# Pipe and Filter Style

- **Status:** Implemented.
- **Context:** Creating a command line interface (CLI) tool for developers to assist in generating Architectural Decision Records.
- **Decision:** Use a pipe-and-filter style architecture
  - **Filters:** There are two types of filters in our architecture: implemented filters, and user filters.
    - **Pre-processing Filters:** "Pre-processing" filters refers to the user selection before activating the GUI. These are filters in the form of if-statements that are run to check whether the user has entered parameters, like the "*-h*" parameter for help with the program, or the "*-s*" parameter to specify the architecture style.
    - **User Filters:** The "user filters" refers to the program and its options itself. The first window (or first parameter) selects the template data, and the second window filters the parameters and their associated notes.
  - **Pipes:** The "pipes" are simply function parameters in this case.
- **Rationale:** This program itself, in some regards, is a pipe-and-filter program: our program is the filter, and the data flowing through it are the basic templates (found in `/adr-templates/`).
- **Consequences:** Selecting functions as filters can lead to bloat. An object-oriented approach 