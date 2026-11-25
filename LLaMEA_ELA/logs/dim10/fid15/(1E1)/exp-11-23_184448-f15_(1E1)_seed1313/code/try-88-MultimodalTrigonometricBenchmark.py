import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Gaussian radial basis components with random centers and variances
        rbfs = 0.0
        num_rbf = min(10, self.dim * 2)
        for i in range(num_rbf):
            center = np.random.uniform(-4.0, 4.0, self.dim)
            variance = np.random.uniform(0.5, 2.0)
            rbfs += np.exp(-np.sum(((x - center) ** 2) / (2 * variance))) * (i + 1)
        
        # Trigonometric sine-cosine couplings between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(x[i]) * np.cos(x[j]) * (i + j) * 0.1
        
        # Adaptive dimension weighting based on position
        dim_weights = np.array([1.0 + 0.5 * np.sin(x[i] * (i+1)) for i in range(self.dim)])
        weighted_sum = np.sum(dim_weights * x**2)
        
        # Chaotic sine modulation with frequency scaling
        chaotic_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            chaotic_mod += np.sin(x[i] * freq) * np.cos(x[i] * freq * 2)
        
        # Polynomial perturbation with interaction terms
        poly_perturb = 0.0
        for i in range(self.dim):
            poly_perturb += (x[i]**3 - 3*x[i]) * (i + 1) * 0.05
        
        return 0.5 * rbfs + 0.3 * trig_coupling + 0.2 * weighted_sum + 0.1 * chaotic_mod + 0.1 * poly_perturb