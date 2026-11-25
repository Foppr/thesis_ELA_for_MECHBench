import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly chaotic sinusoidal components with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sin(11 * x[i]) * np.cos(8 * x[j]) * np.sin(4 * (x[i] + x[j]))
        
        # Add enhanced saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.5 * x[i]**5 - 0.9 * x[i]**4 + 0.6 * x[i]**3 - 0.2 * x[i]**2
        
        # Add stronger non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.8 * np.sin(18 * sum_x) * np.cos(15 * sum_x)
        
        # Add global minimum penalty with exponential scaling
        result += 0.15 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Add asymmetric cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[j]) * np.tan(0.6 * (x[i] - x[j]))
        
        # Add additional chaotic component with dynamic frequency (mutated)
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(5 * x[i] + 0.6 * np.sin(x[i]))
        
        # Add a new twist: perturbed harmonic interactions
        for i in range(self.dim):
            result += 0.3 * np.sin(9 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i]**2)
        
        # Add a novel term: multi-scale chaotic modulation
        for i in range(self.dim):
            result += 0.25 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.tan(0.4 * x[i])
        
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.18 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j]))
        
        # Add a new global structure: nested saddle points with varying depths
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.4 * x[i]**6 - 0.8 * x[i]**5 + 0.5 * x[i]**4 - 0.3 * x[i]**3
        result += nested_term
        
        return result