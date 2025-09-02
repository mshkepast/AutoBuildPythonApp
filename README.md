# AutoBuildPythonApp


Мінімальний приклад Python GUI (Tkinter), який збирається у portable `.exe` через GitHub Actions (PyInstaller).


## Як протестувати CI
1. Створи репозиторій та завантаж файли.
2. Створи тег і відправ його на GitHub:
```bash
git add .
git commit -m "init"
git tag v0.1.0
git push origin main --tags
