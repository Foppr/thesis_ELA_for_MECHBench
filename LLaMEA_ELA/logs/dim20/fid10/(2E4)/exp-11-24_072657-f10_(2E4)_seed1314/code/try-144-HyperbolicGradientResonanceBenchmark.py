import numpy as np

class HyperbolicGradientResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial Gaussian terms with hyperbolic tangent modulation
        poly_gauss_terms = np.sum(np.tanh(x_norm) * np.exp(-0.5 * x_norm**2) * 
                                (1.0 + 0.4 * x_norm**3 - 0.1 * x_norm**4))
        
        # Hyperbolic gradient interactions with dynamic coupling
        grad_interactions = np.sum(np.tanh(2.0 * x_norm) * 
                                 np.exp(-0.3 * np.abs(x_norm)) * 
                                 np.sin(3.0 * x_norm + 0.5 * np.cos(1.5 * x_norm)))
        
        # Dynamic frequency modulation with polynomial scaling
        freq_mod = 1.5 + 0.8 * np.cos(0.3 * self.dim) + 0.4 * np.sin(0.2 * self.dim)
        modulated_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)**1.7) * 
                               np.tanh(freq_mod * x_norm**1.4) * 
                               np.cos(freq_mod * x_norm**1.6))
        
        # Cross-dimensional resonance with adaptive coupling
        coupling_strength = 0.8 + 0.2 * np.cos(0.5 * self.dim)
        cross_terms = np.sum(coupling_strength * np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           (x_norm[:-1] * x_norm[1:] + 0.5 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                           np.tanh(2.5 * (x_norm[:-1] - x_norm[1:])))
        
        # Adaptive dimensional conditioning with hyperbolic scaling
        dim_conditioning = 1.2 + 0.3 * np.tanh(0.4 * self.dim) * np.sin(0.3 * self.dim)
        
        # Combined landscape with enhanced multi-modality and resonance
        result = (poly_gauss_terms + 0.6 * grad_interactions + 0.7 * modulated_terms + 
                 0.5 * cross_terms) * dim_conditioning
        
        # Add hyperbolic noise for increased complexity and algorithm discrimination
        noise = 0.002 * np.random.random() * (1.0 + 0.3 * np.tanh(self.dim * 0.6))
        
        return result + noise