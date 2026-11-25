import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.5 * np.sum(x**2)
        
        # Add multiple chaotic sinusoidal components with nested frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 3 ** (i % 6 + 1)
            freq2 = 5 ** (i % 4 + 1)
            amp1 = 0.8 * np.exp(-0.1 * np.abs(x[i]))
            amp2 = 0.6 * np.exp(-0.05 * np.abs(x[i]))
            result += amp1 * np.sin(freq1 * x[i]) * np.cos(freq1 * x[i] * 0.4) + \
                     amp2 * np.sin(freq2 * x[i] * 0.7) * np.cos(freq2 * x[i] * 0.2)
            
        # Add enhanced polynomial penalties with non-integer exponents and varying coefficients
        for i in range(self.dim):
            power1 = 3.5 + (i % 5)
            power2 = 5.2 + (i % 3)
            result += 0.3 * (x[i] - 1.5)**power1 + 0.28 * (x[i] + 1.8)**power2
            
        # Add a complex global minimum structure with multiple overlapping peaks and ridges
        for i in range(self.dim):
            peak1 = 0.1 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(30 * x[i])
            peak2 = 0.08 * np.exp(-0.5 * ((x[i] + 1.8) / 0.3)**2) * np.cos(20 * x[i])
            result += peak1 + peak2
            
        # Add stronger cross-dimensional coupling with long-range interactions and variable coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                dist = np.abs(x[i] - x[j])
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.3 * dist) * np.exp(-0.05 * dist)
                result += 0.06 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and dynamic scaling
        chaotic_term = 0.1 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.sin(7 * x))
        result += chaotic_term
        
        # Add a saddle point structure to increase conditioning difficulty
        saddle = 0.03 * np.sum(x**4) * np.cos(0.5 * np.sum(x**2))
        result += saddle
        
        return result