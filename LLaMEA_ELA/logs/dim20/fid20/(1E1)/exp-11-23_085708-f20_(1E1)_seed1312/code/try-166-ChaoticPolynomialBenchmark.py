import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component for non-linearity
        tent = 0.0
        a = 1.5
        for i in range(self.dim):
            tent += np.abs(2 * a * x_scaled[i] - a) if x_scaled[i] < 0.5 else np.abs(2 * a * (1 - x_scaled[i]) - a)
        
        # Polynomial interaction terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**3 + x[j]**2) * (x[i] * x[j])**2 * (i + j + 1)
                
        # Fractal-like gradient modulation using fractional powers
        frac_grad = 1.0
        for i in range(self.dim):
            frac_grad *= (1 + 0.3 * np.abs(x[i])**0.7 + 0.2 * np.sin(x[i]**1.3))
            
        # Multi-scale sinusoidal component with varying frequencies
        multi_freq = 0.0
        for i in range(self.dim):
            multi_freq += (np.sin(2 * x[i]) + 
                          0.5 * np.sin(5 * x[i]) + 
                          0.3 * np.sin(10 * x[i]) +
                          0.1 * np.sin(15 * x[i]))
            
        # Cross-dimensional coupling with chaotic feedback
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += (np.tanh(x[i] * x[j]) + 
                               0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])) * (i + j + 1)
        
        # Add a non-smooth component with absolute value and step-like behavior
        smoothness = 0.0
        for i in range(self.dim):
            smoothness += np.abs(np.sin(x[i])) * np.exp(-np.abs(x[i]))
            
        # Combine all terms with different weights
        return tent + poly_term + frac_grad * multi_freq + coupling + smoothness + 3.0