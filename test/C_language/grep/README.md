man grep
grep "Apple" demo.text
    grep 'Apple' demo.text
result: Apple

grep 'apple' demo.txt
reult: apple
       applecake

grep -w 'apple' demo.txt [whole words only]
reult: apple

grep -i 'apple' demo.txt [case senstive]
result: apple
        applecake
        Apple
    
grep -n 'apple' demo.txt  [shows number]
result: 1:apple
        2:applecake

grep -B n 'watermelon' demo.txt [behind] 
grep -A n 'watermelon' demo.txt [front]
grep -C n 'watemelon' demo.txt [all file]
n= number you want to see 

grep 'apple' ./* [* checks all files in directory]

grep -r 'apple' ./ [recusive]

grep -l 'apple' ./* [see location]

grep '...-....' demo.txt
grep '\d{3} \d{4}' demo.txt
results: watermelon ice-cream
        red lips

