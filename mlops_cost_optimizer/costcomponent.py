from abc import ABC, abstractmethod

class CostComponent(ABC):
    """The CostComponent class is a simple abstract base class specifying
    an interface method ("evaluate") used to calculate the cost.
    """
    
    @abstractmethod
    def evaluate(self, scenario_params: dict = None) -> float:
        """Evaluates the cost of this component.
        Args:
            scenario_params (dict): A dictionary of scenario values that
                can be used to evaluate the cost. Default value is None.
        Returns:
            float - the evaluated cost.
        """
    