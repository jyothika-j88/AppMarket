# query_interface.py
import json
import os

INSIGHTS_FILE = os.path.join("data", "insights.json")

with open(INSIGHTS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

insights_list = data.get("insights", [])

def find_insights_by_category(query_category):
    results = []
    query_category = query_category.lower()
    for ins in insights_list:
        cat = ins.get("category", "").lower()
        subcat = ins.get("subcategory", "").lower()
        text = ins.get("insight_text", "").lower()
        if query_category in cat or query_category in subcat or query_category in text:
            results.append(ins)
    return results

def run_query_interface():
    print("=== Intelligent Query System ===")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Enter your query: ").strip().lower()
        if query == "exit":
            print("Exiting query interface.")
            break
        
        if "success factor" in query:
            category = input("Enter keyword (e.g., installs, reviews, rating): ").strip()
            results = find_insights_by_category(category)
            if results:
                print(f"\nSuccess factors related to '{category}':")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r['insight_text']}")
                    for rec in r.get("recommendations", []):
                        print(f"   Recommendation: {rec}")
            else:
                print("No matching success factors found.")
        
        elif "pricing" in query:
            category = input("Enter keyword (e.g., ART_AND_DESIGN, AUTO_AND_VEHICLES): ").strip()
            results = find_insights_by_category(category)
            if results:
                print(f"\nPricing insights for '{category}':")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r['insight_text']}")
                    for rec in r.get("recommendations", []):
                        print(f"   Recommendation: {rec}")
            else:
                print("No matching pricing insights found.")
        
        elif "revenue" in query:
            results = find_insights_by_category("revenue")
            if results:
                print("\nRevenue-related insights:")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r['insight_text']}")
            else:
                print("No revenue insights found.")
        
        elif "launch strategy" in query:
            results = find_insights_by_category("opportunity")
            if results:
                print("\nLaunch strategy insights:")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r['insight_text']}")
                    for rec in r.get("recommendations", []):
                        print(f"   Recommendation: {rec}")
            else:
                print("No launch strategy insights found.")
        
        else:
            print("Sorry, I didn't understand that query. Try another one.")

if __name__ == "__main__":
    run_query_interface()