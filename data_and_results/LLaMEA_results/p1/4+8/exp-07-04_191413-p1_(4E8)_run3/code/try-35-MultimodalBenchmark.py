import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for trigonometric components
        np.random.seed(42)
        self.freqs = np.random.uniform(1.0, 3.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0.0, 2*np.pi, dim)
        
    def f(self, x):
        # Periodic trigonometric components
        trig_term = np.sum(self.amps * np.sin(self.freqs * x + self.phase_shifts) * 
                          np.cos(self.freqs * x + self.phase_shifts))
        
        # Asymmetric saddle points with exponential decay
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i] ** 2 - 1) ** 2 * np.exp(-0.1 * (x[i] ** 2))
            
        # Gradient-dependent conditioning
        grad_cond = 0.0
        for i in range(self.dim - 1):
            grad_cond += (x[i+1] - x[i]) ** 2 * (1 + 0.1 * np.abs(x[i]))
            
        # Cross-dimensional interaction with asymmetric weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1 + 0.01 * (x[i]**2 + x[j]**2))
                
        # Combine all terms
        return trig_term + 0.5 * saddle_term + 0.1 * grad_cond + 0.05 * cross_term