from PIL import Image, ImageDraw 

#Define how many bands do we need and final image resolution
how_much = 12
image_size = 512

one = [i for i in range(how_much+1)]
two = [i for i in reversed(range(how_much+1))]
three = []
for i in range(how_much+1):
    three.append(one[i])
    three.append(two[i])
four = [i for i in three]
for iter,i in enumerate(three):
    if iter==0:
        pass
    else:
        four[iter]=four[iter-1]+four[iter]

remap = lambda val : round(image_size * (val / max(four)))
remapped = list(map(remap,four))
print(remapped)

image = Image.new("L",(image_size,image_size),color=0)
draw = ImageDraw.Draw(image)

for iter,i in enumerate(remapped):
    try:
        pass
        col = "white" if iter%2 else "black"
        j = remapped[iter+1]
        draw.rectangle([i,0,j,image_size],outline=None,fill=col)
    except IndexError:
        pass
image.show()
