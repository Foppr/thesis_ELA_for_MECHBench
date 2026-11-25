import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components with varying frequencies and higher chaos
        for i in range(self.dim):
            freq = 3 ** (i % 6 + 1)
            decay = np.exp(-0.15 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 5 + (i % 5)
            result += 0.35 * (x[i] - 1.5)**power + 0.30 * (x[i] + 1.8)**(power + 2)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.12 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(30 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] - x[j]))
                result += 0.06 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.08 * np.sum(np.sin(25 * x) * np.cos(12 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.1 * np.sin(15 * x[i]) * np.exp(-0.3 * (x[i] - 1.0)**2)
            result += asym_term
            
        return result