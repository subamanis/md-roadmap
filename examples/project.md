# Notes app roadmap

> Each step is one line with its state. Plans live next to this file.

## 1. Main line

- [x] **Step 1 [#step:1]: Storage**
  - [x] **1a Schema:** notes, tags and a join table in SQLite.
  - [x] **1b Migrations:** numbered SQL files, applied at start.
  - **[#note:1]** Every write is one transaction per note, so a crash leaves no half-saved note.
- [x] **Step 2 [#step:2]: Editor**
  - [x] **2a Markdown input** with a live preview.
  - [x] **2b Autosave** one second after the last key.
  - [ ] **[#task:2>3] Pasted images:** stored next to the note, then sent by sync.
    - [ ] Scale down anything wider than 2000 px.
    - [ ] Keep the original file name.
- [x] **[#before:3] Keyboard pass:** every button reachable with Tab, every dialog closed with Esc.
- [~] **Step 3 [#step:3]: Sync**
  - [x] **3a Change log** of every edit, with a timestamp.
  - [~] **3b Server** that merges the change logs of two devices.
    - [x] Merge of edits to different notes.
    - [ ] Merge of edits to the same note.
  - [ ] **3c Conflict view** for a note edited on both sides.
  - **[#note:3]** First sync of 10,000 notes takes 1.8 s on Wi-Fi.
- [ ] **Step 4 [#step:4]: Release**
  - [ ] **4a Installers** for Windows, macOS and Linux.
  - [ ] **4b Website** with a download page.

## 2. Backlog

- [ ] **[#task:3] Retry with backoff:** a failed sync retries after 1, 2, 4 and 8 seconds.
- [ ] **[#after:4] Plugin API:** read access to notes for user scripts.
- [ ] Dark theme for the website.

## 3. Later [#after:4]

- [ ] **Mobile app:** the same storage on Android and iOS.
- [ ] **Shared notebooks:** one notebook that several people edit.
  - [ ] Invites by link.
  - [ ] A role per person: read or write.
