import numpy as np

class HybridAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        scaled_x = x * np.pi / 5.0
        
        # Polynomial base with varying degrees
        poly_component = np.sum(0.1 * x**6 + 0.2 * x**4 + 0.3 * x**2)
        
        # Trigonometric components with multiple frequencies
        trig_component = np.sum(0.5 * np.sin(2 * scaled_x) + 0.3 * np.cos(3 * scaled_x) + 
                              0.2 * np.sin(5 * scaled_x) + 0.1 * np.cos(7 * scaled_x))
        
        # Exponential decay terms with adaptive scaling
        exp_component = np.sum(0.4 * np.exp(-0.5 * x**2) + 0.3 * np.exp(-0.3 * np.abs(x)) + 
                             0.2 * np.exp(-0.1 * x**4))
        
        # Multi-resolution structure with nested components
        resolution_1 = np.sum(0.15 * np.sin(10 * scaled_x) * np.cos(8 * scaled_x))
        resolution_2 = np.sum(0.1 * np.sin(20 * scaled_x) * np.cos(15 * scaled_x))
        resolution_3 = np.sum(0.05 * np.sin(30 * scaled_x) * np.cos(25 * scaled_x))
        
        # Cross-dimensional interactions with adaptive coupling
        cross_dim = 0.08 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Adaptive scaling based on input magnitude
        adaptive_scale = np.sum(0.2 * (1 + 0.5 * np.tanh(x)) * x**3)
        
        # Fractal-like self-similarity through recursive structure
        fractal = 0.1 * np.sum(np.sin(4 * scaled_x) * np.cos(2 * scaled_x) + 
                             np.sin(8 * scaled_x) * np.cos(4 * scaled_x))
        
        # Multi-modal structure with varying depths
        multimodal = 0.3 * np.sum(np.sin(15 * scaled_x)**2 + np.cos(12 * scaled_x)**2)
        
        # Combined landscape with weighted components
        return (poly_component + trig_component + exp_component + resolution_1 + 
                resolution_2 + resolution_3 + cross_dim + adaptive_scale + fractal + multimodal)