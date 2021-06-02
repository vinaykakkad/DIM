<div align="center">
  
<img src="https://doge-in.herokuapp.com/static/images/logo.png">
  
</div>  

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


# DIM Prototype✨
Prototype made for the course ENR 200 - Design, Innovation and Making


## Demo💻

[Demo](https://doge-in.herokuapp.com/)

  
## Environment Variables⚙

To run this project, you will need to add the following environment variables to a .env file at the root of the project

- `EMAIL_HOST_USER` : Your smtp email servie provider

- `EMAIL_HOST_PASSWORD` : Password for your smtp email service provder

You can use smtp providers like gmail, sendgrid etc. Update the `EMAIL_HOST` in dim/settings.py accordingly.


## Run Locally🚀

Clone the project

```bash
  git clone https://github.com/vinaykakkad/DIM
```

Go to the project directory

```bash
  cd DIM
```

Create Environement and install dependencies
```bash
python m venv env
env\Scripts\activate
pip install -r requirements.txt
```

Make migrations and start the server

```bash
  python manage.py makemigrations 
  python manage.py migrate
  python manage.py runserver
```

  
## Features🧾

You can register as a user, tech-expert or recruiter

<details>
  <summary>For users</summary>
  
  - Get job opportunites based on your profile
  - Post events to search for speakers / experts
  - Find relvant courses using proper filters
  - Forum to get some motivation and clear your doubts
  - Chat with peers, experts and recruites
</details>

<details>
  <summary>For tech-experts</summary>
  
  - Get job opportunites based on your profile
  - Find events to take a session based on your expertise
  - Forum to get some motivation and share your knowledge
  - Chat with peers, user and recruites
</details>

<details>
  <summary>For recruiters</summary>
  
  - Find relevant candidates for job-openings
  - Post events to search for speakers / experts
  - Forum to get some motivation and share your knowledge
  - Chat with users, experts and other recruiters
</details>


## Tech Stack👨‍💻

**Frontend:** HTML, CSS, JS, Bootstrap, React

**Backend:** Django, Firebase
  
  
## License🔐

[MIT](https://github.com/vinaykakkad/DIM/blob/main/LICENSE)  

## Contributors ✨
[emoji key](https://allcontributors.org/docs/en/emoji-key)

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/vinaykakkad"><img src="https://avatars.githubusercontent.com/u/56934712?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vinay Kakkad</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=vinaykakkad" title="Code">💻</a> <a href="https://github.com/vinaykakkad/DIM/commits?author=vinaykakkad" title="Documentation">📖</a> <a href="#design-vinaykakkad" title="Design">🎨</a> <a href="#maintenance-vinaykakkad" title="Maintenance">🚧</a> <a href="#projectManagement-vinaykakkad" title="Project Management">📆</a></td>
    <td align="center"><a href="https://github.com/nipun3333"><img src="https://avatars.githubusercontent.com/u/70288062?v=4?s=100" width="100px;" alt=""/><br /><sub><b>nipun3333</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=nipun3333" title="Code">💻</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/tirth-patel-412b70192"><img src="https://avatars.githubusercontent.com/u/64124305?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tirth Patel</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=tirthPatel177" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Poojan987"><img src="https://avatars.githubusercontent.com/u/59042591?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Poojan987</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=Poojan987" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jinesh0109"><img src="https://avatars.githubusercontent.com/u/70638580?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jinesh Salot</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=jinesh0109" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/RP-72"><img src="https://avatars.githubusercontent.com/u/59957244?v=4?s=100" width="100px;" alt=""/><br /><sub><b>RP-72</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=RP-72" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Hirmay"><img src="https://avatars.githubusercontent.com/u/56473003?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hirmay Sandesara</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=Hirmay" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
