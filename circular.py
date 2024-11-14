if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("check for opencv-python import")
    args.add_argument("full_version", help="full version")
    try:
        import cv2
        with open("succeeded.txt", "at") as f:
            f.write(f"{cv2.__version__=} \n")
    except ImportError:
        with open("failed.txt", "at") as f:
            f.write(f"{args.full_version=} \n")


