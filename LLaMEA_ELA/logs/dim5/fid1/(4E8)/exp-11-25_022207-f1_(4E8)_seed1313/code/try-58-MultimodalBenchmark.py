import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic tent map-inspired term for high sensitivity to initial conditions
        tent_term = np.sum(1.0 - 2.0 * np.abs(x_normalized - 0.5))
        
        # Multi-scale fractal noise with varying frequency components
        fractal_noise = np.sum(np.sin(13 * x_normalized) * np.cos(7 * x_normalized) + 
                              0.5 * np.sin(23 * x_normalized) * np.cos(11 * x_normalized) + 
                              0.3 * np.sin(37 * x_normalized) * np.cos(17 * x_normalized))
        
        # Asymmetric hyperbolic tangent potentials with varying steepness
        tanh_potential = np.sum(np.where(x_normalized >= 0, 
                                        0.8 * np.tanh(2 * x_normalized) - 0.3 * x_normalized**2,
                                        1.2 * np.tanh(1.5 * x_normalized) - 0.6 * x_normalized**2))
        
        # Coupled polynomial interactions with cross-dimension dependencies
        poly_interaction = np.sum(x_normalized**7 * np.sin(3 * x_normalized) + 
                                x_normalized**4 * np.cos(5 * x_normalized) + 
                                0.7 * x_normalized**8 * np.sin(x_normalized) + 
                                0.4 * x_normalized**5 * np.cos(2 * x_normalized))
        
        # Cross-dimensional coupling with exponential interaction terms
        cross_coupling = np.sum(np.exp(-np.abs(x_normalized[:-1] - x_normalized[1:])) * 
                               (x_normalized[:-1]**3 + x_normalized[1:]**3))
        
        # Add noise term to increase robustness and challenge optimization algorithms
        noise = 0.15 * np.random.normal(0, 1, self.dim).sum()
        
        # Combine all terms with adjusted weights for balanced contribution
        return tent_term + fractal_noise + tanh_potential + poly_interaction + cross_coupling + noise