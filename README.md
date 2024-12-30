# Exporting to HTML WASM with customization

Start with either

`marimo export html-wasm notebook.py --mode edit -o docs/`

or

`marimo export html-wasm notebook.py --mode run --no-show-code -o docs/`

to generate a static export. The first command includes editable cells (useful
for the scratchpad), the second command generates a readonly page (useful for
the learn section).

The `docs/assets` folder includes CSS files that you can edit. In this example,
which is a `--mode edit` export, the file is
`docs/assets/edit-page-C05ExoCW.css`. I've modified this file to hide the
sidebar and save button, just as an example.
