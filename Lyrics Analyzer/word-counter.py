# Input any text within text string to get output working

text = """
Now I've heard there was a secret chord
That David played, and it pleased the Lord
But you dont really care for music, do you?
It goes like this, the fourth, the fifth
The minor falls, the major lifts
The baffled king composing Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Your faith was strong but you needed proof
You saw her bathing on the roof
Her beauty and the moonlight overthrew her
She tied you to a kitchen chair
She broke your throne, and she cut your hair
And from your lips she drew the Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Well, maybe there's a God above
As for me all I've ever learned from love
Is how to shoot somebody who outdrew you
But it's not a crime that you're hear tonight
It's not some pilgrim who claims to have seen the Light
No, it's a cold and it's a very broken Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Instrumental
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Well people I've been here before
I know this room and I've walked this floor
You see I used to live alone before I knew ya
And I've seen your flag on the marble arch
But listen love, love is not some kind of victory march, no
It's a cold and it's a broken Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
There was a time you let me know
What's really going on below
But now you never show it to me, do you?
And I remember when I moved in you
And the holy dove she was moving too
And every single breath we drew was Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Now I've done my best, I know it wasn't much
I couldn't feel, so I tried to touch
I've told the truth, I didnt come here to London just to fool you
And even though it all went wrong
I'll stand right here before the Lord of song
With nothing, nothing on my tongue but Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Hallelujah, Hallelujah
Hallelujah
"""

print(text.split(), sep="\n")

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count, sep="/n")