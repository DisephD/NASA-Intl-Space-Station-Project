# NASA ISS Project (In Progress)

This project tracks the real-time location of the International Space Station (ISS) and updates a map with its current position. In addition, it gathers detailed information on each astronaut currently aboard the ISS, including their age, nationality, and photos, by scraping data from the internet. This information is stored in a structured DataFrame, ready for future analysis and visualization. 

The repository is still in progress as I work on developing a dashboard to display the ISS's live position, astronaut details, and insights in a more interactive way.

## Table of Contents
1. [Project Status](#project-status)
2. [Goals of the Project](#goals-of-the-project)
3. [Data Collection and Processing](#data-collection-and-processing)
4. [Features (Planned)](#features-planned)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)
7. [Future Work](#future-work)
8. [Contact](#contact)

## Project Status
This project is currently **in progress**. While the core functionalities for tracking the ISS’s location and gathering astronaut data are complete, the final dashboard and real-time map updates are still under development. Updates to this repository will continue as the dashboard is built and additional features are implemented.

## Goals of the Project
The primary goals of this project are:
- **Track ISS Position in Real Time**: Obtain live data on the ISS's position and display it on an interactive map.
- **Gather Astronaut Information**: Scrape and display information on the astronauts currently on board, including age, nationality, and images, providing a personal view of the team aboard.
- **Create an Interactive Dashboard**: Develop a dashboard to present the ISS's position, astronaut details, and other visualized insights in an engaging format.

## Data Collection and Processing
1. **ISS Position Tracking**: Using a public API, the ISS's current latitude and longitude are collected and plotted on a map that will update in real-time.
2. **Astronaut Information**: For each astronaut currently on the ISS, data such as their name, age, nationality, and profile photo is scraped from Wikipedia. This data is then stored in a Pandas DataFrame for efficient processing and retrieval.
   
   - **Handling Disambiguation**: The scraping script identifies astronaut pages by verifying keywords like "astronaut," "cosmonaut," or "taikonaut" in their summaries, ensuring accurate data collection.
   - **Data Storage**: All collected data is saved in a structured DataFrame format, making it easy to manipulate and visualize in future steps.

## Features (Planned)
- **Real-Time Map of ISS Position**: An interactive map that updates to show the ISS's current location as it orbits the Earth.
- **Astronaut Profiles**: Display detailed profiles of each astronaut on board, including their image, age, and nationality.
- **Dynamic Data Updates**: Ensure that both the ISS position and astronaut data are refreshed periodically to maintain real-time accuracy.
- **Interactive Dashboard**: Once completed, the dashboard will provide a consolidated view of the ISS’s path and onboard crew details.

## Technologies Used
- **Python**: Core language for data collection, processing, and visualization.
- **Pandas**: Data manipulation and storage for astronaut details.
- **Geolocation API**: For obtaining real-time ISS location data.
- **Web Scraping (BeautifulSoup, Requests, wiki)**: To gather astronaut data from Wikipedia.
- **Folium **: For real-time map visualization.
- **Dash/Streamlit (Planned)**: To develop the interactive dashboard and integrate real-time updates.

## Project Structure
- **data/**: Stores raw and processed data, including the astronaut profiles in a structured format.
- **scripts/**: Python scripts used for scraping astronaut data, tracking ISS location, and saving results.
- **README.md**: Project documentation.

## Future Work
- **Dashboard Development**: Building an interactive dashboard to visualize the ISS’s position in real-time alongside astronaut data.
- **Improved Data Accuracy**: Enhancing the data scraping process to handle edge cases and ensure accurate astronaut information.
- **Historical Tracking**: Potentially adding a feature to track past ISS locations and astronaut rotations over time.
- **Data Refresh Automation**: Automate data updates so the dashboard remains accurate without manual intervention.

## Contact
Feel free to reach out if you have questions, suggestions, or would like to collaborate.
Send me an email at disephdum@gmail.com, use the repository title as the subject.
