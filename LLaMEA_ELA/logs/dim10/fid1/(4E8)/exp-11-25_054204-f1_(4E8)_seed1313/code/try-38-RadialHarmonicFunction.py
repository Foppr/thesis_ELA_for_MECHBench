import numpy as np

class RadialHarmonicFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add radial basis function components with varying widths and heights
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            sigma = 0.5 + 0.5 * np.sin(i)
            height = 1.0 + 0.5 * np.cos(i)
            result += height * np.exp(-0.5 * ((x - center) / sigma)**2)
        
        # Add harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            amp = 0.3 + 0.2 * np.cos(i)
            result += amp * np.sin(freq * x[i])
            
        # Add polynomial decay terms with configurable exponents
        for i in range(self.dim):
            result += 0.1 * (x[i]**(4 + i % 3))
            
        # Add cross-dimensional coupling with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += 0.05 * coupling * (x[i] * x[j])**2
                
        # Add a global quadratic term to ensure conditioning
        result += 0.5 * np.sum(x**2)
        
        return result