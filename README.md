# ✈FlightFinder

FlightFinder is a powerful tool that helps you find the cheapest flights by scraping Google Flights and analyzing routes across multiple days and layovers.

---

## 📖 What I Learned

While building **FlightFinder**, I learned:

- How to scrape websites to build a structured flight database
- How to use Selenium and ChromeDriver to interact with dynamic websites
- How to sort and format large datasets for clean and useful output
- How to handle and manipulate date ranges for multi-day itineraries
- How to detect and wait for complete website loading before data extraction
- How to use html language in a python program

---

## ⚙️ How to Use

1. Enter the airports or cities involved in your overall itinerary
2. Choose a range of travel dates
3. Provide a list of potential layover airports *(automatic suggestion coming soon)*
4. Set your maximum total trip budget

FlightFinder will then search for the cheapest combination of flights, including separate tickets if needed.

---

## ❓ Why Use FlightFinder Over a Traditional Comparator?

When booking via traditional methods:
- Escales (layovers) are arranged by airlines, who ensure your full connection
- This adds to cost (baggage handling, interline agents, etc.)
- Airline prices also increase due to demand (like during national holidays)

**FlightFinder bypasses this:**
- It looks for separate tickets, which avoids the airline-imposed fees
- It can route you through countries not on holiday, avoiding demand-based price hikes
- It uses Google Flights who aggregates offers from travel agencies and airlines directly.

### 🔹 Real Example (July 8)
- Without FlightFinder: Paris ➔ Amman = €400 (Austrian Airlines, 1 layover)
- With FlightFinder: Paris ➔ Amman = €224 (3 different airlines, 2 layovers)

---

## 📁 Installation

1. Go to the [Releases](https://github.com/mingolino/FlightFinder/releases) tab and download **FlightFinder.exe**
2. Download the latest **ChromeDriver** from [here](https://googlechromelabs.github.io/chrome-for-testing/)
3. Run `chromedriver.exe`
4. Run `FlightFinder.exe`

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.

You are free to:
- Share — copy and redistribute the material in any medium or format

Under the following terms:
- **Attribution** — You must give appropriate credit.
- **NonCommercial** — You may not use the material for commercial purposes.
- **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material.

Read the full license text in the [LICENSE](https://github.com/mingolino/FlightFinder/blob/main/LICENSE) file.

