import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.3 * x_scaled**5 - 0.4 * x_scaled**4 + 0.2 * x_scaled**3 - 0.1 * x_scaled**2 + 0.05 * x_scaled)
        
        # Trigonometric interference with chaotic frequency modulation
        f2 = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) * 
                   np.sin(9 * x_scaled) * np.cos(6 * x_scaled) * 
                   np.sin(3 * x_scaled) * np.cos(1.5 * x_scaled))
        
        # Adaptive radial basis function components with chaotic center placement
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.5 * np.sin(i * 2.1) * np.cos(i * 1.7)
            width = 0.1 + 0.05 * np.sin(i * 3.2)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1 + 0.1 * np.sin(i * 4.3))
        
        # Cross-dimensional interaction terms with chaotic coupling strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(i * 0.7) * np.cos(j * 0.9) * (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * coupling
        
        # Asymmetric saddle point structure with chaotic perturbations
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.2 * x_scaled**6)
        
        # High-frequency oscillation with chaotic amplitude modulation
        f6 = np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled) * 
                   (1 + 0.1 * np.sin(x_scaled * 3.14)))
        
        # Combined penalty for boundary avoidance with chaotic weighting
        f7 = 0.3 * np.sum(np.abs(x_scaled)**4 + np.abs(x_scaled)**2.5 + 0.1 * np.sin(x_scaled * 2.7))
        
        # Chaotic cross-dimensional interaction term
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j > self.dim:
                    f8 += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8