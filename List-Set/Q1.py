allowed   = {"10.0.0.1","10.0.0.2","192.168.1.5"}
attempted = {"10.0.0.1","172.16.0.9","192.168.1.5","45.33.32.156"}

unauthorized = attempted - allowed
all_safe     = attempted.issubset(allowed)

print("Unauthorized IPs:", unauthorized)
print("All logins safe :", all_safe)
for ip in sorted(unauthorized):
    print(f"  [ALERT] Unauthorized access from {ip}")
