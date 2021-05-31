# stockNewsExtraHard
Unassisted challenge exercise

This was an unguided challenge exercise to create a program which sends the top three news stories for a given company depending on that company's stock performance [ie whether
it goes up or down a certain amount within a given time frame.]

I started out using the daily stock prices and performing my own calculations, but then the non-trading days presented a massive pain in the ass. So I went back to the api and
figured I'd simply use the spot prices, which included a % change. So that is what I ran with. The teacher in their solution turned the json data into a list and referenced it
by index, which is something that didn't occur to me. 

I then had to determine whether a stock had changed by x percent. The easiest way was to use a string slice and convert to float [so float(percentage_change[:-2])].

Then I had to get the news articles, which was easy enough. I used a list slice to get the first 3. I then defined a function to iterate through the slice and send a message for
each one, using the json data for the news articles and just referring to them in an fstring. 

And that was it! Although for some reason the environment variables didn't want to work. That being said, when I used the api-keys as strings in the program it worked just fine.
So I'm not sure.
