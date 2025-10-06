def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
    except PermissionError:
        print(f"Error: permission denied: {filename}")
    except UnicodeDecodeError:
        print(f"Error: could not decode file as text: {filename}")
    except OSError as e:
        print(f"OS error while reading {filename}: {e}")
    except Exception as e:
        print(f"Unexpected error while reading {filename}: {e}")
    return None
