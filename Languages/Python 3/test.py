with open("file.txt", "w") as f:
    f.write("baba booey")
    # Format as JSON
    import json
    f.write(json.dumps({"a": 1, "b": 2}))