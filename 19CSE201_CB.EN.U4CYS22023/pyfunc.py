batches=["Hamsini"]
batches.append("Vetrivel")
batches.append("Dev")
batches.append("Hemadhri")
batches.insert(0,"Dharshika")
batches.insert(0,"Deepak")
batches.insert(0,"Hansica")

batches.pop(1)

batches.remove("Hansica")
batches.sort(reverse=True)
print(batches)
