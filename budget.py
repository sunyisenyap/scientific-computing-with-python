class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        # Title line: 30 characters, centered with *
        title = f"{self.name:*^30}"
        lines = [title]
        
        # Ledger items
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"[:7]
            lines.append(f"{desc:<23}{amt:>7}")
            
        # Total line
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)
        
        return "\n".join(lines)


def create_spend_chart(categories):
    spent = {}
    total_spent = 0
    
    # 1. Hitung total pengeluaran (withdrawal) per kategori dan total keseluruhan
    for cat in categories:
        cat_spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent[cat.name] = -cat_spent
        total_spent += spent[cat.name]
        
    # 2. Hitung persentase (dibulatkan ke bawah ke puluhan terdekat)
    percentages = {}
    for cat in categories:
        if total_spent == 0:
            percentages[cat.name] = 0
        else:
            percentages[cat.name] = int((spent[cat.name] / total_spent) * 100) // 10 * 10
            
    # 3. Buat grafik (Bar Chart)
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for cat in categories:
            if percentages[cat.name] >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"
        
    # 4. Garis horizontal bawah (jumlah strip = (jumlah kategori * 3) + 1)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # 5. Nama kategori vertikal di bawah
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line + "\n"
        
    # Hapus newline (\n) di paling akhir sesuai instruksi tes
    return chart.rstrip("\n")