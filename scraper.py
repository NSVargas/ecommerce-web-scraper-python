import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# ==========================================
# CONFIGURACIÓN
# ==========================================
BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
DATA_EXPORT_FILE = 'libros_extraidos.csv'

def obtener_datos_pagina(numero_pagina):
    """
    Función que descarga y parsea una página específica.
    """
    url = BASE_URL.format(numero_pagina)
    print(f"🔄 Scrapeando página: {numero_pagina}...")
    
    try:
        # Simulamos un User-Agent real para evitar bloqueos básicos
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            libros = soup.find_all('article', class_='product_pod')
            
            datos_libros = []
            
            for libro in libros:
                # Extracción de datos con manejo de errores por si falta algún campo
                try:
                    titulo = libro.h3.a['title']
                    precio = libro.find('p', class_='price_color').text
                    # Limpieza básica de datos (quitar símbolo de moneda)
                    precio_limpio = float(precio.replace('£', '').replace('Â', ''))
                    disponibilidad = libro.find('p', class_='instock availability').text.strip()
                    rating = libro.find('p', class_='star-rating')['class'][1]
                    
                    datos_libros.append({
                        'Titulo': titulo,
                        'Precio (£)': precio_limpio,
                        'Disponibilidad': disponibilidad,
                        'Rating': rating
                    })
                except Exception as e:
                    print(f"⚠️ Error al procesar un libro: {e}")
            
            return datos_libros
        else:
            print(f"❌ Error al cargar la página {numero_pagina}. Status: {response.status_code}")
            return []

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return []

def main():
    """
    Función principal que orquesta el scraping de múltiples páginas.
    """
    print("🚀 Iniciando Scraper de Libros...")
    todos_los_libros = []
    
    # Scrapeamos las primeras 3 páginas como demo
    for i in range(1, 4): 
        libros_pagina = obtener_datos_pagina(i)
        todos_los_libros.extend(libros_pagina)
        
        # Pausa ética para no saturar el servidor (buena práctica de ingeniería)
        time.sleep(random.uniform(1, 2))
    
    # Exportar a Excel/CSV con Pandas
    if todos_los_libros:
        df = pd.DataFrame(todos_los_libros)
        df.to_csv(DATA_EXPORT_FILE, index=False, encoding='utf-8-sig')
        print(f"\n✅ ÉXITO: Se han extraído {len(df)} libros.")
        print(f"📁 Datos guardados en: {DATA_EXPORT_FILE}")
        
        # Mostrar una vista previa
        print("\nVista previa de los datos:")
        print(df.head())
    else:
        print("\n⚠️ No se encontraron datos.")

if __name__ == "__main__":
    main()