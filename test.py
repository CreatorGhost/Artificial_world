import webScrap
import model

url = "https://medium.com/swlh/automatic-image-captioning-using-deep-learning-5e899c127387"


text=webScrap.getUrl(url)

summary=model.generate_summary(text,4)

print(summary)