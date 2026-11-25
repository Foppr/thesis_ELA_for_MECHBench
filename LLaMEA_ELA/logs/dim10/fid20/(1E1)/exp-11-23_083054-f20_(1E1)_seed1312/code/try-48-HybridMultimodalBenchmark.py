import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with mixed degrees to create varied curvature
        poly_term = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric components with different frequencies and amplitudes
        trig_term = np.sum(0.8 * np.sin(2 * np.pi * x_norm) ** 2 + 
                          0.6 * np.cos(3 * np.pi * x_norm) ** 2 + 
                          0.4 * np.sin(5 * np.pi * x_norm) ** 2)
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        for center in centers:
            rbfs.append(np.exp(-5 * (x_norm - center)**2))
        rbf_term = np.sum(rbfs)
        
        # Interaction terms between dimensions to increase conditioning
        interaction = np.sum((x_norm[:-1] + x_norm[1:])**2 + 
                           0.3 * (x_norm[:-1] - x_norm[1:])**2)
        
        # Add a global sinusoidal modulation
        global_mod = np.sin(0.5 * np.pi * np.sum(x_norm**2))
        
        # Combine all terms with appropriate weights
        return 0.7 * poly_term + 0.2 * trig_term - 0.1 * rbf_term + 0.05 * interaction + 0.03 * global_mod