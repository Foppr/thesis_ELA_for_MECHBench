import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced harmonic oscillator interactions with frequency modulation and cross-dimensional coupling
        oscillator_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                                (1 + 0.3 * np.sin(2 * np.pi * x_norm)) * 
                                np.exp(-0.2 * np.abs(x_norm)))
        
        # Increased saddle point complexity with asymmetric cubic and quartic terms
        saddle_term = np.sum((x_norm**3 - 0.4 * x_norm**2) * 
                            np.cos(1.5 * x_norm) * 
                            np.exp(-0.1 * x_norm**2))
        
        # Modified frequency modulation with additional sinusoidal perturbations and directional bias
        freq_mod = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                         (1 + 0.15 * np.cos(3 * x_norm)) * 
                         np.exp(-0.2 * np.abs(x_norm)))
        
        # Enhanced gradient flow complexity with higher-order polynomial coupling and repulsive force field
        gradient_flow = np.sum((x_norm**5 + 0.4 * x_norm**3 - 0.2 * x_norm) * 
                              np.sin(2.5 * x_norm) * 
                              np.exp(-0.15 * x_norm**2))
        
        # Improved saddle point structure with directional bias and cross-dimensional coupling
        saddle_bias = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**3 * 
                                 np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                 np.sin(0.7 * (x_norm[:-1] + x_norm[1:])))
        
        # Global conditioning with modified polynomial scaling and added logarithmic term
        conditioning = 0.08 * np.sum(x_norm**6) + 0.02 * np.sum(np.log(1 + np.abs(x_norm)))
        
        # Perturbed repulsive force field to enhance multimodality and convergence challenges
        repulsion = 0.3 * np.sum(np.exp(-0.5 * (x_norm**2 + 0.5 * x_norm**4)) * 
                               np.sin(6 * np.pi * x_norm) * 
                               np.cos(8 * np.pi * x_norm))
        
        # Additional high-frequency oscillatory component for increased complexity
        high_freq = 0.2 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm) * 
                               (1 + 0.2 * np.sin(4 * x_norm)) * 
                               np.exp(-0.3 * np.abs(x_norm)))
        
        # Combine all terms
        return oscillator_term + saddle_term - freq_mod + gradient_flow + saddle_bias + conditioning + repulsion + high_freq