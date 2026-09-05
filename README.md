<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3776AB,50:27AAE1,100:2496ED&height=200&section=header&text=Pablo%20RS&fontSize=62&fontColor=ffffff&fontAlignY=34&desc=Python%20%C2%B7%20Automation%20%C2%B7%20Distributed%20Agents&descAlignY=54&descSize=17&animation=fadeIn" width="100%" alt="Pablo RS — Python, Automation, Distributed Agents">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=900&color=1A7BB8&center=true&vCenter=true&width=600&height=45&lines=Junior+Software+Developer;Agents+that+talk+over+a+message+bus;Python+%2B+NATS+%2B+Docker;I+automate+my+own+workflows" alt="Junior Software Developer — agents, Python, NATS, Docker">

<br>

<a href="mailto:pablorgz98@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
</a>
<a href="https://www.linkedin.com/in/pablors98">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="https://github.com/PabloRS98?tab=repositories">
  <img src="https://img.shields.io/badge/Projects-181717?style=for-the-badge&logo=github&logoColor=white" alt="Projects">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/NATS-27AAE1?style=flat-square&logo=natsdotio&logoColor=white" alt="NATS">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter">

<sub>🇬🇧 English · <a href="#-en-español">🇪🇸 Léelo en español</a></sub>

</div>

<br>

