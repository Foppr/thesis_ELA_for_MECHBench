import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced coupled harmonic oscillators with adaptive frequencies
        freq_adapt = 1 + 0.3 * np.sin(2 * np.pi * x_norm) * np.cos(1.5 * np.pi * x_norm)
        oscillator_term = np.sum(np.sin(freq_adapt * x_norm) * np.cos(freq_adapt * x_norm) * 
                                (1 + 0.15 * np.sin(4 * np.pi * x_norm)) * 
                                np.exp(-0.2 * np.abs(x_norm)))
        
        # Increased polynomial coupling with saddle point embeddings
        poly_coupling = np.sum((x_norm**3 - 0.4 * x_norm**2 + 0.1 * x_norm) * 
                              np.cos(3 * x_norm) * 
                              np.exp(-0.1 * x_norm**2))
        
        # Perturbed repulsive force field with fractal-like patterns
        repulsion_field = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                                (1 + 0.25 * np.cos(3 * x_norm)) * 
                                np.exp(-0.3 * np.abs(x_norm)))
        
        # Gradient flow complexity with directional modulation
        gradient_flow = np.sum((x_norm**5 + 0.4 * x_norm**3 - 0.2 * x_norm) * 
                              np.sin(2.5 * x_norm) * 
                              np.exp(-0.15 * x_norm**2))
        
        # Embedded saddle points with directional bias and spatial correlation
        saddle_bias = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**3 * 
                                 np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                 np.sin(0.7 * (x_norm[:-1] + x_norm[1:])))
        
        # Global conditioning with cross-dimensional interactions
        conditioning = 0.1 * np.sum(x_norm**6 + 0.5 * x_norm**4)
        
        # Add noise-like perturbations for increased complexity
        noise_perturbation = 0.05 * np.sum(np.sin(10 * np.pi * x_norm) * 
                                          np.cos(8 * np.pi * x_norm) * 
                                          np.exp(-0.25 * x_norm**2))
        
        # Combine all terms with adjusted weights
        return oscillator_term + poly_coupling - repulsion_field + gradient_flow + saddle_bias + conditioning + noise_perturbation