def name(x):
    return {"banana": "fruit",
            "apple": "fruit",
            "kiwi": "fruit",
            "cherry": "fruit",
            "lemon": "fruit",
            "grapes": "fruit",
            "tomato": "vegetable",
            "cucumber": "vegetable",
            "pepper": "vegetable",
            "carrot": "vegetable",
            }.get(x, "unknown")


print(name(input()))
