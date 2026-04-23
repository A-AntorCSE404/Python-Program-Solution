def main():

  n = int(input().strip())
  attempts = {}

  for _ in range(n):
      user = input().strip()

      attempts[user] = attempts.get(user, 0) + 1

      if attempts[user] > 3:
          print("BLOCKED", user)
      else:
          print("OK", user, attempts[user])

if __name__=="__main__":
  main()
