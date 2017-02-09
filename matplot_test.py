import matplotlib.pyplot as plt



img = plt.imread('./000000010.jpg')
#plt.imshow(img)

fig, ax = plt.subplots(figsize=(12,12)) #
ax.imshow(img, aspect='equal', )

ax.add_patch( plt.Rectangle((300, 300), 400, 600, fill=False, edgecolor='red', linewidth=3, linestyle='solid') )
ax.text(100, 100, '{}nihao{}'.format('l_', '_hh'), fontsize=24)
ax.set_title('sss', fontsize=14)

plt.axis('off')
plt.tight_layout()
plt.draw()

#plt.savefig('')
fig.savefig('./test.jpg', dpi=90)

plt.show()

