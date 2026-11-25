import numpy as np

class ExponentialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.1 * r) * np.cos(2 * np.pi * r)
        
        # Polynomial valley component
        polynomial = 0.5 * np.sum(x**4) - 2.0 * np.sum(x**2)
        
        # Add multiple exponential peaks to create multimodality
        peaks = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                peaks += np.exp(-0.5 * ((x[i] - 1)**2 + (x[j] + 1)**2)) + \
                         np.exp(-0.3 * ((x[i] + 2)**2 + (x[j] - 2)**2))
        
        # Add a sinusoidal modulation to the radial component
        modulation = 0.3 * np.sin(3 * r) * np.cos(5 * r)
        
        # Add cubic terms for additional complexity
        cubic = 0.1 * np.sum(x**3)
        
        return radial + polynomial + peaks + modulation + cubic