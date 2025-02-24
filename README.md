# Communication Contract
If the server is running, the client can connect to "tcp://localhost:5555" and send it a `JSON` message containing _**tuple(s)**_ of integer data. 

The preconditions are:
  - The tuple must contain only 3 integers, no more and no less
  - The tuple's contents must be in this order: `lower_bound`, `upper_bound`, `count`
  - `lower_bound` must be < `upper_bound` and `count` must be a positive integer
  - REQ must be in `JSON` format (done automatically)

If all preconditions are satisfied, the server will generate a random set of integers per tuple based on the amount in count. 
## For example
If the client sends over a package of:

```python
{
ranges = [
    (2, 5, 1),
    (4, 8, 2),
    (-100, 100, -1)
]
}
```

It could return:

```json
[[5], [7, 8], []]
```

*Note: the last JSON list is empty because '-1' is an invalid count.*

You could then use the received random integer data in any system you were planning to use it for.

## UML Sequence Diagram

![UML](https://github.com/user-attachments/assets/4863aa86-4e08-45b0-b04b-37e776315c65)

