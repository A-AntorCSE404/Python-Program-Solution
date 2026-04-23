
def main():
  
  # take user input
  n = int(input().strip())

  # dictionary 
  freq = {}
  
  for _ in range(n):

    # take ip address from the user
      ip = input().strip()
      freq[ip] = freq.get(ip, 0) + 1
  
  top_ip = None
  top_count = -1
  
  for ip, count in freq.items():
      if count > top_count or (count == top_count and ip < top_ip):
          top_ip = ip
          top_count = count
  
  print(top_ip, top_count)

# Program Entry point
if __name__=="__main__":
  main()
