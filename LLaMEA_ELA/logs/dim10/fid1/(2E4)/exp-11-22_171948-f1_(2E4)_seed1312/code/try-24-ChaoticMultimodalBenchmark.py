import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced fractal-like sinusoidal component with chaotic frequency modulation
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * np.sin(0.5 * x[i])
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale polynomial potential with varying exponents
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(0.3 * x[i])
            poly = (-1)**i * (x[i]**exp_factor - 2*x[i]**(exp_factor/2) + 1)
            result += 0.7 * poly
        
        # Complex cross-dimensional coupling with fractal-like interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2) * np.cos(0.1 * x[i] * x[j])
                result += 0.5 * coupling
        
        # Enhanced logistic map inspired chaotic behavior with multiple iterations
        for i in range(self.dim):
            logistic = 4 * x[i] * (1 - x[i])
            for _ in range(3):
                logistic = 4 * logistic * (1 - logistic)
            result += 0.3 * np.sin(logistic + np.cos(x[i]))
        
        # Multi-scale harmonic component with fractal-like frequency modulation
        for i in range(self.dim):
            scale = 1 + 0.8 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            result += 0.6 * scale * np.cos(7 * x[i] + np.sin(x[i]))
        
        # Additional chaotic cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited but intense coupling
                interaction = np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(x[i] + x[j])
                result += 0.4 * interaction
        
        # Fractal-like polynomial component with varying coefficients
        for i in range(self.dim):
            fractal_poly = x[i]**5 - 3*x[i]**3 + 2*x[i]
            result += 0.2 * fractal_poly * np.sin(0.2 * x[i])
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result