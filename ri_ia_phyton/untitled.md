# Ollama

Video: https://www.youtube.com/watch?v=Pc4jqk4E4TI&t=139s

Requisitos de Memoria:
- 7b models requieren al menos 8GB de Ram
- 13b models requieren al menos 16GB de Ram
- 70b models requieren al menos 64 GB de Ram.

Tenemos que cargar el modelo en **ollama**
```bash
ollama run llama2
```

```bash
# para ver los modelos que tenemos instalados...
ollama list

# para eliminar
ollama rm <modelo>

# ayuda
ollama /?

# salida
ollama /bye
```


# Ollama y jupyterlab

Ya lanzamos **jupyterlab** en un entorno virtual.
También importante leer la documentación.

Vídeos:
https://www.youtube.com/watch?v=ZaChVsOwtoo&t=80s

Dentro de la carpeta: **ri_ia_python** el fichero **Ollama.ipynb**

# Ollama y jupyterlab creando el primer modelo
#youtube #ollama #python

Ya lanzamos **jupyterlab** en un entorno virtual.

- Se utilizan para mejorar e incrementar las capacidades de los modelos LLMs.
- Utilizan BBDD vectoriales.
- El contexto se lo pasamos nosotros a partir de diferentes fuentes (pdfs, bbdd, texto, web...) que se guardan en partes dentro de la bbdd de tipo vectorial.

Usaremos **langchain** y **ollama**.

Requisitos de Memoria:
- 7b models requieren al menos 8GB de Ram
- 13b models requieren al menos 16GB de Ram
- 70b models requieren al menos 64 GB de Ram.
