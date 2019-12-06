# URL Shortener Service

This Readme file just explains a summary of what i did and what 
i could do but because i'm working somewhere else now i haven't 
much more time to work on this.

So here is a summary:
--------
I used ```JWT``` for authentication and authorization as you can see in `iam` application.

There is another app called client that has a ```OneToOne``` relationship to
```iam_user``` table. I did this because maybe we could add more fields to client 
and have more types of users in this system.

Link application just maps the `short_url` to `long_url` and redirects client to that.

Analytics application will handle all the reporting system. So it's just some models for storing 
data and calculate these in periodic jobs.

I tried to do my best for this url shortener app but as i said lack of time for me 
made me stop here. so i will just call some of features that could make this faster.

- First of all we could cache analytics get methods with a cache page of 1 hour.

- Second i created ``viewer`` in async way so client should not wait for creating that model.

Maybe there is more that i could not remember or don't know.

Benchmarking
------
i used  [Locust](https://locust.io/) as a benchmarking tool. i used this before. I simulated 
test with 1000 users and 120 for hatch rate. I got a csv file at one minute stress test that 
i locate this file in logs folder of project. I used your sample link for testing.
This URL `https://example.com/my-very-long-url-3XL6su64dD4Of9OwZS9lg5jOSVxIhgb1JF1JyBlE` but because 
it returns 404 all the redirection requests has a failed status so dont count it a failure.

At the end
-----
I really hope you like how i created and coded in this project
and i could take a backend develop job position in your company.
