import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin
        f1 = 0.05 * np.sum(x**2)
        
        # Chaotic sinusoidal modulations with dynamic frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.5 * i + np.sum(x) / self.dim)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Exponential decay with chaotic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            phase = np.sin(0.4 * i + np.sum(x**2) / (self.dim * 10.0))
            decay = np.exp(-0.3 * np.abs(x[i]))
            f3 += decay * np.cos(4.0 * x[i] + phase)
        
        # Polynomial terms with chaotic coefficients
        f4 = 0.0
        for i in range(self.dim):
            coeff = 1.5 + 0.5 * np.sin(0.6 * i + np.sum(x) / self.dim)
            f4 += coeff * x[i]**4
        
        # Saddle point structure with multi-scale interactions
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    f5 += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Dynamic scaling factor based on global landscape features
        global_scale = 1.0 + 0.3 * np.sin(np.sum(np.abs(x)) / self.dim)
        f6 = global_scale * np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.exp(-0.2 * x**2))
        
        # Chaotic perturbations with varying intensities
        f7 = 0.0
        for i in range(self.dim):
            intensity = 0.8 + 0.4 * np.sin(0.7 * i + np.sum(x) / self.dim)
            f7 += intensity * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7