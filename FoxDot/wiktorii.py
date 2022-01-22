# CMajor = [C, D, E, F, G, A, B]
print(SynthDefs)
p1 >> pluck([0,2,4], dur=[1, 1/2, 1/2], amp = 0.75) # 0,2,4 - C, E, G dur, nuty i polnuty, 
#amp glosnosc
p2 >> pluck([0,1,2,3], dur = 2) + [0,0,4]
p2.stop()

#Wiktorii
p2 >> feel([0,1,2,3,4,5,6,7,8], dur = [1/2, 1/2, 1/2]) + (0,2,4,6,8)
p3 >> glass([2,4,6,8,2,4,6,8], dur = [1/4,1/4, 1/4,1/4,1/4,1/4,1/4,1/4])
p4 >> charm([0,3,5,7,2,4,6], dur =[1, 1,1,1,1,1,1,1])

Clock.clear()

#music samples
d1 >> play("x-o-")
d2 >> play("x-o[---]", dur=1)
d3 >> play("x-o{-=*}")

#complete pattern 
d4 >> play("(x[--])xo{-[--][-x]}")
Clock.clear()
