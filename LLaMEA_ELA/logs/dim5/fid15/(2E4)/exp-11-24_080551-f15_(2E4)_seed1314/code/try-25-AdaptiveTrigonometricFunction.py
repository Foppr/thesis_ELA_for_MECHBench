import numpy as np

class AdaptiveTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with significant elliptical distortion and higher-order polynomial
        result = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4) + 0.02 * np.sum(x**6)
        
        # Multi-scale exponentially decaying sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            amplitude = 2.5 / (i + 1)**1.7
            freq1 = 2.5 * (i + 1)
            freq2 = 3.5 * (i + 1)
            result += amplitude * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
        # Adaptive cross-dimensional interaction terms with distance-dependent strengths and enhanced modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(i - j)
                strength = 1.2 / (dist**1.3 + 1.0)
                freq = 1.2 + 0.7 * dist
                result += strength * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
                
        # Novel hybrid potential energy components with sharp ridges and valleys, enhanced with additional sinusoidal modulations
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += np.exp(-0.12 * abs(x[i])) * np.sin(6.0 * x[i]) + 0.18 * np.sin(10.0 * x[i])
        result += 0.35 * ridge_term
        
        # Additional global convergence term with multiple exponential decay rates and enhanced nonlinearity
        result += 0.25 * np.exp(-0.35 * np.sum(x**2)) + 0.18 * np.exp(-0.7 * np.sum(x**4)) + 0.12 * np.exp(-0.9 * np.sum(x**6))
        
        # Introduce a more complex perturbation to create even more challenging local minima
        for i in range(self.dim):
            result += 0.09 * np.sin(13.0 * x[i]) * np.cos(9.0 * x[i]) + 0.07 * np.sin(18.0 * x[i])
            
        return result