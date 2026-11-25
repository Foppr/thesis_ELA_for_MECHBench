import numpy as np

class HyperbolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic sine chaotic component
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sinh(x[i]) * np.cos(x[i] * np.pi / 3.0) * (1.0 + 0.2 * np.sin(0.5 * x[i]))
        chaotic_term /= self.dim
        
        # Quaternion-inspired spectral decomposition
        spectral_term = 0.0
        for i in range(self.dim):
            spectral_term += (np.sin(x[i] * np.pi / 2.0) ** 2 + np.cos(x[i] * np.pi / 4.0) ** 2) * np.exp(-0.1 * x[i]**2)
        spectral_term /= self.dim
        
        # Dynamic elastic net penalty with adaptive regularization
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_term += (np.abs(x[i]) ** 1.5 + 0.5 * np.sin(0.3 * x[i])) * (1.0 + 0.1 * np.cos(0.2 * x[i]))
        penalty_term /= self.dim
        
        # Multi-scale harmonic oscillation with varying amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi / 3.0) * np.exp(-0.1 * x[i]**2)
        harmonic_term /= self.dim
        
        # Cross-dimensional coupling with inverse distance weighting
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                cross_coupling += np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) / (dist + 1e-8)
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Asymmetric exponential decay with parameter adaptation
        exp_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                exp_term += np.exp(-0.5 * x[i]) * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            else:
                exp_term += np.exp(-0.3 * x[i]) * (1.0 + 0.2 * np.cos(0.6 * x[i]))
        exp_term /= self.dim
        
        # Fractal-like basin structure with recursive scaling
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.sin(x[i] * np.pi / 4.0) * np.cos(x[i] * np.pi / 8.0) * (1.0 + 0.1 * np.sin(0.2 * x[i]))
        basin_term /= self.dim
        
        # Combine all terms with carefully tuned weights
        total = 0.22 * chaotic_term + 0.19 * spectral_term + 0.16 * penalty_term + 0.15 * harmonic_term + 0.13 * cross_coupling + 0.10 * exp_term + 0.15 * basin_term
        
        return total