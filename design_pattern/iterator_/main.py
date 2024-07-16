from browse_history import BrowserHistory


if __name__ == '__main__':
    history = BrowserHistory()
    history.push("https://www.google.com")
    history.push("https://www.facebook.com")

    # The key problem comes with this potential iteration operation

    # If later we decided to use something else to store the history,
    # this loop operation might be problematic.

    # It seems the implementation in python is much easier compared to
    # in Java

    for url in history:
        print("Iterating")
        print(url)

    print(history.get_history())
