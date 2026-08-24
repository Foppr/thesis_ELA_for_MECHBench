import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like frequency patterns
        self.freq_pattern = np.power(2.0, np.arange(dim)) * 0.5
        # Precompute amplitude multipliers
        self.amp_pattern = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / 4.0)
        # Precompute chaotic shift values
        self.shift_pattern = np.sin(np.arange(dim) * np.pi / 3.0) * 0.8 + 0.2
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Fractal-like nested sinusoidal components
        for i in range(self.dim):
            freq = self.freq_pattern[i]
            amp = self.amp_pattern[i]
            phase = self.shift_pattern[i] * np.pi
            result += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.5)
            
        # Add polynomial interaction terms with varying degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.1 * (x[i]**3 + x[j]**3) * np.sin(2.0 * (x[i] - x[j]))
                result += interaction
                
        # Add nested multi-scale sinusoidal components
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(x[i] * 0.5)
            result += 0.3 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.7) * np.sin(x[i] * 0.3)
            
        # Add global shift with fractal scaling
        shift = np.array([self.shift_pattern[i] * np.sin(self.shift_pattern[i] * np.pi) * 2.0 for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add chaotic perturbation with dimension-dependent frequency
        perturbation = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * self.shift_pattern[i]
            perturbation += 0.05 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        result += perturbation
        
        # Add high-order polynomial terms for increased complexity
        result += 0.001 * np.sum(x**4) + 0.0005 * np.sum(x**6) + 0.0001 * np.sum(x**8)
        
        return result