import numpy as np

class MultiModalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2) / (2.0 * self.dim)
        
        # Gaussian radial basis functions with random centers and variances
        rbf_term = 0.0
        num_centers = min(10, self.dim * 2)
        for i in range(num_centers):
            center = np.random.uniform(-3.0, 3.0, self.dim)
            variance = 0.5 + np.random.rand() * 2.0
            distance = np.sum((x - center)**2)
            rbf_term += np.exp(-distance / (2.0 * variance**2))
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                trig_coupling += np.sin(x[i]) * np.cos(x[j]) * (i + j)
        
        # Sine-wave modulation with varying frequencies and amplitudes
        wave_modulation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            wave_modulation += amp * np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
        
        # Exponentially decaying penalty for out-of-bounds regions
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.0 or x[i] > 4.0:
                penalty += np.exp(abs(x[i]) - 4.0)
        
        # Combined fitness with dimensionality scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.5 * rbf_term + 0.3 * trig_coupling + 
                            0.2 * wave_modulation + 0.1 * penalty)