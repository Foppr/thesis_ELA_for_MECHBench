import numpy as np

class ExponentialSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with significant elliptical distortion and higher-order polynomial
        result = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4) + 0.02 * np.sum(x**6)
        
        # Multi-scale exponentially decaying sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            amplitude = 3.0 / (i + 1)**1.8
            freq1 = 3.0 * (i + 1)
            freq2 = 4.0 * (i + 1)
            result += amplitude * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
        # Adaptive cross-dimensional interaction terms with distance-dependent strengths and enhanced modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(i - j)
                strength = 1.5 / (dist**1.5 + 1.0)
                freq = 1.5 + 0.8 * dist
                result += strength * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
                
        # Novel hybrid potential energy components with sharp ridges and valleys, enhanced with additional sinusoidal modulations
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += np.exp(-0.15 * abs(x[i])) * np.sin(7.0 * x[i]) + 0.2 * np.sin(12.0 * x[i])
        result += 0.4 * ridge_term
        
        # Additional global convergence term with multiple exponential decay rates and enhanced nonlinearity
        result += 0.3 * np.exp(-0.4 * np.sum(x**2)) + 0.2 * np.exp(-0.8 * np.sum(x**4)) + 0.1 * np.exp(-1.0 * np.sum(x**6))
        
        # Introduce a more complex perturbation to create even more challenging local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(15.0 * x[i]) * np.cos(11.0 * x[i]) + 0.08 * np.sin(20.0 * x[i])
            
        return result