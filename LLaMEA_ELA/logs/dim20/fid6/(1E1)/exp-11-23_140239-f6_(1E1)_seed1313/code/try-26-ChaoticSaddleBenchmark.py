import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point function with oscillating valleys
        result = 0.0
        
        # Sum of exponentially decaying sinusoidal terms
        for i in range(self.dim):
            # Create a chaotic effect with varying frequencies and amplitudes
            freq = 2 * np.pi * (i + 1) * np.exp(-0.1 * i)
            amp = 10 * np.exp(-0.05 * i)
            
            # Oscillating term with saddle-point characteristics
            oscillation = amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
            # Add a quadratic basin term to create local minima
            basin = 0.1 * (x[i] - 2 * np.sin(0.5 * x[i]))**2
            
            result += oscillation + basin
        
        # Add a global scaling factor and offset for better conditioning
        return result * 0.1 + 0.5 * np.sum(x**4) / self.dim - 10.0