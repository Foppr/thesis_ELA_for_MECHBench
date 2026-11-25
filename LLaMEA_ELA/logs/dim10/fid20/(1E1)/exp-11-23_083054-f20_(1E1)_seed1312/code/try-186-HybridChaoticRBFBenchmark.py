import numpy as np

class HybridChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic scaling factors and radial centers
        self.scaling_factors = np.array([0.5 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        self.centers = np.array([2.0 * np.cos(i * 0.6) for i in range(dim)])
        self.chaotic_perturbations = np.array([0.3 + 0.7 * np.sin(i * 1.1) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal component with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * i)
            amp = 1.5 + 0.8 * np.cos(0.6 * i)
            f1 += amp * np.sin(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial basis function component with chaotic centers and widths
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.8 + 0.4 * np.sin(0.5 * i)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
        
        # Chaotic perturbation component with dynamic scaling
        f3 = 0.0
        for i in range(self.dim):
            perturbation = self.chaotic_perturbations[i]
            f3 += perturbation * np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
        
        # Cross-term interactions with chaotic coupling strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.sin(0.7 * (i + j))
                f4 += coupling * x_norm[i] * x_norm[j] * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Asymmetric polynomial component with chaotic exponents
        f5 = 0.0
        for i in range(self.dim):
            exponent = 3.0 + 1.5 * np.sin(0.9 * i)
            f5 += (x_norm[i] - 0.5)**exponent
        
        # Combine all components with adaptive weights
        weights = [0.2 + 0.1 * np.sin(0.8 * i) for i in range(5)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5