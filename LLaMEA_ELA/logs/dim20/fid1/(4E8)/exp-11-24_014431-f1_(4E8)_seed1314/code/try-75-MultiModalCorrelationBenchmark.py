import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave interactions with varying amplitudes and frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(10 * np.pi * x[i]) + 0.3 * np.sin(20 * np.pi * x[i]) + \
                     0.2 * np.sin(40 * np.pi * x[i]) + 0.1 * np.sin(80 * np.pi * x[i])
        
        # Add adaptive polynomial conditioning with exponential scaling
        for i in range(self.dim):
            f_val += 0.1 * np.abs(x[i])**3.5 + 0.05 * np.abs(x[i])**5.5 + \
                     0.02 * np.abs(x[i])**7.5
        
        # Add cross-dimensional exponential penalties with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                penalty = 0.3 * np.exp(-0.1 * (x[i] - x[j])**2) + \
                          0.2 * np.exp(-0.2 * (x[i] + x[j])**2)
                f_val += penalty
        
        # Add multiple harmonic interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.05 * np.sin(3 * x[i]) * np.cos(4 * x[j]) + \
                           0.03 * np.cos(2 * x[i]) * np.sin(5 * x[j])
                f_val += coupling * np.exp(-0.01 * (x[i] - x[j])**2)
        
        # Add global sinusoidal modulation with chaotic frequency
        f_val += 0.2 * np.sin(0.7 * np.sum(x)) + 0.15 * np.cos(0.4 * np.sum(x)**2) + \
                 0.1 * np.sin(0.3 * np.sum(x)**3)
        
        # Add chaotic correlation terms between all dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.01 * np.sin(x[i] + x[j] + x[k]) * \
                             np.cos(0.5 * (x[i] - x[j])) * \
                             np.exp(-0.02 * (x[k]**2))
        
        # Add multi-scale chaotic oscillations with varying amplitudes
        for i in range(self.dim):
            f_val += 0.1 * np.sin(50 * np.pi * x[i]) + 0.05 * np.sin(100 * np.pi * x[i]) + \
                     0.02 * np.sin(200 * np.pi * x[i])
        
        return f_val