# U_CAN: Ukraine towards Carbon Neutrality — Interactive Presentation

A single-page, data-driven slide deck on reducing urban traffic emissions with adaptive clustering and AI-driven signal control. Designed for 1280×720 displays with accessible, keyboard-first navigation.

## Live Slides

- GitHub Pages (primary)
  https://radiukpavlo.github.io/u-can-carbon-neutrality/

- RawGitHack (mirror)
  https://raw.githack.com/radiukpavlo/u-can-carbon-neutrality/refs/heads/main/index.html

- HTMLPreview (fallback)
  https://htmlpreview.github.io/?https://github.com/radiukpavlo/u-can-carbon-neutrality/refs/heads/main/index.html

If a link shows 404 immediately after an update, wait a minute for caching to complete and refresh.

## Usage

- Next slide: Space / Right / Down
- Previous slide: Left / Up
- Jump to start/end: Home / End
- Overview: O (opens slide index)
- A slide counter and clickable progress bar support pacing and Q&A

## View Locally

- Open `index.html` directly in a browser, or
- Serve the folder with any static HTTP server for consistent asset loading

## Publish to GitHub Pages

1) Go to Repository Settings → Pages  
2) Build and deployment → Source: “Deploy from a branch”  
3) Branch: `main`, Folder: `/ (root)` → Save  
4) After deployment completes, access:  
   https://radiukpavlo.github.io/u-can-carbon-neutrality/

## Troubleshooting

- Blank page or missing assets: hard refresh (Ctrl/Cmd+Shift+R)
- 404 on GitHub Pages: ensure Pages is enabled for `main` and `index.html` is at the repository root
- Slow loads: try the RawGitHack mirror above
- **Selenium PDF error ("DevToolsActivePort file doesn't exist"):**  
  If you run the PDF generator as root (e.g., in some Docker or CI environments), Chrome may fail to start unless you add the `--no-sandbox` flag.  
  **Solution:** In `generate_pdf.py`, add `chrome_options.add_argument("--no-sandbox")` before launching Chrome.

## At a Glance

- Problem context and motivation
- Adaptive cascade clustering for mobility data
- DRL-based traffic signal control
- Experimental setup and realistic scenarios
- Results and roadmap for pilot deployment

Feedback and collaboration are welcome.