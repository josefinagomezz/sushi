import streamlit as st
from PIL import Image

st.set_page_config(page_title="SushiFit", page_icon=":sushi:", layout="wide")

menu = st.sidebar.radio("Navegación", ["Inicio", "Calculadora", "Contacto"])

if menu == "Inicio":
    st.title("Bienvenido a SushiFit")
    st.image("sushi imagen.png", use_container_width=True)

    st.subheader("Problema a resolver:")
    st.write("""
    Muchas personas disfrutan comer sushi, pero desconocen cuántas piezas pueden consumir sin exceder su ingesta calórica diaria.
    """)

    st.subheader("Usuario objetivo:")
    st.write("""
    - Edad: 12 a 45 años  
    - Ubicación: Zonas urbanas  
    - Estilo de vida: Personas que cuidan su alimentación pero disfrutan del sushi
    """)

    st.subheader("Cómo ayuda la aplicación:")
    st.write("""
    **SushiFit** te permite calcular cuántas piezas de sushi puedes comer según tus calorías diarias disponibles.
    También te muestra cuántas calorías consume cada tipo de sushi y recomendaciones saludables.
    """)

    st.video("https://www.youtube.com/watch?v=zlnvJJuIhPI")
    st.audio("cooking-food-music-247352.mp3")
    
elif menu == "Calculadora":
    st.title("Calculadora de SushiFit")
    st.image("calculadora.png", use_container_width=True)

    st.subheader("Ingrese su información:")
    calorias_disponibles = st.number_input("Calorías disponibles para la comida:", min_value=50, max_value=5000, step=1)
    cuantas_piezas_de_sushi = st.number_input("Cuantas piezas de sushi he comido?:", min_value=1, max_value=100, step=1)
    tipo_sushi = st.selectbox("Seleccione el tipo de sushi:", 
                              ["Nigiri", "arroz", "Salmon", "queso crema", "verduras", "pollo"])

    calorias_sushi = {
        "Nigiri": 70,
        "arroz": 100,
        "Salmon": 90,
        "queso crema": 120,
        "verduras": 30,
        "pollo": 100
    }

    if calorias_disponibles > 0:
        calorias_por_pieza = calorias_sushi[tipo_sushi]
        piezas_posibles = calorias_disponibles // calorias_por_pieza

        st.success("Puedes comer aproximadamente **5 piezas de sushi hasta 30 piezas de sushi**.")
        st.info("Cada pieza de sushi contiene aproximadamente 50 calorias.**")

        st.markdown("### Recomendaciones:")
        if piezas_posibles > 15:
            st.warning("Estás comiendo bastante sushi ¡Considera acompañar con ensalada o té verde!")
        elif piezas_posibles < 5:
            st.info("Podrías disfrutar algunas piezas más sin preocuparte demasiado ")
        else:
            st.success("Cantidad equilibrada. ¡Buen provecho! ")
            
elif menu == "Contacto":
    st.title("Contacto")
    st.image("2.png", width=300)

    st.write("""
    ### Equipo de desarrollo SushiFit:
    - **CEO:** [ANTONIA Y RENATA]  
    - **Product Manager:** [ANTONIA]  
    - **Developer:** [RENATA]  
 
    Email: sushi.fit.app@gmail.com  
    """)

    st.image("sushi imagen 2.jpg")
    st.video("https://www.youtube.com/watch?v=NTFjleENYEo")    
