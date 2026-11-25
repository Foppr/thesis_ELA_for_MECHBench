import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced harmonic oscillator interactions with frequency modulation and phase shifts
        oscillator_term = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                                (1 + 0.4 * np.sin(3 * np.pi * x_norm)) * 
                                np.exp(-0.25 * np.abs(x_norm)))
        
        # Increased saddle point complexity with asymmetric cubic and quartic terms and perturbed gradients
        saddle_term = np.sum((x_norm**4 - 0.5 * x_norm**3 + 0.1 * x_norm) * 
                            np.cos(2 * x_norm) * 
                            np.exp(-0.15 * x_norm**2))
        
        # Modified frequency modulation with additional sinusoidal perturbations and cross-dimensional coupling
        freq_mod = np.sum(np.sin(6 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * 
                         (1 + 0.2 * np.cos(4 * x_norm)) * 
                         np.exp(-0.25 * np.abs(x_norm)))
        
        # Enhanced gradient flow complexity with higher-order polynomial coupling and directional bias
        gradient_flow = np.sum((x_norm**6 + 0.5 * x_norm**4 - 0.3 * x_norm**2) * 
                              np.sin(3 * x_norm) * 
                              np.exp(-0.2 * x_norm**2))
        
        # Improved saddle point structure with directional bias and cross-dimensional coupling
        saddle_bias = 0.5 * np.sum((x_norm[:-1] - x_norm[1:])**4 * 
                                 np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                 np.sin(0.8 * (x_norm[:-1] + x_norm[1:])))
        
        # Global conditioning with modified polynomial scaling and added logarithmic term
        conditioning = 0.1 * np.sum(x_norm**7) + 0.03 * np.sum(np.log(1 + np.abs(x_norm)))
        
        # Perturbed repulsive force field to enhance multimodality and convergence challenges
        repulsion = 0.3 * np.sum(1 / (1 + np.exp(-5 * (x_norm**2 - 0.2))) * 
                               np.sin(3 * x_norm) * 
                               np.cos(2 * x_norm))
        
        # Additional chaotic modulation for improved discrimination
        chaotic_mod = 0.2 * np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * 
                                  np.exp(-0.3 * x_norm**2) * 
                                  np.sin(0.5 * np.pi * x_norm))
        
        # Cross-dimensional coupling enhancement
        cross_coupling = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                    np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Combine all terms with adjusted weights for better performance
        return oscillator_term + saddle_term - freq_mod + gradient_flow + saddle_bias + conditioning + repulsion + chaotic_mod - cross_coupling