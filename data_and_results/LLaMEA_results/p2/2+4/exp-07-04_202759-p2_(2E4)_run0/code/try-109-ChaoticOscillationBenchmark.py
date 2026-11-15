import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillation component with varying frequencies and amplitudes
        oscillation = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i])
            amp = 1.0 + 0.5 * np.cos(0.3 * x[i])
            oscillation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Asymmetric saddle point component with gradient-dependent scaling
        saddle = 0
        for i in range(self.dim):
            # Asymmetric quadratic term with directional bias
            bias = 0.5 * np.sin(x[i]) * np.cos(x[i])
            saddle += (x[i]**2 + bias * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale interaction term with varying coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for sparsity
                coupling = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                interaction += coupling * np.sin(3 * (x[i] - x[j])) * np.exp(-0.5 * (x[i] - x[j])**2)
        
        # Gradient-dependent conditioning term
        conditioning = 0
        for i in range(self.dim):
            grad_term = np.abs(np.cos(x[i])) + 0.1
            conditioning += grad_term * x[i]**4
        
        # Combined function with dynamic weighting
        return 0.4 * oscillation + 0.3 * saddle + 0.2 * interaction + 0.1 * conditioning