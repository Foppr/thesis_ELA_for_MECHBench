import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced harmonic oscillator interactions with frequency modulation
        oscillator_term = np.sum(np.sin(3.5 * np.pi * x_norm) * np.cos(4.2 * np.pi * x_norm) * 
                                (1 + 0.35 * np.sin(2.1 * np.pi * x_norm)) * 
                                np.exp(-0.22 * np.abs(x_norm)))
        
        # Increased saddle point complexity with asymmetric cubic and quartic terms
        saddle_term = np.sum((x_norm**3 - 0.42 * x_norm**2) * 
                            np.cos(1.6 * x_norm) * 
                            np.exp(-0.11 * x_norm**2))
        
        # Modified frequency modulation with additional sinusoidal perturbations
        freq_mod = np.sum(np.sin(5.1 * np.pi * x_norm) * np.cos(7.3 * np.pi * x_norm) * 
                         (1 + 0.16 * np.cos(3.1 * x_norm)) * 
                         np.exp(-0.21 * np.abs(x_norm)))
        
        # Enhanced gradient flow complexity with higher-order polynomial coupling
        gradient_flow = np.sum((x_norm**5 + 0.42 * x_norm**3 - 0.21 * x_norm) * 
                              np.sin(2.6 * x_norm) * 
                              np.exp(-0.16 * x_norm**2))
        
        # Improved saddle point structure with directional bias and cross-dimensional coupling
        saddle_bias = 0.42 * np.sum((x_norm[:-1] - x_norm[1:])**3 * 
                                 np.exp(-0.21 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                 np.sin(0.72 * (x_norm[:-1] + x_norm[1:])))
        
        # Global conditioning with modified polynomial scaling and added logarithmic term
        conditioning = 0.085 * np.sum(x_norm**6) + 0.021 * np.sum(np.log(1 + np.abs(x_norm)))
        
        # Add a small perturbation to increase landscape complexity
        perturbation = 0.01 * np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Combine all terms
        return oscillator_term + saddle_term - freq_mod + gradient_flow + saddle_bias + conditioning + perturbation