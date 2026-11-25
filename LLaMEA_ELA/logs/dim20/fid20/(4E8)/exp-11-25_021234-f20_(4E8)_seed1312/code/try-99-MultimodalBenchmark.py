import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin with adaptive scaling
        f1 = 0.03 * np.sum(x**2)
        
        # Enhanced chaotic sinusoidal modulations with logarithmic barriers
        f2 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 3.0 * np.sin(0.6 * i + np.sum(x) / self.dim)
            amp = 1.2 + 0.8 * np.cos(0.4 * i)
            # Add logarithmic barrier effect
            barrier = 1.0 / (1.0 + np.exp(-5.0 * (np.abs(x[i]) - 3.0)))
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2) * barrier
        
        # Multi-scale exponential decay with chaotic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            phase = np.sin(0.5 * i + np.sum(x**2) / (self.dim * 8.0))
            decay = np.exp(-0.4 * np.abs(x[i]))
            # Add multi-scale effect
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * x[i])
            f3 += decay * np.cos(5.0 * x[i] + phase) * scale_factor
        
        # Polynomial terms with chaotic coefficients and logarithmic penalties
        f4 = 0.0
        for i in range(self.dim):
            coeff = 2.0 + 1.0 * np.sin(0.7 * i + np.sum(x) / self.dim)
            # Add penalty for large values
            penalty = 1.0 + 0.3 * np.log(1.0 + np.abs(x[i]))
            f4 += coeff * x[i]**5 * penalty
        
        # Enhanced saddle point structure with multi-scale interactions and cross-terms
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    # Add chaotic interaction strength
                    strength = 0.3 + 0.2 * np.sin(0.5 * (i + j) + np.sum(x) / self.dim)
                    f5 += strength * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Dynamic scaling factor with chaotic modulation
        global_scale = 1.2 + 0.4 * np.sin(np.sum(np.abs(x)) / self.dim)
        f6 = global_scale * np.sum(np.sin(2.5 * x) * np.cos(1.8 * x) * np.exp(-0.25 * x**2))
        
        # Chaotic perturbations with varying intensities and multi-frequency components
        f7 = 0.0
        for i in range(self.dim):
            intensity = 1.0 + 0.6 * np.sin(0.8 * i + np.sum(x) / self.dim)
            # Add multiple frequency components
            f7 += intensity * (np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) + 
                              0.5 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]))
        
        # Add a global logarithmic barrier term
        log_barrier = 2.0 * np.sum(np.log(1.0 + np.exp(0.5 * np.abs(x))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + log_barrier