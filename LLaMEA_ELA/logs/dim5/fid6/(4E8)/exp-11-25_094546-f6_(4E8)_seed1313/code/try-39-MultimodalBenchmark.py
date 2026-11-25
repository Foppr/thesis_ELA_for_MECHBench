import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial terms with higher degrees and adaptive coefficients
        f1 = np.sum(0.8 * x_norm**6 + 0.6 * x_norm**5 + 0.4 * x_norm**4 + 0.2 * x_norm**3 + 0.1 * x_norm**2)
        
        # High-frequency trigonometric terms with varying amplitudes and phases
        f2 = np.sum(1.5 * np.sin(10 * np.pi * x_norm) + 1.0 * np.sin(15 * np.pi * x_norm) + 
                   0.7 * np.sin(20 * np.pi * x_norm) + 0.3 * np.sin(25 * np.pi * x_norm))
        
        # Multiple exponential penalty terms with different decay rates
        f3 = np.sum(np.exp(-2.0 * x_norm**2) + 0.5 * np.exp(-0.5 * x_norm**2) - 1.5)
        
        # Complex cross-dimensional interaction terms with nonlinear coupling
        f4 = np.sum((x_norm[:-1] ** 2) * (x_norm[1:] ** 3) * np.cos(np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Additional radial symmetry components for enhanced multimodality
        radius = np.sqrt(np.sum(x_norm**2))
        f5 = 0.5 * np.sin(12 * np.pi * radius) * np.exp(-0.5 * radius**2)
        
        # Combine all components with adjusted weights for maximum challenge
        return 1.2 * f1 + 0.8 * f2 + 0.6 * f3 + 0.4 * f4 + 0.3 * f5