from TrackmanCaddy import TrackmanCaddy as caddy
import time

try:
    print("Grabbing you a caddy...\n")
    myCaddy = caddy()
    myCaddy.set_hotkeys()
    myCaddy.start_watcher_thread()
    print("Caddy is ready, play away!\n")

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Tipping caddy and shutting down...")

finally:
    myCaddy.shutdown()
    print("Bye!")
