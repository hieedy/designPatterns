You’re building a workflow engine (like approvals, onboarding, or data pipelines).

- Each workflow is made up of multiple tasks (e.g., SendEmailTask, ApprovalTask, ValidationTask).

- Users often need to create new workflows that are slightly different from existing ones.

    - **Example**: HR Onboarding workflow is 10 steps. Another team wants the same workflow but with only 8 steps and a different notification template.

- Creating each workflow from scratch is tedious and error-prone.

👉 You want to use the Prototype Pattern so that:

You store a few workflow prototypes in a registry.

- Users can clone a prototype workflow and tweak only what’s different (e.g., change one task, remove another).



## Your Practice Challenge

1. Implement the following classes:

   - Task (base class for tasks, with attributes like name, config). 
   - Subclasses: SendEmailTask, ApprovalTask, ValidationTask.
   - Workflow (contains list of tasks, supports clone()). 
   - WorkflowRegistry (keeps named prototypes).

2. Steps:
   - Create a prototype onboarding workflow with 3–4 tasks. 
   - Register it as "onboarding". 
   - Clone it to make a "fast_onboarding" workflow (remove one task, tweak config). 
   - Clone again to make a "secure_onboarding" workflow (add an extra approval).

3. Print out the workflows to confirm each clone is **independent** (changes in one clone should not affect the prototype).
