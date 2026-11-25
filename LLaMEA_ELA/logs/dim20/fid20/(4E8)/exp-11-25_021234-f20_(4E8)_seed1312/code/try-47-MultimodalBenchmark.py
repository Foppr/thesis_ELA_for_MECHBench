import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Periodic parabolic wells with varying depths
        f2 = 0.5 * np.sum((x - np.floor(x / 2.0) * 2.0)**2 * np.sin(np.pi * x)**2)
        
        # Exponentially decaying barriers to create narrow valleys
        f3 = 0.3 * np.sum(np.exp(-0.5 * (x**2)) * np.cos(10.0 * x))
        
        # Asymmetric skewing to bias optimization direction
        skew_factor = 1.0 + 0.3 * np.sin(0.7 * np.sum(x))
        f4 = 0.2 * np.sum(np.abs(x)**1.5 * skew_factor)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        f5 = 0.15 * np.sum(np.sin(5.0 * x + 0.3) * np.cos(3.0 * x - 0.2))
        
        # Cubic terms for additional curvature
        f6 = 0.05 * np.sum(x**3)
        
        # Fractal-like structure using recursive scaling
        f7 = 0.1 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Add a global scaling factor based on input magnitude
        global_scale = 1.0 + 0.2 * np.tanh(0.5 * np.sum(x**2))
        
        return global_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7)