import streamlit as st


def calculate_lot_sizes(stop_loss_pips, risk_percent):
    capitals = [5000, 15000, 25000, 50000, 100000]
    lot_sizes = []

    for capital in capitals:
        # Calcul du montant du risque
        risk_amount = (risk_percent / 100) * capital
        # Calcul du lot size en utilisant la formule correcte
        lot_size = risk_amount / (stop_loss_pips * 10)
        lot_sizes.append((capital, lot_size))

    return lot_sizes


# CSS personnalisé pour l'interface
st.markdown("""
    <style>
        body {
            background-color: #2c2f36;
            color: #f1f1f1;
        }
        .css-1d391kg {
            color: #f1f1f1;
        }
        .css-18e3th9 {
            color: #FF6347;
        }
        .css-1v3fvcr {
            background-color: #FF6347;
            color: white;
        }
        .stTextInput input {
            background-color: #1c1c1c;
            color: #f1f1f1;
            border: 1px solid #444;
        }
        .stButton>button {
            background-color: #FF6347;
            color: white;
            border-radius: 10px;
        }
        .stTextArea>div>textarea {
            background-color: #1c1c1c;
            color: #f1f1f1;
            border: 1px solid #444;
        }
        .stMarkdown {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("🎯 **Calculateur de Lot Size**")

# Entrée pour le Stop Loss (pips)
stop_loss_pips = st.number_input("⛔ Stop Loss (pips):", min_value=1.0, value=10.0, step=1.0)

# Entrée pour le Risque (%)
risk_percent = st.number_input("💰 Risque (%):", min_value=0.1, value=1.0, step=0.1)

# Bouton pour calculer
if st.button("💡 Calculer", key="calculate"):
    lot_sizes = calculate_lot_sizes(stop_loss_pips, risk_percent)

    # Affichage des résultats
    st.markdown("### **Résultats Calculés** :")
    for capital, lot_size in lot_sizes:
        st.write(f"**Capital** : ${capital} | **Lot Size** : {lot_size:.2f}")
