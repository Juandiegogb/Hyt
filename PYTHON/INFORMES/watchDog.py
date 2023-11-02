import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            new_folder_path = event.src_path
            destination_folder = '/ruta/destino/'  # Reemplaza esto con la ruta de la carpeta destino
            shutil.move(new_folder_path, destination_folder)
            print(f"Se movió la carpeta {new_folder_path} a {destination_folder}")

if __name__ == "__main__":
    folder_to_watch = '/ruta/a/observar/'  # Reemplaza esto con la ruta de la carpeta a observar
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
