def estimate_origin(similar_results):
    """
    similar_results = output from similarity search
    """

    if not similar_results:
        return None

    # Sort by date (earliest first)
    sorted_results = sorted(similar_results, key=lambda x: x["date"])

    # Pick earliest
    origin = sorted_results[0]

    return {
        "estimated_image": origin["image"],
        "source": origin["source"],
        "date": origin["date"],
        "confidence": round(origin["similarity"] * 100, 2)
    }