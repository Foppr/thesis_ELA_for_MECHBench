import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with non-linear frequency modulation
        sinusoidal = 0
        for i in range(self.dim):
            freq = (i + 1) * (1.0 + 0.5 * np.sin(0.3 * i))
            sinusoidal += np.sin(freq * x[i]) * np.cos(freq * x[i] / 1.7)
        
        # Higher-order polynomial interactions with chaotic coefficients
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.3 * np.sin(i * j * 0.5)
                polynomial += coeff * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Dynamic exponential barriers with dimension-dependent parameters
        barriers = 0
        for i in range(self.dim):
            barrier1 = np.exp(-0.3 * (x[i] - 2.5)**2) + np.exp(-0.3 * (x[i] + 2.5)**2)
            barrier2 = 0.15 * np.abs(x[i])**1.7
            barriers += barrier1 + barrier2
        
        # Fractal-like ruggedness with recursive sinusoidal perturbations
        ruggedness = 0
        for i in range(self.dim):
            ruggedness += np.sin(20 * x[i]) * np.cos(25 * x[i]) * np.sin(30 * x[i])
        
        # Additional chaotic coupling between dimensions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for scalability
                coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (i + j)
        
        # Combine all components with increased complexity and scaling
        return 5 * sinusoidal + 3 * polynomial + 2 * barriers + 1.2 * ruggedness + 0.8 * coupling + 15 * self.dim