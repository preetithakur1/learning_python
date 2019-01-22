import numpy as mp
x = [1,2,3]
y = [1,2,3]
a = mp.add(x,y)
print(a)

ax = {
	"tim" : "teamA",
	"sam" : "teamB"
}
print(ax)
print(ax["tim"])
del ax["tim"]
print(ax)
ax["Deep"] = "teamC"
print(ax)

