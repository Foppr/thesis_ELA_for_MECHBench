import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive parameters
        self.chaos_seq = np.sin(np.arange(1000) * 0.123456789) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with time-varying coefficients
        chaotic_grad = 0.0
        for i in range(self.dim):
            idx = int(np.abs(x[i]) * 100) % len(self.chaos_seq)
            coeff = self.chaos_seq[idx]
            chaotic_grad += coeff * np.sin(3.0 * x[i]) * np.cos(2.5 * x[i])
        
        # Multi-scale oscillation with exponentially decaying amplitudes
        multi_scale = 0.0
        for k in range(1, min(6, self.dim + 1)):
            freq = 2 ** k
            amp = 1.0 / (k * 2.0)
            multi_scale += amp * np.sin(freq * x[(k-1) % self.dim])
        
        # Saddle point structure with coupled quadratic and cubic terms
        saddle = 0.0
        for i in range(0, self.dim, 2):
            j = (i + 1) % self.dim
            saddle += (x[i]**2 - x[j]**2) * np.cos(0.5 * x[i]) * np.sin(0.3 * x[j])
        
        # Adaptive conditioning with exponential scaling
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= np.exp(0.1 * np.abs(x[i]))
        
        # Asymmetric penalty with logarithmic scaling
        penalty = np.sum(np.where(np.abs(x) > 4.0, 
                                 0.5 * np.log(1.0 + (np.abs(x) - 4.0)**2), 
                                 0.0))
        
        return 0.3 * chaotic_grad + 0.25 * multi_scale + 0.25 * saddle + penalty * cond_factor