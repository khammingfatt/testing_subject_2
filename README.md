# Navigating the HDB Resale Market: A Data-Driven Approach to Valuations Hello this Project is awesome!!!!

## The Challenge: A Complex Housing Landscape
For most Singaporeans, purchasing a Housing & Development Board (HDB) resale flat is one of the most significant financial decisions of their lives. However, the resale market is complex and highly dynamic. Prices are influenced by a myriad of factors—ranging from the remaining lease and floor area to the proximity to MRT stations, shopping malls, and hawker centers. 

For buyers, overpaying is a constant fear. For sellers, pricing a property too low leaves money on the table, while pricing it too high means it might sit on the market for months. 

**How can we empower consumers to make confident, data-backed property decisions?**

## The Solution: Demystifying Prices with Machine Learning
This project addresses the uncertainty in the housing market by leveraging historical transaction data to build an intelligent **HDB Resale Price Predictor**. 

By training a robust Random Forest machine learning model on past transactions, the application acts as an impartial, data-driven appraiser. It identifies hidden patterns in the data that a human might miss—quantifying exactly how much value an extra 500 meters closer to an MRT station adds, or how much a high-floor premium actually costs across different planning areas.

## Business Value & Consumer Impact
This tool is designed with the everyday consumer in mind, delivering immediate, actionable value:
1. **Empowered Negotiation:** Buyers can enter negotiations armed with a realistic, algorithmically generated baseline price, preventing them from severely overpaying for a unit in a heated market.
2. **Optimized Selling Strategy:** Sellers can benchmark their asking price against the model's estimate to ensure their listing is competitive yet profitable.
3. **Informed Financial Planning:** Prospective homeowners can estimate the costs of their desired flat configurations *before* they start house-hunting, allowing for accurate budgeting and mortgage planning.
4. **Time Savings:** Instead of manually cross-referencing past transactions on the HDB portal, users get an instant, highly customized valuation tailored to the specific attributes of their target property.

## How It Works: The Data Behind the Predictor
Our model evaluates a property holistically. When a user inputs the details of a flat, the model analyzes key drivers of value:
*   **Space & Age:** Floor Area (sqft) and the HDB's Age (reflecting the impact of the remaining lease).
*   **Convenience & Accessibility:** Distance to the nearest MRT station, and the density of Malls and Hawker Centers within a 2km radius.
*   **Location & Exclusivity:** The Planning Area (e.g., Bishan vs. Woodlands) and the specific Flat Type/Model.
*   **Micro-Features:** The floor level (Mid Storey), and the presence of immediate amenities like Commercial Units, Multistorey Carparks, and Precinct Pavilions within the block.

## Project Structure & Deliverables
*   **`app.py`**: The interactive Streamlit web application where consumers can interact with the model seamlessly.
*   **`Project 3 - Visualisations v4.twbx`**: A Tableau dashboard providing deep-dive visual analytics into the trends driving the HDB market.
*   **`random_forest_model.joblib`**: The engine behind the application—our pre-trained predictive model.
*   **`Project3-AnyDebs-Refactored.ipynb`**: The technical blueprint detailing data cleaning, feature engineering, and model training.
*   **`HDB_30Slides_V4_FINAL_V3(LOCKED).pdf`**: The executive presentation summarizing our findings, methodology, and recommendations.

## Try It Out
To experience the predictor yourself:
1. Ensure you have the necessary libraries installed: 
   ```bash
   pip install streamlit pandas numpy joblib
   ```
2. Run the application from your terminal: 
   ```bash
   streamlit run app.py
   ```

---
*Developed by Any Debs*
