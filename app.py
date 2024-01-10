# Import library
import streamlit as st
import pandas as pd
import database
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def read_data():
    dataset = database.results
    table = pd.DataFrame(dataset)
    st.write('Dataset Penjualan :')
    st.write(table)
    periode = table


    # st.subheader("Upload Dataset")
    # uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # if uploaded_file is not None:
    #     data = pd.read_csv(uploaded_file)
    #     st.dataframe(data.head())
    #     return data
    
def apply_apriori(data, min_support):

    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    st.subheader("Frequent Itemsets")
    st.dataframe(frequent_itemsets)

    st.subheader("Association Rules")
    st.dataframe(rules)


# Main function
def main():
    st.title("Sistem Asosiasi Pola Pembelian")
    data = read_data()

    if data is not None:
        min_support = st.slider("Minimum Support", min_value=0.01, max_value=1.0, step=0.01, value=0.1)
        st.write("Selected Minimum Support:", min_support)
        
        if st.button("Run Apriori"):
            apply_apriori(data, min_support)

# Run the app
if __name__ == "__main__":
    main()
