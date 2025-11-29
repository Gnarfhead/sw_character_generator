"""Functions to manage magic skills tab based on character class."""

def manage_magic_tab(character, app):
    """Evaluate if the character is a magic class and enable/disable magic tab."""
    print("DEBUG manage_magic_tab: ----------------------------------------------------------------")

    if character is None:
        raise ValueError("ERROR manage_magic_tab: No character provided for magic class evaluation.")

    # Enable or disable magic_frame based on magic user status
    if character.magic_user_class is False:
        print("DEBUG manage_magic_tab: Disabling magic skills tab for non-magic user.")
        print("DEBUG manage_magic_tab: Magic user status is", character.magic_user_class)
        app.lower_notebook.tab(app.magic_frame, state="disabled")
    else:
        print("DEBUG manage_magic_tab: Enabling magic skills tab for magic user.")
        print("DEBUG manage_magic_tab: Magic user status is", character.magic_user_class)
        app.lower_notebook.tab(app.magic_frame, state="normal")