import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient dynamics using logistic map modulation
        logistic_mod = np.sum(4 * x_norm * (1 - x_norm) * np.sin(np.pi * x_norm))
        
        # Embedded peak clustering with varying distances
        peak_cluster = np.sum(np.exp(-np.sum((x_norm.reshape(-1, 1) - x_norm.reshape(1, -1))**2, axis=1) / 0.5) * 
                             np.cos(3 * np.pi * x_norm))
        
        # Adaptive condition number modulation
        cond_mod = np.sum((1 + 0.5 * np.sin(2 * np.pi * x_norm)) * x_norm**2 * np.exp(-0.1 * x_norm**2))
        
        # Multi-scale harmonic interactions
        harmonic_interaction = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                                    (1 + 0.3 * np.sin(6 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with asymmetric scaling
        cross_dim = np.sum((x_norm[:-1] * x_norm[1:]) * np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                          np.sin(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Saddle point enhancement with directional asymmetry
        saddle_enhance = 0.2 * np.sum((x_norm**3 - 0.4 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Global conditioning with polynomial scaling and exponential decay
        global_cond = 0.1 * np.sum(x_norm**6 * np.exp(-0.05 * np.abs(x_norm)))
        
        # Combine all terms
        return logistic_mod + peak_cluster - cond_mod + harmonic_interaction + cross_dim + saddle_enhance + global_cond