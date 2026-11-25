import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Logistic map parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map for dimension-specific scaling
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial potential with varying degrees
        result = np.sum(0.1 * x**6 + 0.3 * x**4 + 0.5 * x**2)
        
        # Chaotic modulation using logistic map sequence
        chaotic_modulation = np.sum(self.chaotic_sequence * np.sin(x))
        result += 0.8 * chaotic_modulation
        
        # Asymmetric saddle points with exponential decay
        for i in range(self.dim):
            saddle_term = np.exp(-0.5 * (x[i] - 1)**2) - np.exp(-0.5 * (x[i] + 1)**2)
            result += 0.3 * saddle_term * (1 + 0.2 * np.sin(3 * x[i]))
            
        # Cross-dimensional coupling with chaotic weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                coupling += weight * np.sin(2 * (x[i]**2 - x[j]**2))
        result += 0.5 * coupling
        
        # Multi-scale oscillatory components
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Varying frequencies
            oscillation += np.sin(freq * x[i]) * np.cos(freq * x[i])
        result += 0.4 * oscillation
        
        # Non-convex penalty with polynomial constraints
        penalty = np.sum((x**3 - 3*x)**2)
        result += 0.2 * penalty
        
        # Fractal-like structure using recursive polynomial terms
        fractal = 0.0
        for i in range(self.dim):
            poly_val = x[i]**5 + 0.5 * x[i]**3 + 0.1 * x[i]
            fractal += np.sin(poly_val) * np.cos(poly_val)
        result += 0.15 * fractal
        
        # Add global optimum bias
        result += 0.05 * np.sum((x - 0.1)**2)
        
        return result