> [!TIP]
> **Open to junior developer roles, internships and collaborative projects.**
> The fastest way to reach me is [email](mailto:pablorgz98@gmail.com) or [LinkedIn](https://www.linkedin.com/in/pablors98).

<br>

## 👋 About me

I'm a junior developer who prefers building over reading about building. Lately my work has
converged on one thing: **automating my own workflows with Python** — assistant agents that talk
to each other over a message bus, bots that report to me on Telegram, and dashboards that pull
everything into one place.

It also means owning the unglamorous parts: the data model, the deployment, the configuration,
and making it all survive a reboot on a machine that isn't mine.

<br>

## 🧠 How my agents talk to each other

The pattern behind my current work — two agents exchanging messages over a **NATS** bus, with
**Telegram** as the human-facing interface:

```mermaid
flowchart LR
    U(["👤 User"]) <--> TG["📱 Telegram Bot"]
    TG <--> H1["🤖 Hermes Agent 1"]
    H1 <--> N{{"⚡ NATS<br>message bus"}}
    N <--> H2["🤖 Hermes Agent 2"]

    style U fill:#3776AB,stroke:#27AAE1,color:#fff
    style TG fill:#26A5E4,stroke:#27AAE1,color:#fff
    style N fill:#27AAE1,stroke:#2496ED,color:#fff
```

<br>

## 🚀 Projects

<table>
<tr>
<td width="50%" valign="top">

### ⚡ [Arquitectura Doble Agente](https://github.com/PabloRS98/arquitectura-doble-agente)

A reference architecture for two Hermes agents that talk to each other over **NATS**, with
Telegram as the human-facing interface. Documents the messaging patterns and the wiring, so the
whole setup can be reproduced from scratch.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/NATS-27AAE1?style=flat-square&logo=natsdotio&logoColor=white" alt="NATS">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram">

</td>
<td width="50%" valign="top">

### 📊 [Projects Dashboard](https://github.com/PabloRS98/projects-dashboard)

A multi-forge project manager that aggregates repositories from **GitHub, GitLab and Bitbucket**,
scans local clones for uncommitted or unpushed work, and pushes alerts to Telegram.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/REST_APIs-4479A1?style=flat-square&logo=fastapi&logoColor=white" alt="REST APIs">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram">

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📚 [Content-Media-Manager](https://github.com/PabloRS98/Content-Media-Manager)

A self-hosted catalog for books, movies, series, games and podcasts. Everything lives on your own
machine: **no cloud, no paid APIs, one Docker container**. Because tracking a personal library
shouldn't require a subscription.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/MIT-A31F34?style=flat-square" alt="MIT">

</td>
<td width="50%" valign="top">

### 💰 [Finance Tracker](https://github.com/PabloRS98/finance-tracker)

A personal finance manager built with **Flask** — tracking income, expenses and balances through
a web interface.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">

</td>
</tr>
</table>

<details>
<summary><b>🎮 ProyectoGRPG</b> — cross-platform RPG built with Flutter <sub>(private)</sub></summary>

<br>

My largest codebase so far, and where most of my Dart and application-architecture learning has
happened. Still private while in development — happy to walk through the code or the architecture
on request.

<img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart">
<img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter">

</details>

<br>

## 🛠️ Tech Stack

<table>
<tr>
<td valign="top"><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white" alt="Dart">
</td>
</tr>
<tr>
<td valign="top"><b>Frameworks</b></td>
<td>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flutter">
</td>
</tr>
<tr>
<td valign="top"><b>Infra &amp; Messaging</b></td>
<td>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/NATS-27AAE1?style=for-the-badge&logo=natsdotio&logoColor=white" alt="NATS">
<img src="https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot API">
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux">
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</td>
</tr>
</table>

<br>

## 📫 Get in touch

I'm actively looking for my first professional opportunity as a developer. If you think I could be
a fit for your team — or you just want to talk about a project — I'd be glad to hear from you.

<div align="center">

<a href="mailto:pablorgz98@gmail.com">
  <img src="https://img.shields.io/badge/pablorgz98@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="pablorgz98@gmail.com">
</a>
<a href="https://www.linkedin.com/in/pablors98">
  <img src="https://img.shields.io/badge/in/pablors98-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin.com/in/pablors98">
</a>

</div>

<br>

---

<h2 id="-en-español">🇪🇸 En español</h2>

<details>
<summary><b>Haz clic para desplegar la versión en español</b></summary>

<br>

**💼 Abierto a puestos junior, prácticas y proyectos en colaboración.** La vía más rápida para contactarme es [email](mailto:pablorgz98@gmail.com) o [LinkedIn](https://www.linkedin.com/in/pablors98).

### 👋 Sobre mí

Soy un desarrollador junior al que le sirve más construir que leer sobre cómo construir.
Últimamente mi trabajo ha convergido en una sola cosa: **automatizar mis propios flujos con
Python** — agentes asistentes que se comunican entre sí por un bus de mensajes, bots que me
reportan por Telegram y paneles que lo reúnen todo en un mismo sitio.

También significa encargarme de las partes que no lucen: el modelo de datos, el despliegue, la
configuración y conseguir que todo sobreviva a un reinicio en una máquina que no es la mía.

### 🧠 Cómo se comunican mis agentes

El patrón detrás de mi trabajo actual: dos agentes intercambiando mensajes por un bus **NATS**,
con **Telegram** como interfaz para el usuario.

```mermaid
flowchart LR
    U(["👤 Usuario"]) <--> TG["📱 Bot de Telegram"]
    TG <--> H1["🤖 Agente Hermes 1"]
    H1 <--> N{{"⚡ NATS<br>bus de mensajes"}}
    N <--> H2["🤖 Agente Hermes 2"]

    style U fill:#3776AB,stroke:#27AAE1,color:#fff
    style TG fill:#26A5E4,stroke:#27AAE1,color:#fff
    style N fill:#27AAE1,stroke:#2496ED,color:#fff
```

### 🚀 Proyectos

**⚡ [Arquitectura Doble Agente](https://github.com/PabloRS98/arquitectura-doble-agente)** — `Python` · `NATS` · `Telegram`

Una arquitectura de referencia para dos agentes Hermes que se comunican por **NATS**, con Telegram
como interfaz para el usuario. Documenta los patrones de mensajería y el cableado necesario para
reproducir el montaje desde cero.

**📊 [Projects Dashboard](https://github.com/PabloRS98/projects-dashboard)** — `Python` · `APIs REST` · `Telegram`

Un gestor de proyectos multi-forge que agrega repositorios de **GitHub, GitLab y Bitbucket**,
escanea los clones locales en busca de trabajo sin commitear o sin subir, y envía alertas por
Telegram.

**📚 [Content-Media-Manager](https://github.com/PabloRS98/Content-Media-Manager)** — `Python` · `Docker` · `MIT`

Un catálogo self-hosted para libros, películas, series, videojuegos y podcasts. Todo vive en tu
propia máquina: **sin nube, sin APIs de pago, un solo contenedor Docker**. Porque llevar el
registro de una biblioteca personal no debería exigir una suscripción.

**💰 [Finance Tracker](https://github.com/PabloRS98/finance-tracker)** — `Python` · `Flask`

Un gestor de finanzas personales hecho con **Flask**: seguimiento de ingresos, gastos y saldos a
través de una interfaz web.

**🎮 ProyectoGRPG** — `Dart` · `Flutter` · *privado*

Un proyecto de RPG multiplataforma hecho con Flutter. Es mi base de código más grande hasta la
fecha y donde he aprendido la mayor parte de lo que sé de Dart y de arquitectura de aplicaciones.
Sigue en privado mientras está en desarrollo — encantado de enseñar el código o explicar la
arquitectura si hay interés.

### 🛠️ Stack tecnológico

| | |
|:--|:--|
| **Lenguajes** | Python · Dart |
| **Frameworks** | Flask · Flutter |
| **Infraestructura y mensajería** | Docker · NATS · Telegram Bot API · SQLite · Linux · Git |

### 📫 Contacto

Estoy buscando activamente mi primera oportunidad profesional como desarrollador. Si crees que
puedo encajar en tu equipo — o simplemente quieres hablar de algún proyecto — escríbeme.

| | |
|---|---|
| 📧 **Email** | [pablorgz98@gmail.com](mailto:pablorgz98@gmail.com) |
| 💼 **LinkedIn** | [linkedin.com/in/pablors98](https://www.linkedin.com/in/pablors98) |

<div align="center"><a href="#"><b>⬆️ Volver arriba</b></a></div>

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2496ED,50:27AAE1,100:3776AB&height=120&section=footer" width="100%" alt="">
</div>
