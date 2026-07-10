# | Greedy  | Lazy     |
# | ------- | -------- |
# | `*`     | `*?`     |
# | `+`     | `+?`     |
# | `?`     | `??`     |
# | `{m,n}` | `{m,n}?` |

# The extra changes the strategy
# Instead of:
# Match as much as possible
# it becomes:
# Match as little as possible while still allowing the overall pattern to succeed
