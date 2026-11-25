import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced sinusoidal chaotic component with fractal-like frequency modulation
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * (1 + 0.3 * np.sin(0.5 * i))
            result += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Modified polynomial potential with higher-order terms and variable coefficients
        for i in range(self.dim):
            poly = ((-1)**i) * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
            result += 0.4 * poly
        
        # Enhanced cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
                result += 0.4 * coupling
        
        # Modified logistic map inspired chaotic behavior with parameter variation
        for i in range(self.dim):
            logistic = 3.8 * x[i] * (1 - x[i]**2)
            result += 0.3 * np.sin(logistic * 2)
        
        # Multi-scale harmonic component with dynamic scaling factors
        for i in range(self.dim):
            scale = 1 + 0.7 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            result += 0.5 * scale * np.cos(7 * x[i] + 0.5 * np.sin(x[i]))
        
        # Additional chaotic harmonic component with varying amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(13 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result