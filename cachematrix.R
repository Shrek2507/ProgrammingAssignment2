## Put comments here that give an overall description of what your
## functions do

## This function creates a special object called "matrix" that can cache its inverse.

makeCacheMatrix <- function(x = matrix()) {
  inverse_of_matrix <- NULL
  set <- function(b) {
    x <<- b
    inverse_of_matrix <<- NULL
  }
  get <- function() x
  set_inverse_value <- function(inverse_value) inverse_of_matrix <<- inverse_value
  get_inverse_value <- function() inverse_of_matrix
  list(set = set, get = get, set_inverse_value = set_inverse_value, get_inverse_value = get_inverse_value)
}


## Computes the inverse of matrix if it is not already cached. If it exists then it caches it.

cacheSolve <- function(x, ...) {
  ## Return a matrix that is the inverse of 'x'
  inverse_of_matrix <- x$get_inverse_value()
  if (!is.null(inverse_of_matrix)) {
    message("getting cached data")
    return(inverse_of_matrix)
  }
  mat <- x$get()
  inverse_of_matrix <- solve(mat, ...)
  x$set_inverse_value(inverse_of_matrix)
  inverse_of_matrix
}
