import numpy as np

class ExponentialSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with slight elliptical distortion
        result = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Multi-scale exponentially decaying sinusoidal perturbations with varying frequencies
        for i in range(self.dim):
            amplitude = 2.0 / (i + 1)**1.5
            freq1 = 2.0 * (i + 1)
            freq2 = 3.0 * (i + 1)
            result += amplitude * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
        # Adaptive cross-dimensional interaction terms with distance-dependent strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based adaptive decay and frequency modulation
                dist = abs(i - j)
                strength = 1.0 / (dist**1.2 + 1.0)
                freq = 1.0 + 0.5 * dist
                result += strength * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
                
        # Novel hybrid potential energy components with sharp ridges and valleys
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += np.exp(-0.1 * abs(x[i])) * np.sin(5.0 * x[i])
        result += 0.3 * ridge_term
        
        # Additional global convergence term with multiple exponential decay rates
        result += 0.2 * np.exp(-0.3 * np.sum(x**2)) + 0.1 * np.exp(-0.7 * np.sum(x**4))
        
        # Introduce a small perturbation to create more complex local minima
        for i in range(self.dim):
            result += 0.05 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Add a new component to enhance multimodality and challenge
        correlation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlation_term += (x[i] * x[j]) / (1.0 + abs(x[i] - x[j])**2)
        result += 0.15 * correlation_term
        
        # Add a periodic component with varying frequency across dimensions
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2.0 * np.pi * x[i] / (i + 1)) * np.cos(3.0 * np.pi * x[i] / (i + 1))
        result += 0.25 * periodic_term
        
        return result