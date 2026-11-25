import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add enhanced chaotic sine-wave interactions with varying amplitudes and frequencies
        for i in range(self.dim):
            f_val += 0.6 * np.sin(12 * np.pi * x[i]) + 0.4 * np.sin(25 * np.pi * x[i]) + \
                     0.3 * np.sin(50 * np.pi * x[i]) + 0.2 * np.sin(100 * np.pi * x[i])
        
        # Add modified polynomial conditioning with exponential scaling
        for i in range(self.dim):
            f_val += 0.15 * np.abs(x[i])**4.0 + 0.1 * np.abs(x[i])**6.0 + \
                     0.05 * np.abs(x[i])**8.0
        
        # Add strengthened cross-dimensional exponential penalties with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                penalty = 0.4 * np.exp(-0.15 * (x[i] - x[j])**2) + \
                          0.3 * np.exp(-0.25 * (x[i] + x[j])**2)
                f_val += penalty
        
        # Add enhanced harmonic interactions with stronger chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.08 * np.sin(4 * x[i]) * np.cos(5 * x[j]) + \
                           0.06 * np.cos(3 * x[i]) * np.sin(6 * x[j])
                f_val += coupling * np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Add global sinusoidal modulation with enhanced chaotic frequency
        f_val += 0.3 * np.sin(0.8 * np.sum(x)) + 0.2 * np.cos(0.5 * np.sum(x)**2) + \
                 0.15 * np.sin(0.4 * np.sum(x)**3)
        
        # Add enhanced chaotic correlation terms between all dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.02 * np.sin(x[i] + x[j] + x[k]) * \
                             np.cos(0.6 * (x[i] - x[j])) * \
                             np.exp(-0.03 * (x[k]**2))
        
        # Add enhanced multi-scale chaotic oscillations with varying amplitudes
        for i in range(self.dim):
            f_val += 0.15 * np.sin(60 * np.pi * x[i]) + 0.1 * np.sin(120 * np.pi * x[i]) + \
                     0.05 * np.sin(240 * np.pi * x[i])
        
        # Add additional chaotic noise terms to increase landscape complexity
        for i in range(self.dim):
            f_val += 0.03 * np.sin(150 * np.pi * x[i]) + 0.02 * np.cos(200 * np.pi * x[i])
        
        return f_val