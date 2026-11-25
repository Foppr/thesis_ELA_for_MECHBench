import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal gradient modulation with higher frequency components
        fractal_term = np.sum(np.sin(3 * np.pi * x_norm) * 
                             np.cos(4 * np.pi * x_norm) * 
                             np.sin(6 * np.pi * x_norm) * 
                             np.exp(-0.15 * np.abs(x_norm)))
        
        # Improved time-variant harmonic components with stronger coupling
        time_variant = np.sum((np.sin(5 * np.pi * x_norm + 0.6 * np.sin(3 * np.pi * x_norm))) * 
                             (1 + 0.4 * np.cos(7 * np.pi * x_norm)) * 
                             np.exp(-0.25 * x_norm**2))
        
        # Enhanced chaotic saddle points with modified logistic map
        chaotic_saddle = np.sum((x_norm**4 - 0.6 * x_norm**3 + 0.15 * x_norm**2) * 
                               np.sin(8 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(5 * np.pi * x_norm)) * 
                               np.exp(-0.25 * np.abs(x_norm)))
        
        # Enhanced multi-scale polynomial coupling
        multiscale = np.sum((x_norm**6 + 0.5 * x_norm**4 - 0.25 * x_norm**2) * 
                           np.cos(4 * x_norm) * 
                           np.exp(-0.15 * x_norm**2))
        
        # Stronger dynamic repulsion field with modified exponential decay
        dynamic_repulsion = np.sum(1 / (1 + np.exp(-12 * (x_norm**2 - 0.15))) * 
                                  np.sin(6 * x_norm) * 
                                  np.cos(5 * x_norm) * 
                                  np.exp(-0.2 * np.abs(x_norm)))
        
        # Enhanced cross-dimensional coupling with stronger interaction terms
        cross_coupling = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**2 * 
                                    np.sin(3 * (x_norm[:-1] + x_norm[1:])) * 
                                    np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Improved global conditioning with modified logarithmic scaling
        global_conditioning = 0.3 * np.sum(np.log(1 + 1.5 * np.abs(x_norm)) * np.exp(-0.15 * x_norm**2))
        
        # Add a strong deceptive term to increase difficulty
        deceptive_term = 0.5 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Combine all terms
        return fractal_term + time_variant - chaotic_saddle + multiscale + dynamic_repulsion + cross_coupling + global_conditioning + deceptive_term