import streamlit as st
import requests
import json


st.header('Home Remedies for :blue[diseases] :relieved:', divider='rainbow')
# st.header('_Streamlit_ is :blue[cool] :sunglasses:')

disease_map = {'Digestive System': ("Indigestion(Dyspepsia)", "Anorexia(Loss of appetite)", "Flatulence(Gas)", "Heart Burn", "Nausea & Vomiting",
         "Constipation", "Diarrhoea"),
                'Blood Circulation System': ("Bleeding nose", "Hypertension", "Anaemia", "Sunstroke",
                                             "Cholesterolemia"),
               'Respiratory System': ('Common cold', 'Pharyngitis', 'Influenza', 'Asthma')


               }

sidebar = st.sidebar

sidebar.subheader('Choose which part of your body is not happy :unamused:')

# Add a selectbox to the sidebar:
disease_type = sidebar.selectbox(
    '',
    ('Digestive System', 'Blood Circulation System', 'Respiratory System')
)


st.image("images/systems.jpeg")

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.subheader('Choose your disease 	:point_right:')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    disease_name = st.radio(
        '',
        disease_map.get(disease_type))
    st.write(f"You are having {disease_name}!")


find = st.button('Find Details')
result = None

if find:
    data = json.dumps({"disease_name": disease_name.lower(), "disease_type": disease_type})
    try:
        print('requesting with data'+data)
        result = requests.get("http://3.111.38.153:5000/query", data=data)
    except Exception as e:
        print(e)


if result:
    result = result.json()
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Causes", "Symptoms", "Remedies", "Harmful foods", "Beneficiary foods"])

    with tab1:
        st.header("Causes")
        left_column, right_column = st.columns(2)
        right_column.image("images/unhealthy.jpeg", width=400)
        left_column.write(result.get("causes"))

    with tab2:
        st.header("Symptoms")
        left_column, right_column = st.columns(2)

        right_column.image("images/symptoms.png", width=400)
        left_column.write(result.get("symptoms"))

    with tab3:
        st.header("Remedies")
        left_column, right_column = st.columns(2)

        right_column.image("images/remedies.jpeg", width=400)
        left_column.write(result.get("remedies"))

    with tab4:
        st.header("Harmful Foods")
        left_column, right_column = st.columns(2)

        right_column.image("images/lifestyle.jpeg", width=400)
        left_column.write(result.get("harmful_foods"))

    with tab5:
        st.header("Beneficiary Foods")
        left_column, right_column = st.columns(2)

        right_column.image("images/healthy.jpeg", width=400)
        left_column.write(result.get("beneficial_foods"))