import pytholog

# Step 1: Create a knowledge base
kb = pytholog.KnowledgeBase("family")

# Step 2: Add facts dynamically
kb.assert_fact("parent", "john", "mary")  # john is the parent of mary
kb.assert_fact("parent", "mary", "susan")  # mary is the parent of susan

# Add a rule dynamically
kb.add_clause("grandparent(X, Y)", "parent(X, Z) & parent(Z, Y)")

# Step 3: Query the knowledge base
result = kb.query("grandparent(john, susan)")

# Print the result
print(result)
