import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed exponents
        poly_base = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**5 + 0.2 * x_norm**4)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig1 = np.sum(2.0 * np.sin(3 * x_norm) * np.cos(7 * x_norm))
        trig2 = np.sum(1.5 * np.sin(5 * x_norm) * np.cos(9 * x_norm))
        trig3 = np.sum(1.0 * np.sin(11 * x_norm) * np.cos(13 * x_norm))
        
        # Exponential interaction terms
        exp_interaction = np.sum(np.exp(-x_norm**2) * np.exp(-0.5 * x_norm**4))
        
        # Custom distance-based interaction (pairwise Euclidean-like)
        dist_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                dist_interaction += np.sqrt((x_norm[i] - x_norm[i+1])**2 + 0.1)
        
        # Chaotic modulation using sine-Gordon-like term
        chaotic = np.sum(np.sin(10 * x_norm) * np.sin(100 * x_norm))
        
        # Radial basis function with varying centers and widths
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            rbf += np.exp(-5.0 * (x_norm - centers[i])**2)
        
        # Cross-dimensional coupling with a custom nonlinear interaction
        coupling = np.sum((x_norm[:-1] * x_norm[1:])**(1.5))
        
        # Additive noise for robustness
        noise = 0.001 * np.random.random()
        
        # Weighted combination of all components
        return (0.4 * poly_base + 
                0.25 * trig1 + 
                0.2 * trig2 + 
                0.15 * trig3 + 
                0.1 * exp_interaction + 
                0.05 * dist_interaction + 
                0.1 * chaotic + 
                0.08 * rbf + 
                0.05 * coupling + 
                noise)