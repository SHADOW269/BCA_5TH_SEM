# Function to check if a number is prime
is_prime <- function(n) {
  if (n == 1) {
    return(FALSE)
  }
  if (n == 2) {
    return(FALSE)
  }
  if (n == 3) {
    return(TRUE)
  }
  #if (n %% 2 == 0) {
   #  return(FALSE)
  #}
  for (i in 2:sqrt(n)) {
    if (n %% i == 0) {
      return(FALSE)
    }
  }
  return(TRUE)
}

# Function to generate a list of primes in a given range
generate_primes <- function(start, end) {
  primes <- c()
  for (i in start:end) {
    if (is_prime(i)) {
      primes <- c(primes, i)
    }
  }
  return(primes)
}

# Input from the user for the range
start <- as.integer(readline(prompt = "Enter the starting number: "))
end <- as.integer(readline(prompt = "Enter the end of the range: "))

# Generate and display the list of prime numbers
prime_numbers <- generate_primes(start, end)
cat("Prime numbers between", start, "and", end, "are:\n")
cat(prime_numbers, sep = ", ", "\n")
