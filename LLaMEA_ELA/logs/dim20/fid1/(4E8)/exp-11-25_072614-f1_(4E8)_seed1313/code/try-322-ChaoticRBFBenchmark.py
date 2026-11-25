import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for sine wave modulation
        self.chaos_params = np.array([1.5 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        # Adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.8 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = self.chaos_params[i]
            chaotic_term += np.sin(freq * x[i] + np.sin(2.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        chaotic_term /= self.dim
        
        # Radial basis function component
        rbf_term = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf_term += self.widths[i] * np.exp(-0.5 * np.sum((diff**2) / (self.conditioning**2)))
        rbf_term /= 10.0
        
        # Adaptive conditioning term
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning[i] * x[i]**2 * np.exp(-0.05 * x[i]**2)
        cond_term /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i] + x[j]) + 0.3 * np.sum(x)) * np.exp(-0.1 * abs(x[i] - x[j]))
                cross_term += coupling * (x[i]**2 + x[j]**2)
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale oscillation with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.8 * np.pi * i)
            multi_scale += amp * np.sin(3.0 * x[i] + 0.2 * np.sum(x)) * np.exp(-0.1 * x[i]**2)
        multi_scale /= self.dim
        
        # Saddle point structure with hyperbolic tangent
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(1.5 * x[i]) * np.exp(-0.08 * x[i]**2)
        saddle_term /= self.dim
        
        # Combined weighted sum
        total = (0.3 * chaotic_term + 
                 0.25 * rbf_term + 
                 0.2 * cond_term + 
                 0.15 * cross_term + 
                 0.08 * multi_scale + 
                 0.02 * saddle_term)
        
        return total