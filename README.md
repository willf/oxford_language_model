## Python client for the Project Oxford web language model API 

This is a client for the Project Oxford Web Language Model API

Information about the Web Language Model API can be found at 
https://msdn.microsoft.com/en-US/library/mt628626.aspx
    
You will need a subscription key to use this services. There are limits to 
the number of calls one can make to this service, and rate limits. This client 
does not concern itself with these limits.

Example uses:

   > import oxford_language_model
   > client = oxford_language_model.Client()
   > tobreak = 'thebeatles'
   > print(client.break_into_words(tobreak)[0]['words'])
   "the beatles"
   > print(client.generate_next_words('the world wide')[0]['word'])
   "web"
