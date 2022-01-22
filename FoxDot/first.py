# CMajor = [C, D, E, F, G, A, B]
print(SynthDefs)
p1 >> pluck([0,2,4], dur=[1, 1/2, 1/2], amp = 0.75) # 0,2,4 - C, E, G dur, nuty i polnuty, 
#amp glosnosc
p2 >> pluck([0,1,2,3], dur = 2) + [0,0,4]
p2.stop()

#akord(krotki)
p1 >> ambi([0,2,4], dur=[1, 1/2, 1/2], amp = 0.75)
p1.stop()
p3 >> glass([0,1,2,3], dur = [1, 1/2, 1/2]) + (0,2,4)
p3.stop()

#music samples
d1 >> play("x-o-")
d2 >> play("x-o[---]", dur=1)
d3 >> play("x-o{-=*}")

#complete pattern 
d4 >> play("(x[--])xo{-[--][-x]}")
