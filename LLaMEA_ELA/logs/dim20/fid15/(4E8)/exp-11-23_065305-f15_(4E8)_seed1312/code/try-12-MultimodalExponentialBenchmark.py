import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Quadratic radial term - global minimum at origin
        quadratic = 0.01 * np.sum(x**2)
        
        # Exponentially decaying sinusoidal terms creating many local minima
        sinusoidal = 0
        for i in range(self.dim):
            # Use exponential decay with increasing frequency
            freq = 2**(i+1)
            decay = np.exp(-0.1 * i)
            sinusoidal += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        # Interaction terms between dimensions with exponential weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.05 * (i + j))
                interaction += weight * np.sin(x[i]) * np.cos(x[j])
        
        # Add a global scaling factor to control the landscape complexity
        return quadratic + sinusoidal + 0.1 * interaction