import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [0, 4] range for logistic map parameter
        normalized_x = (x + 5.0) / 2.0
        
        # Chaotic logistic map components with bifurcation points
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = normalized_x[i]
            x_prev = 0.5
            for _ in range(100):  # Allow transient to settle
                x_prev = r * x_prev * (1 - x_prev)
            logistic_terms[i] = x_prev
            
        # Cross-dimensional coupling with varying strength
        coupling_strength = 0.3
        cross_coupling = coupling_strength * np.sum(np.sin(logistic_terms[:-1] - logistic_terms[1:]) * 
                                                  np.cos(logistic_terms[:-1] + logistic_terms[1:]))
        
        # Fractal-like terrain with multiple scales
        fractal_terrain = 0.4 * np.sum(np.sin(10 * logistic_terms) * np.cos(15 * logistic_terms) + 
                                     np.sin(20 * logistic_terms) * np.cos(25 * logistic_terms))
        
        # Multi-scale curvature using different powers
        curvature = 0.3 * np.sum(logistic_terms**3 + logistic_terms**5 + logistic_terms**7)
        
        # Discontinuity through step functions on transformed variables
        discontinuous = 0.25 * np.sum(np.heaviside(np.sin(logistic_terms), 0.5) * 
                                    np.abs(np.cos(logistic_terms)) + 
                                    np.heaviside(np.cos(logistic_terms), 0.5) * 
                                    np.abs(np.sin(logistic_terms)))
        
        # Parameterized bifurcation points with varying sensitivity
        bifurcation = 0.35 * np.sum((1 + 0.2 * np.sin(x)) * np.log(1 + np.abs(logistic_terms)) + 
                                  (1 + 0.1 * np.cos(x)) * np.exp(-np.abs(logistic_terms)))
        
        # Asymmetric landscape with directional preference
        asymmetric = 0.2 * np.sum(np.sin(2 * logistic_terms) * np.abs(np.cos(logistic_terms)) + 
                                np.cos(3 * logistic_terms) * np.abs(np.sin(logistic_terms)))
        
        # Composite function with weighted components
        return 0.7 * (np.sum(logistic_terms**2) + cross_coupling + fractal_terrain + 
                     curvature + discontinuous + bifurcation + asymmetric)