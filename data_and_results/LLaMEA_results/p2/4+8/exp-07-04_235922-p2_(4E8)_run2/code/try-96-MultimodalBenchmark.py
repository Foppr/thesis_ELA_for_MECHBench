import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic exponential terms with polynomial chaos
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**9 - 36*xi**7 + 588*xi**5 - 4200*xi**3 + 10500*xi
            exp_term = np.exp(-0.5 * xi**2) * np.sin(3 * xi) + 0.3 * np.exp(-0.3 * xi**2) * np.cos(5 * xi)
            result += 0.15 * poly_term * exp_term
        
        # Add higher-order polynomial coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**3 + x[j]**3) * np.sin(0.2 * x[i] * x[j]) + (x[i]**2 * x[j]**2) * np.cos(0.3 * x[i] * x[j])
                result += 0.25 * coupling * (x[i]**4 + x[j]**4)
        
        # Add adaptive multi-scale radial barriers
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += (x[i] - 2.0)**2 + (x[i] + 2.0)**2
        barrier = 0.6 * np.exp(-0.08 * radial_sum) + 0.4 * np.exp(-0.02 * radial_sum**2) + 0.2 * np.exp(-0.01 * radial_sum**3)
        result += barrier
        
        # Add dynamic conditioning with chaotic modulation
        conditioning = 1.0 + 0.15 * np.sin(self.dim * 0.8) * np.cos(self.dim * 0.5) + 0.08 * np.sin(self.dim * 1.1) * np.cos(self.dim * 0.9) + 0.05 * np.sin(self.dim * 1.3)
        result *= conditioning
        
        # Add multi-scale sinusoidal modulation with exponential decay
        modulate = 0.0
        for i in range(self.dim):
            modulate += np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.03 * x[i]**2) + 0.25 * np.sin(10 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.015 * x[i]**2) + 0.15 * np.sin(15 * x[i]) * np.cos(17 * x[i]) * np.exp(-0.01 * x[i]**2)
        result += 0.25 * modulate
        
        # Add noise component with chaotic scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(15 * x[i]) * np.cos(13 * x[i]) * np.exp(-0.04 * x[i]**2) + 0.15 * np.sin(18 * x[i]) * np.cos(16 * x[i]) * np.exp(-0.02 * x[i]**2) + 0.1 * np.sin(20 * x[i]) * np.cos(19 * x[i])
        result += 0.02 * noise
        
        return result