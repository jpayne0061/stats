import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open("/home/ubuntu/workspace/charges2.txt").read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('crime_cloud.png', bbox_inches="tight")