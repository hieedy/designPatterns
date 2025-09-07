from copy import  deepcopy, copy




class Task:
    def __init__(self, name, timeout=5, config=None):
        self.timeout = timeout
        self.name = name
        self.config = config


class EmailTask(Task):

    def __init__(self):
        super().__init__(
            'Email'
        )


class ApprovalTask(Task):

    def __init__(self):
        super().__init__(
            'Approval'
        )


class ValidationTask(Task):

    def __init__(self):
        super().__init__(
            'Validation'
        )


class CloneObjectMixin:

    def clone(self, *, deep=False):
        return deepcopy(self) if deep else copy(self)


class WorkFlow(CloneObjectMixin):

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks


class WorkflowRegistry:
    _workflows = {}

    @classmethod
    def register(cls, name, obj):
        if name in cls._workflows:
            raise ValueError(f'prootype with the name {name} is already registered')
        cls._workflows[name] = obj

    @classmethod
    def get_prototype(cls, name) -> WorkFlow:
        if name in cls._workflows:
            return cls._workflows[name].clone(deep=True) #important step


if __name__ == '__main__':
    wf = WorkFlow()
    wf.add_task(EmailTask())
    wf.add_task(ApprovalTask())
    wf.add_task(EmailTask())

    WorkflowRegistry.register('onboarding',wf)

    # now use the protoype and clone it and then can modify it
    # client code will looks like
    fast_onboarding = WorkflowRegistry.get_prototype(
        'onboarding'
    )

