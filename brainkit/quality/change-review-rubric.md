# Change Review Rubric

This rubric defines how changes proposed by Synthetic Intelligence, swarm agents, or higher-order automation should be reviewed.

## Review Goals

A good review checks more than correctness. It should also check:

- lane fit
- business value
- governance fit
- quality impact
- rollback awareness
- clarity for future operators

---

## Review Dimensions

### 1. Purpose Fit
Does the change clearly support the repo’s role and current mission?

### 2. Lane Fit
Does the change belong in this lane, or should it be routed elsewhere?

### 3. Quality Impact
Does it improve or degrade clarity, maintainability, testing, or reliability?

### 4. Risk Impact
Does it touch protected paths, payment logic, approvals, or public trust surfaces?

### 5. Viability Impact
Does it support direct revenue, supporting value, platform value, or knowledge-product value?

### 6. Reversibility
Can the change be rolled back or corrected without confusion?

### 7. Traceability
Can reviewers identify the mission, task, or event that caused the change?

---

## Suggested Ratings

- strong
- acceptable
- weak
- blocked

Any blocked rating in risk or lane fit should pause autonomous application.

---

## Best Practices

- review for system fit, not only local correctness
- use higher scrutiny for cross-lane changes
- do not treat documentation as low-value; docs affect operations
- require higher confidence for public or monetized flows

---

## Rule of thumb

A good review asks not just “does this work?” but also “does this belong here, at this time, in this form?”
