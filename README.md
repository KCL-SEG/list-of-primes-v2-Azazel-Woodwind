# Primes exercise

## Assignment
You should already have tackled a version of the is exercise earlier.  This repository contains some template code for a function called `primes`, which takes a single argument `number_of_primes`:

```
def primes(number_of_primes):
    list = []
    return list
```

In this exercise, you must extend the code such that, given a positive value for `number_of_primes`, the `primes` function returns a list containing the first `number_of_primes` prime numbers.  For example, `primes(10)` should the following list:

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

If `primes` is called with argument 0 or a negative number, it must raise a `ValueError`.

If you did the previous version of this exercise, copy your code from that solution here to start.  Then extend it to raise the exceptions required.

## Expectations
Once your solution works, review it to see whether you can improve it.  Make sure the meaning of the variables is easy to understand.  Try to keep your functions small.  Consider whether there is scope to improve the performance of your algorithm.

## How to complete the exercise
To start work on the exercise, find the URL of this repository on GitHub and clone it to your machine with:

`$ git clone URL`

where `URL` is the URL of your repository on GitHub.  Find the `primes.py` file and complete your solution.

You can test your solution in the development environment by running pytest.  From the root of your Python project, simply run

`$ pytest`

If pytest has not been installed yet, run:

`$ pip3 install pytest`

I recommend that you test your solution locally, but you do not have to do this.  Once your exercise is complete, you need to push your repository with:

`$ git push`

GitHub will automatically test your solution. 
