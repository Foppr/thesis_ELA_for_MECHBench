import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial term with mixed degrees and cross-terms
        poly_term = np.sum(0.8 * x_scaled**7 + 0.6 * x_scaled**6 + 0.4 * x_scaled**5 + 0.2 * x_scaled**4)
        
        # Enhanced trigonometric terms with multiple frequencies, modulations, and phase shifts
        trig_term = np.sum(np.sin(9 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Radial basis function component with multiple centers and varying widths
        rbf_term = np.sum(np.exp(-7.0 * (x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)))
        
        # Exponential interaction term with more complex structure and higher-dimensional coupling
        exp_interaction = np.sum(np.exp(-(x_scaled[:-1]**2 + x_scaled[1:]**2 + 0.5 * x_scaled[:-1]**3 * x_scaled[1:])) * np.cos(4 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Cross-term with higher-order interactions, sine modulation, and asymmetric weighting
        cross_term = np.sum(x_scaled[:-1]**3 * x_scaled[1:]**3 * np.sin(4 * np.pi * x_scaled[:-1]) * np.cos(2 * np.pi * x_scaled[1:]))
        
        # Shifted global minimum with chaotic perturbations and multi-modal structure
        shift = np.sum((x_scaled - 0.05)**3 + 0.3 * np.sin(6 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Additional noise-like term with chaotic frequency components to increase landscape complexity
        noise_term = np.sum(0.15 * np.sin(12 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled))
        
        # Combine all terms with carefully adjusted weights and introduce a new asymmetric penalty
        return 1.1 * poly_term + 0.6 * trig_term + 0.4 * rbf_term + 0.25 * exp_interaction + 0.2 * cross_term + 0.1 * shift + 0.07 * noise_term + 0.03 * np.sum(np.abs(x_scaled)**3)