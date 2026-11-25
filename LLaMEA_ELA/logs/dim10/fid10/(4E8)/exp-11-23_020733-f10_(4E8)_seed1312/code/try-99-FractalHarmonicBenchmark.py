import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like term with power-law scaling
        result = 0.0
        for i in range(self.dim):
            # Logarithmic barrier near boundaries
            penalty = 0.0
            if abs(x[i]) > 4.0:
                penalty = 10.0 * np.log(abs(x[i]) - 3.9)
            result += penalty + 0.1 * x[i]**2
            
        # Multi-scale harmonic oscillations with fractal frequency patterns
        for i in range(self.dim):
            freq = 2.0 * (1.0 + 0.5 * np.sin(i * np.pi / self.dim)) * np.log(i + 2)
            result += 2.0 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
            
        # Self-similar geometric components with varying amplitude
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            result += amp * np.sin(2**i * x[i]) * np.cos(2**(i+1) * x[i])
            
        # Cross-dimensional coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * np.sin(x[i] + x[j]) * np.exp(-abs(x[i] - x[j]) / (i + j + 1))
                result += coupling
                
        # Logarithmic spiral potential with chaotic modulation
        spiral_term = 0.0
        for i in range(self.dim):
            spiral_term += np.log(abs(x[i]) + 1) * np.sin(np.log(i + 1) * x[i])
        result += 0.5 * spiral_term
        
        # Multi-scale periodicity with diminishing amplitude
        for scale in [1, 2, 4]:
            if scale <= self.dim:
                for i in range(self.dim):
                    freq = 3.0 * scale * np.cos(i * np.pi / (self.dim + 1))
                    result += 0.2 * np.sin(freq * x[i]) * np.exp(-scale * abs(x[i]))
                    
        # Asymmetric penalty with fractal dimension scaling
        asym_penalty = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                asym_penalty += 1.2 * np.log(x[i] + 1) * (x[i]**3)
            else:
                asym_penalty += 0.8 * np.log(-x[i] + 1) * (x[i]**4)
        result += asym_penalty
        
        return result