import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with logarithmic boundary penalties
        result = 0.0
        for i in range(self.dim):
            # Logarithmic barrier near boundaries
            penalty = 0.0
            if abs(x[i]) > 4.0:
                penalty = 5.0 * np.log(abs(x[i]) - 3.9)
            result += penalty + 0.1 * x[i]**2
            
        # Multi-scale harmonic oscillations with chaotic frequency modulation
        for i in range(self.dim):
            freq = 2.0 * (1.0 + 0.3 * np.sin(i * np.pi / self.dim)) * np.log(i + 2)
            result += 1.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
            
        # Self-similar geometric components with chaotic amplitude scaling
        for i in range(self.dim):
            amp = 1.0 + 0.4 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 3))
            result += amp * np.sin(2**i * x[i]) * np.cos(2**(i+1) * x[i])
            
        # Cross-dimensional coupling with chaotic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * np.sin(x[i] + x[j]) * np.exp(-abs(x[i] - x[j]) / (i + j + 2))
                result += coupling
                
        # Logarithmic spiral potential with chaotic modulation
        spiral_term = 0.0
        for i in range(self.dim):
            spiral_term += np.log(abs(x[i]) + 1) * np.sin(np.log(i + 1) * x[i])
        result += 0.3 * spiral_term
        
        # Multi-scale periodicity with diminishing amplitude and chaotic scaling
        for scale in [1, 2, 4]:
            if scale <= self.dim:
                for i in range(self.dim):
                    freq = 2.5 * scale * np.cos(i * np.pi / (self.dim + 1)) * (1.0 + 0.2 * np.sin(scale * i))
                    result += 0.15 * np.sin(freq * x[i]) * np.exp(-scale * abs(x[i]))
                    
        # Asymmetric penalty with chaotic dimension scaling
        asym_penalty = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                asym_penalty += 0.8 * np.log(x[i] + 1) * (x[i]**2.5)
            else:
                asym_penalty += 0.6 * np.log(-x[i] + 1) * (x[i]**3.5)
        result += asym_penalty
        
        # Add chaotic noise component to increase landscape irregularity
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += 0.1 * np.sin(10 * x[i] + np.cos(i)) * np.cos(5 * x[i] + np.sin(i))
        result += chaos_noise
        
        return result