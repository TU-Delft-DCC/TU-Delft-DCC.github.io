
### Side effects and external state {.unnumbered}
Side effects refer to observable changes or interactions that a function or expression has on the external world beyond its return value. Non-pure functions are functions that have side effects or rely on external state, making their behavior dependent on factors other than their inputs. 

:::{.callout-tip}
**Pure functions** are **deterministic** and have **no side-effects**.
:::

Instead, non pure functions may

- **modify state outside their scope**, such as changing the value of a global variable, printing to the console, or modifying files
- produce **different results** for the same input depending on the state of external (global) variables or resources
- use random number generation and are thus **non-deterministic**
- **read input** from the user or write output to a display
- interact with databases, APIs, or other **external services**


:::{.callout-note appearance="simple"} 
## Solution

Ensure that each function or module has a single responsibility. Break down complex functions into smaller, focused functions that perform specific tasks. This helps in isolating non-pure functions with side effects from pure functions.

![*CC-BY-4.0 CodeRefinery*](https://raw.githubusercontent.com/coderefinery/modular-code-development/61517f7f01a0ff49c441f7dee731be4f6799ec03/img/good-vs-bad.svg)
:::