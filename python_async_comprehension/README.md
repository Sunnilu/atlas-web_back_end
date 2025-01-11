How to write an asynchronous generator
How to use async comprehensions
How to type-annotate generators

The function async_generator is annotated with Generator[float, None, None], indicating it yields float values and doesn't take input or return any result.
The first type (float) indicates the type of value the generator will yield.
The second None indicates the type of value that the generator will receive (in this case, it doesn't receive any input).
The final None indicates the type of value the generator returns when it finishes (again, it doesn't return anything in this case).