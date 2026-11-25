import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Polynomial chaos component with varying exponents and chaotic modulation
        for i in range(self.dim):
            result += 3.0 * (x[i]**7 + 0.6 * x[i]**6 + 0.4 * x[i]**5 + 0.2 * x[i]**4 + 0.1 * x[i]**3)
            
        # Radial basis function with dynamic centers, widths, and chaotic amplitudes
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                amplitude1 = 2.5 + 0.5 * np.sin(0.3 * i)
                amplitude2 = 1.8 + 0.3 * np.cos(0.4 * i)
                result += amplitude1 * np.exp(-0.4 * (x[i] - centers[i])**2) + amplitude2 * np.exp(-0.2 * (x[i] + centers[i])**2)
                
        # Dynamic cross-dimensional coupling with enhanced chaotic sinusoids
        t = 1.5 + 0.2 * self.dim
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.sin(t * x[i] * x[j]) * np.cos(0.7 * t * (x[i]**2 + x[j]**2)) + 0.3 * np.sin(2.0 * t * x[i] * x[j])
                result += 2.0 * coupling
                
        # Multi-modal sine-polynomial interactions with dynamic frequencies
        for i in range(self.dim):
            freq = 2.5 + 0.5 * np.sin(0.2 * i)
            result += 3.0 * np.sin(freq * x[i]) * (x[i]**5 - 2.5 * x[i]**3 + 1.5 * x[i])
            
        # Fractional power chaotic component with enhanced nonlinearity
        for i in range(self.dim):
            result += 2.2 * np.power(np.abs(x[i]), 1.8) * np.sin(6.0 * x[i]) + 0.8 * np.cos(4.0 * x[i])
            
        # Adaptive conditioning based on dimensionality with chaotic scaling
        condition_factor = 1.2 + 0.7 * np.log(self.dim + 1) + 0.3 * np.sin(0.1 * self.dim)
        result *= condition_factor
        
        # Complex hyperbolic interactions with time-varying parameters
        for i in range(self.dim):
            param1 = 1.8 + 0.4 * np.cos(0.2 * i)
            param2 = 1.5 + 0.3 * np.sin(0.3 * i)
            result += param1 * np.sinh(1.8 * x[i]) * np.cos(2.5 * x[i]) + param2 * np.cosh(1.5 * x[i]) * np.sin(2.2 * x[i])
            
        # Nested trigonometric component with recursive structure and chaotic coefficients
        for i in range(self.dim):
            nested = 0.0
            for k in range(1, 12):
                coeff = 0.4**k * (1.0 + 0.1 * np.sin(0.1 * k * i))
                nested += coeff * np.sin(2**(k) * x[i])
            result += nested
            
        # Penalty term with logarithmic scaling and chaotic modification
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.8 * np.log(np.abs(x[i]) + 1.7) + 0.2 * np.sin(0.5 * i)
        result += penalty
        
        # Multi-modal component with exponential decay interactions and chaotic modulation
        for i in range(self.dim):
            modulator = 1.0 + 0.2 * np.cos(0.3 * i)
            result += modulator * np.exp(-0.6 * x[i]**2) * np.sin(5.0 * x[i])
            
        # Cross-dimensional polynomial coupling with dynamic coefficients and chaotic variations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.7 + 0.4 * np.sin(0.1 * (i + j)) + 0.2 * np.cos(0.2 * i)
                result += coeff * (x[i]**3 + x[j]**3) * np.cos(x[i] * x[j]) + 0.3 * np.sin(0.5 * x[i] * x[j])
                
        # Time-varying chaotic modulation with enhanced complexity
        for i in range(self.dim):
            result += 1.2 * np.sin(np.pi * np.sin(5.0 * x[i])) * np.cos(np.pi * np.cos(4.0 * x[i])) + 0.5 * np.tan(0.3 * x[i])
            
        return result