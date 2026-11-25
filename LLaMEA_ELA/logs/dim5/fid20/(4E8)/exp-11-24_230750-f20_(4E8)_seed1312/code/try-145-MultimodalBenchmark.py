import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay interactions with varying strength and distance scaling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                exp_decay += np.exp(-0.5 * (dist / (1.0 + 0.1 * np.abs(x[i]) + 0.1 * np.abs(x[j])))) * \
                            np.cos(2.0 * np.pi * dist) * (1.0 + 0.3 * np.sin(0.5 * np.pi * x[i]))
        
        # Cosine modulation with adaptive frequency and amplitude based on dimensionality
        cos_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * np.pi * i)
            amp = 1.0 + 0.4 * np.cos(0.4 * np.pi * i)
            cos_mod += amp * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive radial symmetry with dynamic center and scaling factors
        radial_sym = 0.0
        centers = np.linspace(-3.0, 3.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            dist_from_center = np.sqrt(np.sum((x - centers[i])**2))
            radial_sym += np.exp(-0.5 * (dist_from_center / (1.0 + 0.2 * np.abs(x[i])))) * \
                         np.sin(3.0 * dist_from_center) * np.cos(2.0 * x[i])
        
        # Polynomial coupling with mixed degrees and alternating signs
        poly_coupling = 0.0
        for i in range(self.dim - 1):
            poly_coupling += (-1)**i * (x[i]**3 + x[i+1]**4) * np.cos(0.5 * x[i] * x[i+1])
        
        # Dynamic conditioning based on coordinate distribution and global statistics
        cond_factor = 1.0 + 0.3 * np.sin(self.dim * 0.2) * (np.std(x) / (np.mean(np.abs(x)) + 1e-8))
        
        # Quadratic base with directional weighting and adaptive scaling
        quadratic = cond_factor * np.sum((x**2) * (1.0 + 0.2 * np.sin(0.5 * x)))
        
        # Additional noise component with structured correlation
        noise = 0.03 * np.random.rand() * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        # Combine all components into final fitness value
        return quadratic + exp_decay + cos_mod + radial_sym + poly_coupling + noise