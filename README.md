Last Nmae: Lee
First Name: Chang Suk

My project is to provide a service to test the strength of the password.
I'm using nodeJS to take the password from the user and then send the password to 
python and Java to test the strength of the password.

To connect between Java and Python rabbitMq was used.

For Java, I was planning to use SpringBoot and use REST API to connect between Java and NodeJS but
I didn't have enough time.

I'm using very simple and primitive method for guessing the password.
Basically, the program is guessing all possible combination of character within the min length of password
and the max length of the password. At first, I tried to use all combination of alphabet + digits + special characters.
However, the process time was so long if I did that, so I limited the password to be the combination of alphabet and digits only.
But still, it takes so much time to guess the password with length longer than 4.
