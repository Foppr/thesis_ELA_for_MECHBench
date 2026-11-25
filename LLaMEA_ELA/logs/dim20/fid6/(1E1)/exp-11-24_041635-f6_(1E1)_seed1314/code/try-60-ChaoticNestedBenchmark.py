import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.cos(7.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with prime frequency ratios and dynamic amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 3.14159
            amp = 1.0 / ((i + 1) ** 1.5)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.sin(0.7 * x[i])
        
        # Enhanced cross-dimensional coupling with chaotic phase interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.8 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Polynomial and exponential components with harmonic interference
        poly_term = np.sum(x**4) * np.cos(0.3 * r)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.15 * r) * np.cos(0.2 * r)
        
        # Additional chaotic harmonic interference
        harm_interf = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harm_interf += 0.3 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
        
        # Final chaotic combination with dynamic scaling
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + harm_interf
        
        return result