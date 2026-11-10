# Topic 1
message = "Hi, welcome to AI Engineering Learnings"
print(message)

# Topic 2 - Data types (int, float, str, bool, None, list, tuple, dict, set)
value = 100
print(type(value))

value = "Hello"
print(type(value))

# Topic 3 - Mutable (list,  dict, set) vs Immutable (int, float, str, bool, tuple) objects 
# Immutable
name = "Python"
name = name + " AI"
print(name)

# Mutable
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# Topic 4 - Python collections ( List, Tuples, Sets, Dictionaries)
# Lists - Ordered & Mutable
messages = ["Hi", "Hello", "How are you"]
messages.append("Good evening")
messages.remove("Hi")
print(messages)

#Tuples - Ordered & Immutable (Useful for fixed collections of values that should not be modified)
coordinates = (12.97, 77.59)

latitude = coordinates[0]
longitude = coordinates[1]
print(latitude, longitude)

#Sets - Unordered collections of unique elements (Useful for removing duplicate IDs, finding unique categories and performing set operations)
document_ids = {104, 102, 101, 103, 101}
print(document_ids)

#Dictionaries - Key-value Ordered & Mutable data structures 
user = {
    "name": "John",
    "role": "developer",
    "experience": 5,
    "skills": ["Python", "Node.js", "MongoDB"]
}
print(user["name"])
print(user)
user["role"] = "AI Engineer"
user["location"] = "Bangalore"
print(user)


################################# Shallow copy vs Deep copy #################################
import copy

original = {
    "model": "gpt-model",
    "settings": {
        "temperature": 0.7
    }
}

shallow = original.copy()
deep = copy.deepcopy(original)

shallow["settings"]["temperature"] = 0.2
deep["settings"]["temperature"] = 0.5




################################# TEST1 #################################
app_name = "Claude"
model_name = "Opus"
temperature = 1
max_tokens = 100000
streaming_enabled = False
response = {
    "success": True 
}

print(app_name, model_name, temperature, max_tokens, streaming_enabled, response)
print(type(app_name), type(model_name), type(temperature), type(max_tokens), type(streaming_enabled), type(response))


################################# TEST2 #################################
first = [10, 20, 30]
second = first

second.append(40)

print(first)
print(second)
print(first is second)

################################# TEST3 #################################
ai_models = ["opus1", "opus2", "opus3", "opus4", "opus5"]
ai_models.append("opus6")
ai_models.remove("opus3")
print(len(ai_models))
ai_models_set = set(ai_models)

################################# TEST4 #################################
llm_config = {
    "provider": "openai",
    "model": "gpt-model",
    "temperature": 0.7,
    "max_tokens": 1000,
    "streaming": True
}
print(llm_config["provider"])
llm_config["temperature"] = 0.3
llm_config["timeout"] = 30
llm_config["supported_features"] = ["streaming", "function_calling", "vision"]
for k,v in llm_config.items():
    print(f"{k}: {v}")
print("model" in llm_config)

################################# TEST5 #################################
conversation = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a programming language."
    }
]
conversation.append({"role": "user", "content":"just an addition"})
conversation.append({"role": "assistant", "content": "assistants response"})
print(len(conversation))
for conv in conversation:
    if conv["role"] == "user":
        print(conv["content"])
unique_roles = set()
for conv in conversation:
    unique_roles.add(conv["role"])
print(unique_roles)
