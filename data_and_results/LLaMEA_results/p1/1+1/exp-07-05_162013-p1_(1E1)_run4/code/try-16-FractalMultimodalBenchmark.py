import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal constants
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 0.3
        self.fractal_sequence = self._generate_fractal_sequence()
        
    def _generate_fractal_sequence(self):
        # Generate a fractal-like sequence using power-law distribution
        seq = np.zeros(self.dim)
        for i in range(self.dim):
            seq[i] = (i + 1) ** (-self.alpha)
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Power-law interaction component
        for i in range(self.dim):
            result += self.fractal_sequence[i] * (x[i]**self.beta)
            
        # Multi-scale harmonic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = self.fractal_sequence[i] * self.fractal_sequence[j]
                result += scale_factor * np.sin(self.gamma * x[i] * x[j])
                
        # Discrete dynamical system component
        for i in range(self.dim):
            result += 0.1 * np.sin(x[i]) * np.cos(2 * x[i])
            
        # Ruggedness via fractional Brownian motion approximation
        for i in range(self.dim):
            result += 0.05 * np.sin(10 * x[i] * self.fractal_sequence[i]) * np.cos(5 * x[i])
            
        # Global scaling and bias
        result += 0.2 * np.sum(np.abs(x)**(1 + self.alpha))
        
        # Add a small perturbation to avoid trivial optima
        result += 0.01 * np.sum(x**4)
        
        return result