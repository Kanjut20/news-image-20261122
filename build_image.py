from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W=H=1024
NAVY=(15,42,68); GOLD=(212,175,55); BG=(245,244,239); WHITE=(255,255,255)
INK=(20,28,38); GREY=(90,98,110)
img=Image.new("RGB",(W,H),BG)
d=ImageDraw.Draw(img)
def font(name,size,bold=False):
    p=f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf"
    return ImageFont.truetype(p,size)
def wrap(text,f,maxw,draw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if draw.textlength(t,font=f)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

# Header
d.rectangle([0,0,W,168],fill=NAVY)
d.text((32,22),"WORLD NEWS",font=font("s",58,True),fill=WHITE)
d.text((32,96),"SUNDAY  •  22 NOVEMBER 2026",font=font("s",30,True),fill=GOLD)
d.text((700,30),"THE DAY IN",font=font("s",22,True),fill=(180,200,220))
d.text((700,58),"ONE IMAGE",font=font("s",22,True),fill=(180,200,220))
d.rectangle([0,168,W,174],fill=GOLD)

panels=[
 ("CLIMATE  •  COP31, ANTALYA","COP31 ENDS WITH\nNO DEAL","Nearly 200 nations fail to agree\non fossil fuels and climate finance.",(178,34,34)),
 ("JUSTICE  •  THE HAGUE","ICJ: MYANMAR\nCOMMITTED GENOCIDE","Court rules against Myanmar over\nthe Rohingya minority.",(31,58,95)),
 ("WAR  •  LIBYA","UKRAINE SANK A\nRUSSIAN WARSHIP","Zelenskyy says Ukraine was behind\nthe drone strike in Benghazi port.",(90,50,120)),
 ("ENERGY  •  STRAIT OF HORMUZ","TANKERS HIT AS\nIRAN TENSIONS RISE","Iran strikes tankers; Bahrain says\nan attack hit a plant, injuring 2.",(140,90,0)),
 ("MIDDLE EAST  •  WEST BANK","SETTLERS TORCH\nHOMES & CARS","Dozens raid Palestinian villages;\nIsrael's opposition calls it terrorism.",(0,110,90)),
 ("ASIA  •  INDONESIA","34 MISSING IN\nFACTORY FIRE","Candy-factory fire in Indonesia;\nrescue teams recover remains.",(150,40,40)),
]
# grid 2 cols x 3 rows
x0,y0=24,190; pw,ph=476,236; gx,gy=24,16
for i,p in enumerate(panels):
    kicker,head,sub,color=p
    x=x0+(i%2)*(pw+gx); y=y0+(i//2)*(ph+gy)
    d.rounded_rectangle([x,y,x+pw,y+ph],radius=14,fill=WHITE,outline=(210,210,205),width=2)
    d.rounded_rectangle([x,y,x+pw,y+58],radius=14,fill=color)
    d.rectangle([x,y+40,x+pw,y+58],fill=color)
    d.text((x+16,y+15),kicker,font=font("s",17,True),fill=WHITE)
    # number badge
    d.ellipse([x+pw-52,y+70, x+pw-14,y+108],fill=color)
    d.text((x+pw-40,y+76),str(i+1),font=font("s",24,True),fill=WHITE)
    yy=y+70
    for line in head.split("\n"):
        d.text((x+16,yy),line,font=font("s",29,True),fill=INK); yy+=36
    yy+=6
    for line in wrap(sub,font("s",19),pw-32,d):
        d.text((x+16,yy),line,font=font("s",19),fill=GREY); yy+=25

# footer
fy=y0+3*(ph+gy)+4
d.rounded_rectangle([24,fy,1000,fy+62],radius=12,fill=NAVY)
d.text((40,fy+18),"ALSO:  Kyiv strike kills 3  •  Nigeria boat, 24 dead  •  Mexico cartel chief captured",
       font=font("s",16,True),fill=WHITE)
out="/home/hatch/workspace/goals/make-fun-contest-entries/files/news-image-20261122/entry.png"
os.makedirs(os.path.dirname(out),exist_ok=True)
img.save(out,optimize=True)
print(out, os.path.getsize(out), img.size)
