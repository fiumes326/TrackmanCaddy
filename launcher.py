import TrackmanCaddy from TrackmanCaddy as caddy


try:
    myCaddy = caddy()
    print("Caddy is ready, play away!")

    while True:

except KeybaodInterrupt:
    print("Tipping caddy and shutting down...")

finally:
    caddy.shutdown()
