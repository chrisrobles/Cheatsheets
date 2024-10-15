# System Design

## Serverless


Cloud computing execution model where the cloud provider (e.g., DigitalOcean, AWS) automatically handles the allocation and provisioning of servers.

"Pay as you go"

Provisioning
: Process of setting up and configuring the necessary resources (servers, storage, networking components, etc.)

## Vertical vs Horizontal Scaling

### Horizontal Scaling (Scaling Out)

Definition:
- Adding more machines or nodes to your system.

Example:
- Adding more servers to handle increased load.

Advantages:
- Improved fault tolerance and redundancy.
- Easier to scale incrementally.
- Can handle more concurrent users.

Disadvantages:
- More complex to manage and maintain.
- Requires load balancing.
- Potentially higher network latency.

### Vertical Scaling (Scaling Up)

Definition: 
- Adding more power (CPU, RAM, storage) to an existing machine.

Example: 
- Upgrading the hardware of a single server.

Advantages:
- Simpler to implement and manage.
- No need for load balancing.
- Lower network latency.

Disadvantages:
- Limited by the capacity of a single machine.
- Potentially higher cost for high-end hardware.
- Single point of failure.

