Proyecto 2: Agente lector de papers

Descripción. Recibe una URL o PDF de arXiv y produce una ficha técnica del paper.

Herramientas mínimas

load_pdf(path_or_url): extrae el texto por secciones.
get_section(name): devuelve una sección concreta (abstract, método, resultados, conclusiones).
extract_references(n): lista las referencias principales.

Salida esperada (esquema)

Problema que aborda, método propuesto, datos usados, resultados clave, limitaciones y 3 preguntas abiertas.
Cada afirmación importante debe ir con la sección de la que procede.

Restricciones

Si una sección no existe o el PDF no se puede leer, el agente lo dice en lugar de rellenar.

Criterios de aceptación

Probado con 3 papers de temas distintos.
Un papel con tablas o fórmulas no rompe el agente.

===============================================================
01-single-agent

Agente de logs Linux: lee journalctl o /var/log, detecta errores recurrentes y propone una causa probable. Encaja con tu perfil de sistemas.
Agente de lectura de papers: le das un PDF de arXiv y devuelve resumen, metodología, limitaciones y preguntas abiertas.
Agente de documentación de repos: recorre un repo y genera o actualiza su README y docstrings.

02-multi-agent

Pipeline de revisión de Pull Requests: un agente revisa seguridad, otro estilo y otro cobertura de tests, y un supervisor une el informe. Se puede conectar a la API de GitHub.
Equipo de preparación de entrevistas: un agente analiza la oferta de empleo, otro compara con tu CV, otro simula preguntas técnicas y otro corrige tus respuestas.
Debate entre agentes para evaluar decisiones técnicas: uno defiende Kubernetes, otro Docker Compose, y un juez decide según tu contexto.

03-langgraph-workflows

Secuencial: ETL asistido por LLM que limpia un CSV sucio, infiere el esquema y genera el SQL de carga.
Paralelo: buscador de ofertas que consulta varias fuentes a la vez y fusiona y puntúa los resultados.
Condicional: triage de incidencias de infraestructura, que enruta alertas a “reiniciar servicio”, “escalar” o “ignorar” según severidad.
Iterativo: generador de consultas SQL que ejecuta, lee el error y se corrige hasta que la consulta funciona.

04-chatbot-memoria

Tutor personal de alemán: recuerda el vocabulario que fallas y repasa ese contenido en sesiones posteriores (memoria a largo plazo).
Asistente de proyecto: guarda decisiones técnicas tomadas en conversaciones anteriores y las recupera cuando preguntas “¿por qué elegimos X?”.
Comparador de modelos con LangSmith: el mismo chatbot con dos modelos distintos y un informe de coste, latencia y calidad.

05-tools-y-rag

Agente con tools de sistema: consulta uso de CPU/disco, puertos y contenedores Docker con herramientas seguras de solo lectura.
RAG sobre normativa o convocatorias públicas (BOE, ayudas, becas), con citas a la fuente y evaluación con RAGAS.
Agente SQL sobre datos abiertos: pregunta en lenguaje natural sobre un dataset público y devuelve tabla y gráfico.

06-human-in-the-loop

Agente de despliegue: propone los pasos de un docker compose up o un cambio de configuración y espera tu “OK” en cada paso crítico.
Moderador de contenido: clasifica textos y solo envía a revisión humana los casos con baja confianza.
Editor de CV asistido: propone cambios en tu CV adaptados a una oferta y tú aceptas o rechazas cada uno.

07-deploy

API de agente en Docker con /health, logs estructurados y variables de entorno bien gestionadas.
CI con evaluación automática: GitHub Actions que ejecuta tests y una evaluación RAGAS mínima, y bloquea el merge si baja la calidad.
Despliegue en Kubernetes local (kind o minikube) del mismo agente. Combina bien con tus certificaciones DevOps.

08-proyectos-finales

Observatorio de vivienda con asistente: RAG + SQL sobre los datos públicos del proyecto de portfolio que ya tienes en mente.
Copiloto DevOps: agente que explica errores de Docker, Bash o Kubernetes y sugiere comandos con confirmación humana.
Herramienta open source pequeña: una CLI de agente que haga una sola cosa útil (por ejemplo, “explica este error de terminal”).