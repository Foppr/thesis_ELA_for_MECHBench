import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Polynomial chaos terms with varying exponents
        poly_chaos = np.sum(np.power(np.abs(x_scaled), 3.5) * np.sin(3 * x_scaled))
        
        # Radial basis function components with Gaussian peaks
        rbf_terms = np.sum(np.exp(-5.0 * (x_scaled**2 + 0.1)**2) * np.cos(4 * np.pi * x_scaled))
        
        # Quaternion-inspired coupling terms for multidirectional complexity
        quat_coupling = np.sum((x_scaled**2 + 0.5) * np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Mixed trigonometric interactions with varying frequencies
        trig_interaction = np.sum(np.sin(7 * x_scaled) * np.cos(5 * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Saddle-point and ridge interactions for varied conditioning
        saddle_ridge = np.sum(x_scaled**4 * np.cos(3 * np.pi * x_scaled)) + 0.5 * np.sum(x_scaled**6)
        
        # Cross-term coupling with exponential decay
        cross_coupling = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(6 * np.pi * x_scaled))
        
        # Combined function with diverse curvature and alignment challenges
        return poly_chaos + rbf_terms + quat_coupling + trig_interaction + saddle_ridge + cross_coupling