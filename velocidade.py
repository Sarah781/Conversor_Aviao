import streamlit as st

st.title("Conversor de Altitude e Velocidade de um :red[Avião]")


st.write("## Conversão de Altitude")
pes = st.number_input("Digite o valor em pés (ft): ", value=0)
metros = pes * 0.3048
km = pes * 0.0003048
st.write(f"Um avião a :blue[{pes:.1f}] ft está voando a ≈ :green[{km:.2f}] km de altitude.")

st.write("## Conversão de Velocidade")
nos = st.number_input("Digite a velocidade em nós (kts):", value=0)
kmh = nos * 1.852
st.write(f"Se ele tem :blue[{nos:.1f}] kts de velocidade, ele está a ≈ :green[{kmh:.1f}] km/h.")



# # Conversão de altitude (pés → metros e km)
# pes = float(input("Digite o valor em pés (ft): "))
# metros = pes * 0.3048
# km = pes * 0.0003048

# # Conversão de velocidade (nós → km/h)
# nos = float(input("Digite a velocidade em nós (kts): "))
# kmh = nos * 1.852

# # Exibir resultados formatados
# print(f"\nUm avião a {pes:.1f} ft está voando a ≈ {km:.2f} km de altitude.")
# print(f"Se ele tem {nos:.1f} kts de velocidade, ele está a ≈ {kmh:.1f} km/h.")
