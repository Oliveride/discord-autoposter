# 🤖 Discord Auto-Poster

A lightweight, automated Python script designed to regularly post advertising, announcements, or recruitment messages to specific Discord channels. Perfect for streamlining workflow, managing community boards, and removing the hassle of manual posting.

## 🚀 Features

*   **Fully Automated Posting:** Automatically sends your custom message template to the target channel at set intervals.
*   **Flexible Delay System:** Easily switch between minutes and seconds for intervals using a boolean flag (`DELAY_IN_SECONDS`).
*   **Anti-Spam Randomization:** Set custom minimum and maximum delay ranges to keep the posting intervals dynamic and natural.
*   **Ready for Scalability:** Tracks the `last_message_id` for potential future updates (e.g., auto-deleting the previous post before sending a new one).

## 🛠 Setup & Installation

### 1. Requirements
Make sure you have Python 3.x installed along with the `requests` library[cite: 2]. If you don't have it, install it via your terminal:

```bash
pip install requests
