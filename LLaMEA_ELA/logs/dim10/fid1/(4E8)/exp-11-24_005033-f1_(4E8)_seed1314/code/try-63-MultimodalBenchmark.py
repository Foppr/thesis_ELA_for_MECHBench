import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial basis function components with chaotic frequency modulation
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            freq = 1.0 + 0.5 * np.sin(0.3 * r + i) + 0.2 * np.cos(0.7 * r + i)
            result += 0.8 * np.exp(-0.5 * (x[i] * freq)**2) * np.sin(freq * x[i])**2
        
        # Adaptive cubic coupling with dynamic phase shifts
        for i in range(self.dim - 1):
            phase_shift = 0.5 * np.sin(0.2 * x[i] + 0.3 * x[i+1])
            result += 0.6 * (x[i]**3 + x[i+1]**3) * np.cos(phase_shift)
        
        # Cross-dimensional quartic interactions with varying coupling strengths
        for i in range(self.dim - 2):
            coupling = 0.3 + 0.2 * np.sin(0.5 * i)
            result += coupling * (x[i] * x[i+1] * x[i+2])**2
        
        # Dynamic exponential penalty with position-dependent scaling
        pos_scale = 1.0 + 0.4 * np.sum(np.abs(x)) + 0.1 * np.sum(x**2)
        result += 0.5 * np.exp(pos_scale * np.sum(np.sin(0.3 * x)**2))
        
        # Enhanced nonlinear terms with modified polynomial weights
        for i in range(self.dim):
            result += 0.04 * x[i]**6 + 0.03 * x[i]**8 + 0.02 * x[i]**10
        
        return result