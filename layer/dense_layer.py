"""
"""

import numpy as np
from ..operation import Operation, WeightMultiply, BiasAdd, Linear, Dropout
from .layer import Layer

class Dense(Layer):
    """
    """
    def __init__(self,
                 neurons: int,
                 activation: Operation = Linear(),
                 conv_in: bool = False,
                 dropout: float = 1.0,
                 weight_init: str = "standard") -> None:
        super().__init__(neurons)
        self.activation = activation
        self.conv_in = conv_in
        self.dropout = dropout
        self.weight_init = weight_init

    def _setup_layer(self, input_: np.ndarray) -> None:
        """
        """
        np.random.seed(self.seed)
        num_in = input_.shape[1]

        if self.weight_init == "glorot":
            scale = 2/(num_in + self.neurons)
        else:
            scale = 1.0

        # weights
        self.params = []
        self.params.append(np.random.normal(loc=0,
                                            scale=scale,
                                            size=(num_in, self.neurons)))

        # bias
        self.params.append(np.random.normal(loc=0,
                                            scale=scale,
                                            size=(1, self.neurons)))

        self.operations = [WeightMultiply(self.params[0]),
                           BiasAdd(self.params[1]),
                           self.activation]

        if self.dropout < 1.0:
            self.operations.append(Dropout(self.dropout))

        return None
