import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with varying degrees and adaptive coefficients
        poly_basin = np.sum(0.5 * x_norm**8 + 0.4 * x_norm**7 + 0.3 * x_norm**6 + 0.2 * x_norm**5 + 0.1 * x_norm**4)
        
        # Multi-frequency sinusoidal modulations with phase shifts
        sin_mod = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(6 * np.pi * x_norm**2) * np.cos(4 * np.pi * x_norm**2) * np.sin(2 * np.pi * x_norm**2))
        
        # Stronger cross-dimensional coupling with higher-order interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * np.pi * (x_norm[i] - x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Novel asymmetric saddle structure with multiple higher-order terms
        saddle = np.sum(x_norm**9 * np.cos(5 * np.pi * x_norm) + 0.7 * x_norm**8 * np.sin(4 * np.pi * x_norm) + 0.5 * x_norm**7 * np.cos(3 * np.pi * x_norm))
        
        # Additional harmonic components with exponential growth for increased complexity
        harmonic = np.sum(np.sin(15 * np.pi * x_norm**4) * np.cos(10 * np.pi * x_norm**4) * np.exp(-x_norm**2))
        
        # Cross-dimensional interference terms
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += (x_norm[i]**2 * x_norm[j]**2) * np.sin(5 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Add noise and scale the function
        noise = 0.015 * np.random.random()
        
        return 2.0 * poly_basin + 1.0 * sin_mod + 0.8 * sin_mod2 + 0.9 * cross_interaction + 0.6 * saddle + 0.4 * harmonic + 0.3 * interference + noise