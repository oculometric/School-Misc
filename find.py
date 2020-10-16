def find ():
    for a in range (0, 10):
        for b in range (0, 10):
            for c in range (0, 10):
                for d in range (0, 10):
                    for e in range (0, 10):
                        for f in range (0, 10):
                            for g in range (0, 10):
                                for h in range (0, 10):
                                    for i in range (0, 10):
                                        for j in range (0, 10):
                                            arr = [a,b,c,d,e,f,g,h,i,j]
                                            keepgoing = True
                                            for x in range (0, 10):
                                                for y in range (0, 10):
                                                    if (arr[x] == arr[y]) and (x != y):
                                                        keepgoing = False
                                                        break
                                                if keepgoing == False:
                                                    break
                                                    
                                        
                                            if (a % 1 != 0): continue
                                            if (((a*10)+b) % 2 != 0): continue
                                            if (((a*100)+(b*10)+c) % 3 != 0): continue
                                            if (((a*1000)+(b*100)+(c*10)+d) % 4 != 0): continue
                                            if (((a*1000)+(b*1000)+(c*100)+(d*10)+e) % 5 != 0): continue
                                            if (((a*10000)+(b*10000)+(c*1000)+(d*100)+(e*10)+f) % 6 != 0): continue
                                            if (((a*100000)+(b*100000)+(c*10000)+(d*1000)+(e*100)+(f*10)+g) % 7 != 0): continue
                                            if (((a*1000000)+(b*1000000)+(c*100000)+(d*10000)+(e*1000)+(f*100)+(g*10)+h) % 8 != 0): continue
                                            if (((a*10000000)+(b*10000000)+(c*1000000)+(d*100000)+(e*10000)+(f*1000)+(g*100)+(h*10)+i) % 9 != 0): continue
                                            if (((a*100000000)+(b*100000000)+(c*10000000)+(d*1000000)+(e*100000)+(f*10000)+(g*1000)+(h*100)+(i*10)+j) % 10 != 0): continue
                                            return ((a*100000000)+(b*100000000)+(c*10000000)+(d*1000000)+(e*100000)+(f*10000)+(g*1000)+(h*100)+(i*10)+j)
                                            


print (find ())
