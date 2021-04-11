def input_matrix():
  print("Enter four floating point numbers:")
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  pass

def inverse(M):        
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  pass

def matmul(M1, M2):
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  pass

def almost_identity(M, epsilon):
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################    
  pass



def main():
  M = input_matrix()
  print("Matrix M in row order form:")
  print(M)
  M_inv = inverse(M)
  print("Inverse of matrix M in row order form")
  print(M_inv)
  identity = matmul(M, M_inv)
  print("Result of multiplying M with its inverse in row order form:")
  print(identity)
  almost_identity(identity, 1e-4)



if __name__ == "__main__":
  main()