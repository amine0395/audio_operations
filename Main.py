import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import  convert
def on_created(event):
    print("created")
    convert.mp3_to_wav(str(event.src_path))

def on_deleted(event):
    print("deleted")
def on_modified(event):
    print("modified")
def on_moved(event):
    print("moved")

if __name__ == "__main__":

    event_handler = FileSystemEventHandler()

    event_handler.on_created = on_created
    event_handler.on_moved = on_moved
    event_handler.on_deleted= on_deleted
    event_handler.on_modified=on_modified

    path="C:/Users/amine/Desktop/watch"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        print("done")