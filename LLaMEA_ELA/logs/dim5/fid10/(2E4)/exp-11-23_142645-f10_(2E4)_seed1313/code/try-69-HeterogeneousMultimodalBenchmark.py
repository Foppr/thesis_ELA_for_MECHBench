import numpy as np

class HeterogeneousMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees and cross-terms
        polynomial = np.sum(0.3 * x**2 + 0.1 * x**3 + 0.02 * x**4 + 0.005 * x**5)
        
        # Trigonometric mixture with varying frequencies and phases
        trigonometric = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) + 
                               np.sin(5.0 * x) * np.cos(7.0 * x) + 
                               np.sin(4.0 * x) * np.cos(6.0 * x))
        
        # Exponential interaction terms with adaptive scaling
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                scale = 1.0 + 0.5 * np.sin(0.3 * (i + j))
                exponential += scale * np.exp(-0.5 * dist**2) * np.cos(2.0 * dist)
        
        # Adaptive noise component with dynamic amplitude
        noise_amp = 0.1 + 0.05 * np.sin(np.sum(x) * 0.1)
        noise = np.random.normal(0, noise_amp, self.dim)
        noise_component = np.sum(noise**2)
        
        # Dynamic conditioning based on problem dimensionality
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combined fitness with weighted components
        return (condition_factor * (polynomial + trigonometric + exponential) + 
                0.3 * noise_component + 
                0.5 * np.sum(np.abs(x)**3))