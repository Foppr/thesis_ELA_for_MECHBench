import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial base with irregular exponents and stronger higher-order terms
        f_val = 3.0 * np.sum(x_norm**5) + 1.2 * np.sum(x_norm**9) + 0.8 * np.sum(np.abs(x_norm)**3.7)
        
        # Chaotic trigonometric perturbations with non-uniform frequencies and phase shifts
        f_val += 5.0 * np.sum(np.sin(7 * np.pi * x_norm + np.pi/4) * np.cos(5 * np.pi * x_norm + np.pi/3))
        
        # Intensified Gaussian-like attractive points with variable variance and multiple peaks
        gaussian_penalty = 0.0
        centers = np.linspace(-0.9, 0.9, 13)
        variances = np.logspace(-2, -0.5, 13)
        for c, v in zip(centers, variances):
            gaussian_penalty += 3.5 * np.exp(-15 * np.sum((x_norm - c)**2) / v)
        
        f_val += gaussian_penalty
        
        # Extended and irregular cross-dimensional interactions with multi-scale coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                freq_i = 1.5 + 0.5 * np.sin(i * 0.3)
                freq_j = 2.0 + 0.3 * np.cos(j * 0.4)
                cross_term += 0.8 * np.sin(freq_i * np.pi * (x_norm[i] + x_norm[j])) * np.cos(freq_j * np.pi * (x_norm[i] - x_norm[j]))
        f_val += cross_term
        
        # Additional irregular penalty terms to increase conditioning difficulty
        f_val += 0.3 * np.sum(np.abs(x_norm)**4.2) + 0.15 * np.sum(np.sin(9 * np.pi * x_norm))
        
        return f_val