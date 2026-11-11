# Topic 1 - Functions
def greet(name):
    return f"Hey, {name}"

result = greet("Tajammul")
print(result)


def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(100, 5)

print(result)
# Execution Flow
# Function definition -> calculate_total(price, quantity) Python creates a function object and binds it to the name.
# Function invocation -> calculate_total(100, 5) Arguments are bound to parameters.
# Function execution -> total = 100 * 5 The function executes its statements.
# Return value -> 500 The returned value is assigned to result.

# Topic 2 - Positional and keyword arguments
# Positional arguments (Values are assigned based on their position)

def create_embedding(text, model):
    print(f"Text: {text}")
    print(f"Model: {model}")

create_embedding("Hello AI", "text-embedding-3-small")

# Keyword arguments (Values are assigned using parameter names)
create_embedding(model="text-embedding-3-small", text="Hello AI")

# Topic 3 - Default arguments
def generate_response(
    prompt,
    model="gpt-model",
    temperature=0.7
):
    print(f"Prompt: {prompt}")
    print(f"Model: {model}")
    print(f"Temperature: {temperature}")

def add_message(message, history=[]):       # Important internal behaviour: Mutable default arguments
    history.append(message)                 # Python evaluates default argument expressions once, when the function is defined, not every time the function is called.
    return history

print(add_message("Hello"))
print(add_message("How are you?"))
print(add_message("Good morning"))

# Topic 4 - *args and **kwargs
# *args - Variable positional arguments (The *args syntax collects additional positional arguments into a tuple)
def calculate_total(*args):
    print(args)
    print(type(args))

    return sum(args)

print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, 40, 50))

# **kwargs - Variable keyword arguments (**kwargs collects additional keyword arguments into a dictionary.)
def configure_model(**kwargs):
    print(kwargs)
    print(type(kwargs))

configure_model(
    model="gpt-model",
    temperature=0.7,
    max_tokens=1000,
    streaming=True
)

# Argument unpacking – The reverse operation (Here, *numbers unpacks the list into three positional arguments.)
# def sum(a,b,c):
#     return a+b+c
# numbers = [1,2,3]
# print(sum(*numbers))

# Topic 5 - Lambda functions
square = lambda x: x * x        # Equivalent to JS const square = x => x*x;
print(square(5))

# Topic 6 - How Python passes arguments
def modify_list(items):
    items.append(100)

numbers = [10, 20, 30]
modify_list(numbers)
print(numbers)




################################# TEST1 #################################
def calculate_token_cost(input_tokens, output_tokens, input_cost_per_token, output_cost_per_token):
    return input_tokens * input_cost_per_token + output_tokens * output_cost_per_token

print(calculate_token_cost(1000, 500, 0.000002, 0.000006))


################################# TEST2 #################################
def create_embedding(text, model, dimensions):
    pass

create_embedding("hi", "opus", 2)
create_embedding(model="opus", dimensions=2, text="hi")
create_embedding("hi", dimensions=2, model="opus")

################################# TEST3 #################################
def generate_response(
    prompt,
    model="gpt-model",
    temperature=0.7,
    max_tokens=1000
):
    pass

generate_response("test prompt")
generate_response("test prompt", "gpt-model2")
generate_response("test prompt", temperature=1, max_tokens=3000)
generate_response(prompt="test prompt", model="gpt-model1", temperature=1, max_tokens=3000)


################################# TEST4 #################################
def calculate_average(*nums):
    print(sum(nums)/len(nums))

calculate_average(10, 20, 30)
calculate_average(10, 20, 30, 40, 50)

################################# TEST5 #################################
def llm_configurator(**kwargs):
    for key, value in kwargs.items():
        print(value)

llm_configurator(
    provider="openai",
    model="gpt-model",
    temperature=0.7,
    streaming=True,
    max_tokens=2000
)

################################# TEST6 #################################
def create_agent(name, *tools, **config):
    print(name)
    for tool in tools:
        print(tool)

    for key, value in config.items():
        print(value)

    return {
        "name": name,
        "tools": tools,
        "config": config
    }

create_agent(
    "Research Agent",
    "web_search",
    "calculator",
    model="gpt-model",
    temperature=0.5,
    memory=True
)


################################# TEST7 #################################
def add_message(message, history=[]):
    history.append(message)
    return history

print(add_message("Hello"))
print(add_message("Python"))
print(add_message("AI Engineering"))