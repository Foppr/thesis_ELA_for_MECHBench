import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sinusoidal modulations with chaotic frequency components
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + 1.0)
            result += 3.0 * np.sin(freq * x[i]) * np.cos(0.7 * x[i]**2)
            
        # Polynomial chaos with dynamic exponents
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(0.2 * i)
            result += 1.5 * (x[i]**exp_factor + 0.8 * x[i]**(exp_factor + 1))
            
        # Fractal-like nested structure with recursive scaling
        for i in range(self.dim):
            nested_sum = 0.0
            scale = 1.0
            for k in range(1, min(6, self.dim)):
                scale *= 0.7
                nested_sum += scale * np.sin(2**(k) * x[i])
            result += 2.0 * nested_sum
            
        # Adaptive conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.2 * np.mean(np.abs(x))
        result *= condition_factor
        
        # Multi-scale chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interaction = np.sin(3.0 * x[i] + 2.0 * x[j]) * np.cos(1.5 * x[i] - x[j])
                result += 1.2 * interaction * (1.0 + 0.1 * np.abs(x[i] * x[j]))
                
        # Hyperbolic tangent and logarithmic components
        for i in range(self.dim):
            result += 2.5 * np.tanh(1.5 * x[i]) * np.log(np.abs(x[i]) + 2.0)
            
        # Cross-dimensional coupling with time-varying coefficients
        t = 0.5 + 0.5 * np.sin(0.1 * self.dim)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = (1.0 + 0.3 * np.sin(t * (i + j))) * np.cos(0.5 * x[i] * x[j])
                result += coeff * (x[i]**2 + x[j]**2)
                
        # Multi-modal sine-polynomial hybrid
        for i in range(self.dim):
            result += 1.8 * np.sin(4.0 * x[i]) * (x[i]**3 - x[i])
            
        # Exponential decay with sinusoidal modulation
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i])
            
        # Fractional power chaotic component
        for i in range(self.dim):
            result += 1.3 * np.power(np.abs(x[i]), 1.8) * np.sin(4.0 * x[i])
            
        return result