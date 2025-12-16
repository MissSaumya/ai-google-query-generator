from src.query_engine import SearchQueryGenerator

# Initialize
bot = SearchQueryGenerator()

# Test
print("Testing connection...")
result = bot.generate_queries("How to bake a cake without eggs")
print(result)