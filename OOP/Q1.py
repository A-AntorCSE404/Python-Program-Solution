from abc import ABC, abstractmethod
import datetime

# ── ABSTRACTION: defines the contract ──────────────────────────
class BankAccount(ABC):

    def __init__(self, owner: str, account_no: str, pin: str):
        # ── ENCAPSULATION: all sensitive data is private ───────────
        self.__owner      = owner
        self.__account_no = account_no
        self.__pin        = pin
        self.__balance    = 0
        self.__history    = []

    # ── Getters (controlled read access) ──────────────────────
    def get_balance(self):
        return self.__balance

    def get_account_no(self):
        return f"****{self.__account_no[-4:]}"   # masked

    def get_history(self):
        return list(self.__history)             # copy, not reference

    # ── Protected balance mutator (used by subclasses) ─────────
    def _set_balance(self, amount):
        self.__balance = amount

    def _log(self, msg):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self.__history.append(f"[{ts}] {msg}")

    def account_info(self):      # shared inherited method
        return (f"Owner : {self.__owner}\n"
                f"Acct  : {self.get_account_no()}\n"
                f"Type  : {type(self).__name__}\n"
                f"Bal   : ৳{self.__balance:,.2f}")

    # ── ABSTRACTION: subclasses MUST implement these ───────────
    @abstractmethod
    def deposit(self, amount): 
      pass

    @abstractmethod
    def withdraw(self, amount): 
      pass

    @abstractmethod
    def calculate_interest(self): 
      pass


# ── INHERITANCE: inherits BankAccount ──────────────────────────
class SavingsAccount(BankAccount):
    MIN_BALANCE  = 1000
    INTEREST_RATE = 0.04   # 4% per year

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
          
        self._set_balance(self.get_balance() + amount)
        self._log(f"Deposited ৳{amount:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
          
        if self.get_balance() - amount < self.MIN_BALANCE:
            raise ValueError(f"Must keep min ৳{self.MIN_BALANCE}.")
          
        self._set_balance(self.get_balance() - amount)
        self._log(f"Withdrew ৳{amount:,.2f}")

    # ── POLYMORPHISM: own version of calculate_interest ────────
    def calculate_interest(self):
        interest = self.get_balance() * self.INTEREST_RATE
      
        self._set_balance(self.get_balance() + interest)
      
        self._log(f"Interest credited ৳{interest:,.2f} (4%)")
        return interest





class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Must be positive.")
          
        self._set_balance(self.get_balance() + amount)
        self._log(f"Deposited ৳{amount:,.2f}")

    def withdraw(self, amount):
        if self.get_balance() - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError("Overdraft limit exceeded.")
          
        self._set_balance(self.get_balance() - amount)
        self._log(f"Withdrew ৳{amount:,.2f}")

    # ── POLYMORPHISM: current accounts earn no interest ────────
    def calculate_interest(self):
        self._log("No interest for CurrentAccount.")
        return 0


class MaturityError(Exception):  # custom exception
  pass   

class FixedDepositAccount(BankAccount):
    INTEREST_RATE = 0.08   # 8% per year

    def __init__(self, owner, account_no, pin, maturity_date):
        super().__init__(owner, account_no, pin)
        self.maturity_date = maturity_date   # datetime.date object

    def deposit(self, amount):
        if amount <= 0: 
          raise ValueError("Must be positive.")
          
        self._set_balance(self.get_balance() + amount)
        self._log(f"Deposited ৳{amount:,.2f}")

    def withdraw(self, amount):
        if datetime.date.today() < self.maturity_date:
            raise MaturityError(
                f"Locked until {self.maturity_date}.")
          
        self._set_balance(self.get_balance() - amount)
        self._log(f"Withdrew ৳{amount:,.2f}")

    # ── POLYMORPHISM: highest interest rate ────────────────────
    def calculate_interest(self):
        interest = self.get_balance() * self.INTEREST_RATE
      
        self._set_balance(self.get_balance() + interest)
        self._log(f"Interest credited ৳{interest:,.2f} (8%)")
        return interest


# ── POLYMORPHISM: works for ALL account types ──────────────────
def process_month_end(accounts: list):
  
    print("─── Month-End Interest Processing ───")
    for acc in accounts:
        earned = acc.calculate_interest()   # each type responds differently
        print(f"  {type(acc).__name__:<20} → ৳{earned:,.2f}")


# ─── Demo ──────────────────────────────────────────────────────
savings = SavingsAccount("Rahim",   "ACC001", "1234")
current = CurrentAccount("Karim",   "ACC002", "5678")
fixed   = FixedDepositAccount("Salam", "ACC003", "9999",
            datetime.date(2026, 12, 31))

savings.deposit(50000)
current.deposit(20000)
fixed.deposit(100000)

process_month_end([savings, current, fixed])

# Encapsulation proof
try:
    print(savings.__balance)       # → AttributeError ✗
except AttributeError as e:
    print(f"Blocked: {e}")

# Abstraction proof
try:
    BankAccount("x","y","z")        # → TypeError ✗
except TypeError as e:
    print(f"Blocked: {e}")
