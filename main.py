import tkinter as tk
import text as info
import twitter_bot as bot


root = tk.Tk()
root.geometry("230x300")
# root.resizable(width=False, height=False)
root.title("Twitter Bot")


entries = [] #find in post_tweets_button


def tweet_once_button():
	post_window = tk.Toplevel()
	post_window.geometry("300x500")
	post_window.resizable(width=False, height=False)
	post_window.title("Tweet Once")

	tweet_text = tk.Text(post_window, height= 20, width = 33)
	tweet_text.grid(row = 0 , column = 0)

	def post_tweet():
		global final_text
		final_text = tweet_text.get("1.0",'end-1c')
		bot.tweet(final_text)
		answer.config(text= "Your tweet has been posted!")

	post = tk.Button(post_window, text = "Post", 
		padx = 50, pady = 20, command = post_tweet)
	post.grid(row = 5, column = 0)

	
	close_window = tk.Button(post_window, text = "Close", 
		padx = 50, pady = 20, command = lambda: post_window.destroy())
	close_window.grid(row = 6, column = 0)

	answer = tk.Label(post_window, text = "")
	answer.grid(row = 7, column = 0)


def post_tweets_button():
	post_tweets_window = tk.Toplevel()
	post_tweets_window.geometry("300x500")
	post_tweets_window.resizable(width=False, height=False)
	post_tweets_window.title("Post Tweets")

	delay_label = tk.Label(post_tweets_window, text = "Delay (in seconds)")
	delay_label.grid(row = 12, column = 0)

	for i in range(8):
		tweet_box = tk.Text(post_tweets_window, height = 2, width = 37)
		tweet_box.grid(row = i+1 , column = 0)
		entries.append(tweet_box)


	delay_box = tk.Entry(post_tweets_window, width = 20)
	delay_box.grid(row = 13, column = 0)
		
	def number():
		try:
			bot.post_delay = int(delay_box.get())
			answer.config(text= f"Your tweets are being posted each {bot.post_delay} seconds!")
		except ValueError:
			answer.config(text= "Please the amount of seconds")
				
	def post_all_tweets():
		for text in entries:
			final_tweets = text.get("1.0", "end-1c")
			bot.tweet_list.append(final_tweets)
			for i in bot.tweet_list:
				if i == "":
					bot.tweet_list.remove(i)

		number()
		bot.post_tweets()
		bot.tweet_list.clear()
		entries.clear()


	post_tweets = tk.Button(post_tweets_window, text = "Post",
		padx = 50, pady = 20, command = post_all_tweets)
	post_tweets.grid(row = 15, column = 0)

	close_window = tk.Button(post_tweets_window, text = "Close", 
		padx = 50, pady = 20, command = lambda: post_tweets_window.destroy())
	close_window.grid(row = 16, column = 0)

	answer = tk.Label(post_tweets_window, text = "")
	answer.grid(row = 14, column = 0)


def about_button():
	about_window = tk.Toplevel()
	about_window.geometry("230x300")
	about_window.resizable(width=False, height=False)
	about_window.title("About")

	about_text = tk.Label(about_window, text = info.about_text , padx = 23, pady = 30)
	about_text.grid(row = 0, column = 0)

	close_window = tk.Button(about_window, text = "Close", 
		padx = 96, pady = 30, command = lambda: about_window.destroy())
	close_window.grid(row = 1 , column = 0)


label = tk.Label(root, text = "Twitter Bot",  padx = 85, pady =30, bg = "blue")
label.grid(row = 0, column = 0, columnspan = 2)

tweet_once = tk.Button(root, text = "Tweet Once", padx = 23, pady =30, command = tweet_once_button)
tweet_once.grid(row = 1, column = 0)

post_tweets = tk.Button(root, text = "Post Tweets", padx = 21, pady =30, command = post_tweets_button)
post_tweets.grid(row = 1, column = 1)

exit = tk.Button(root, text = " Exit", padx = 43, pady =30, command = lambda: root.destroy())
exit.grid(row = 2, column = 0)

about = tk.Button(root, text = "About", padx = 37, pady =30, command = about_button)
about.grid(row = 2, column = 1)


root.mainloop()