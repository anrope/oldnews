# ![OldNews Logo](https://raw.githubusercontent.com/anrope/oldnews/master/resources/OldNews_OldMan_600px.png)


**Current project status**: v1.0: Ketchup

---

Who better to recommend what you should read today than you? Our project is a "throwback recommendation engine" powered by your past self. It was created at the third Hacking Journalism, which was hosted at the Washington Post.

##Slides
See the <a href="https://docs.google.com/presentation/d/1AEq2_NnTDShNXdvNn8rZfp1pRXz1Hztd296X8qAkXVQ/edit?usp=sharing">project slides</a> for more information on our project.

##Backend

The backend is written in Python, and takes care of ingesting a list of article urls representing the user's reading history. Each article is passed to the Embedly Extract API to grab necessary metadata including title, image, keywords, and related articles. The url and metadata are pushed into a Firebase database for consumption by the frontend.

## Credits

- Lindsey Carbonell: <a href="https://twitter.com/authoressence">@authoressence</a>
- Emily Greenhalgh: <a href="https://twitter.com/emwritesscience">@emwritesscience</a>
- Will Halicks: <a href="https://twitter.com/whalicks">@whalicks</a>
- Colleen Mcenaney: <a href="https://twitter.com/colleenmcenaney">@colleenmcenaney</a>
- Andrew Nguyen: <a href="https://twitter.com/onlyandrewn">@onlyandrewn</a>
- Andy Pellett: <a href="https://twitter.com/anrop">@anrop</a>
- Justina Vasquez: <a href="https://twitter.com/helloimjustina">@helloimjustina</a>

