from ddgs import DDGS


def web_search(
    query,
    max_results=5,
):
    """
    Performs a web search using DDGS.
    """

    try:

        with DDGS() as ddgs:

            results = list(

                ddgs.text(

                    query,
                    max_results=max_results,

                )

            )

        formatted_results = []

        for result in results:

            formatted_results.append(

                {
                    "title": result["title"],
                    "url": result["href"],
                    "snippet": result["body"],
                }

            )

        return formatted_results

    except Exception as error:

        raise RuntimeError(
            f"Web search failed.\n\n{error}"
        ) from error